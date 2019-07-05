import numpy
import bornagain as ba
from bornagain import deg, angstrom, nm, kvector_t
import matplotlib.pyplot as plt

def get_sample():
    # Defining Materials
    material_air       = ba.MaterialBySLD("Air", 0.0, 0.0)
    material_oleicAcid = ba.MaterialBySLD("OleicAcid", 8.52e-06, 1.3e-08)
    material_nc        = ba.MaterialBySLD("Particle", 4.121e-05, 3e-06)
    material_sio2      = ba.MaterialBySLD("SiO2", 2.26763e-05, 2.232e-07)
    material_si        = ba.MaterialBySLD("Si", 2.0064e-05, 3.5e-07)

    # Defining Layers
    layer_air = ba.Layer(material_air)
    layer_oleicAcid = ba.Layer(material_oleicAcid, 10.08)
    layer_oleicAcid.setNumberOfSlices(10)
    layer_sio2 = ba.Layer(material_sio2, 7.7)
    layer_si = ba.Layer(material_si)

    # Defining Form Factors
    formFactor = ba.FormFactorBox(8.58*nm, 8.58*nm, 8.58*nm)

    # Defining Particles
    particle = ba.Particle(material_nc, formFactor)
    particle_position = kvector_t(0.0*nm, 0.0*nm, -10.18*nm)
    particle.setPosition(particle_position)

    # Defining particles with parameter following a distribution
    distr = ba.DistributionLogNormal(8.58*nm, 1.0)
    par_distr = ba.ParameterDistribution("/Particle/Box/Length", distr, 5, 0.15)
    par_distr.linkParameter("/Particle/Box/Width").linkParameter("/Particle/Box/Height")
    particleDistribution = ba.ParticleDistribution(particle, par_distr)

    # Defining Interference Functions
    interference = ba.InterferenceFunction2DParaCrystal(13.28*nm, 13.28*nm, 90.0*deg, 0.0*deg, 877.0*nm)
    interference.setDomainSizes(877.0*nm, 877.0*nm)
    interference.setIntegrationOverXi(True)
    interference_pdf  = ba.FTDistribution2DGauss(1.63*nm, 1.63*nm, 0.0*deg)
    interference.setProbabilityDistributions(interference_pdf, interference_pdf)

    # Defining Particle Layouts and adding Particles
    layout = ba.ParticleLayout()
    layout.addParticle(particleDistribution, 1.0)
    layout.setInterferenceFunction(interference)

    # Adding layouts to layers
    layer_oleicAcid.addLayout(layout)

    # Defining Multilayers
    multiLayer = ba.MultiLayer()
    multiLayer.addLayer(layer_air)
    multiLayer.addLayer(layer_oleicAcid)
    multiLayer.addLayer(layer_sio2)
    multiLayer.addLayer(layer_si)
    return multiLayer


def get_simulation():
    simulation = ba.GISASSimulation()

    detector = ba.RectangularDetector(981, 168.732, 1043, 179.396)
    detector.setPerpendicularToDirectBeam(1733.5, 105.0, 58.206)
    simulation.setDetector(detector)

    simulation.setDetectorResolutionFunction(ba.ResolutionFunction2DGaussian(0.254, 0.254))
    simulation.setBeamParameters(0.13414*nm, 0.13*deg, 0.0*deg)
    simulation.setBeamIntensity(6.246e+09)
    simulation.getOptions().setUseAvgMaterials(True)
    simulation.getOptions().setIncludeSpecular(True)
    background = ba.ConstantBackground(1.0e+00)
    simulation.setBackground(background)
    simulation.addMask(ba.Rectangle(100.239, -5.575, 110.293, 98.987), True)  # mask beam stopper
    simulation.addMask(ba.Rectangle(83.510, -18.363, 85.344, 198.365), True)  # mask detector gap

    simulation.setTerminalProgressMonitor()
    return simulation


def run_simulation():
    sample = get_sample()
    simulation = get_simulation()
    simulation.setSample(sample)
    simulation.runSimulation()
    return simulation.result()


if __name__ == '__main__':
    result = run_simulation()
    hist = result.histogram2d()
    hist.save("simulation.int")
    fig = plt.figure()
    ba.plot_colormap(result, units=ba.AxesUnits.QSPACE, title="Q-space",
                     xlabel=r'$Q_{y} [1/nm]$', ylabel=r'$Q_{z} [1/nm]$', zlabel=None)
    plt.show()