import numpy
import bornagain as ba
from bornagain import deg, angstrom, nm, kvector_t
import matplotlib.pyplot as plt

def get_sample():
    # Defining Materials
    magnetization = ba.kvector_t(0.0, 444e3, 0.0) #parallel to beam
    material_air       = ba.MaterialBySLD("Air", 0.0, 0.0)
    material_oleicAcid = ba.MaterialBySLD("OleicAcid", 0.078e-06, 0e-08)
    material_nc_parallel = ba.MaterialBySLD("Particle", 6.132e-6, 0e-06, magnetization)
    material_nc_antipara = ba.MaterialBySLD("Particle", 6.132e-6, 0e-06, -magnetization)
    material_sio2      = ba.MaterialBySLD("SiO2", 4.186e-6, 0e-07)
    material_si        = ba.MaterialBySLD("Si", 2.079e-6, 0e-07)

    # Defining Layers
    layer_air = ba.Layer(material_air)
    layer_oleicAcid = ba.Layer(material_oleicAcid, 10.18)
    layer_oleicAcid.setNumberOfSlices(10)
    layer_sio2 = ba.Layer(material_sio2, 7.4)
    layer_si = ba.Layer(material_si)

    # Defining Form Factors
    formFactor = ba.FormFactorBox(8.58*nm, 8.58*nm, 8.58*nm)

    # Defining Particles
    particle_position = kvector_t(0.0*nm, 0.0*nm, -10.18*nm)

    composition = ba.ParticleComposition()
    # 1 >   2 >
    # 3 <   4 <
    particle1 = ba.Particle(material_nc_parallel, formFactor)
    particle2 = ba.Particle(material_nc_antipara, formFactor)

    composition.addParticle(particle1, kvector_t(0.0*nm, 0.0*nm, -10.18*nm))
    composition.addParticle(particle1, kvector_t(0.0*nm, 13.28*nm, -10.18*nm))
    composition.addParticle(particle1, kvector_t(13.28*nm, 0.0*nm, -10.18*nm))
    composition.addParticle(particle2, kvector_t(13.28*nm, 13.28*nm, -10.18*nm))

    # Defining Interference Functions
    interference = ba.InterferenceFunction2DParaCrystal(2*13.28*nm, 2*13.28*nm, 90.0*deg, 0.0*deg, 877.0*nm)
    interference.setDomainSizes(877.0*nm, 877.0*nm)
    interference.setIntegrationOverXi(False)
    interference_pdf  = ba.FTDistribution2DGauss(numpy.sqrt(2)*1.63*nm, numpy.sqrt(2)*1.63*nm, 0.0*deg)
    interference.setProbabilityDistributions(interference_pdf, interference_pdf)

    # Defining Particle Layouts and adding Particles
    layout = ba.ParticleLayout()
    layout.addParticle(composition, 1.0)
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


def get_simulation(beam_pol, anal_dir):
    simulation = ba.GISASSimulation()

    detector = ba.RectangularDetector(128, 640, 256, 640)
    detector.setPerpendicularToDirectBeam(5000, 319.225, 326.15)
    simulation.setDetector(detector)

    simulation.setDetectorResolutionFunction(ba.ResolutionFunction2DGaussian(5, 5))
    simulation.setBeamParameters(0.6*nm, 0.35*deg, 0.0*deg)
    simulation.setBeamIntensity(1e9)
    simulation.getOptions().setUseAvgMaterials(True)
    simulation.getOptions().setIncludeSpecular(True)
    background = ba.ConstantBackground(20)
    simulation.setBackground(background)

    simulation.setBeamPolarization(beam_pol)
    simulation.setAnalyzerProperties(anal_dir, 1.0, 0.5)

    # simulation.addMask(ba.Rectangle(100.239, -5.575, 110.293, 98.987), True)  # mask beam stopper
    # simulation.addMask(ba.Rectangle(83.510, -18.363, 85.344, 198.365), True)  # mask detector gap

    simulation.setTerminalProgressMonitor()
    return simulation


def run_simulation():
    sample = get_sample()

    simulation_uu = get_simulation(ba.kvector_t(1.0, 0.0, 0.0), ba.kvector_t(1.0, 0.0, 0.0))
    simulation_uu.setSample(sample)
    simulation_uu.runSimulation()
    hist_uu = simulation_uu.result().histogram2d()
    hist_uu.save("simulation_uu.int")

    simulation_dd = get_simulation(ba.kvector_t(-1.0, 0.0, 0.0), ba.kvector_t(-1.0, 0.0, 0.0))
    simulation_dd.setSample(sample)
    simulation_dd.runSimulation()
    hist_dd = simulation_dd.result().histogram2d()
    hist_dd.save("simulation_dd.int")

    simulation_ud = get_simulation(ba.kvector_t(1.0, 0.0, 0.0), ba.kvector_t(-1.0, 0.0, 0.0))
    simulation_ud.setSample(sample)
    simulation_ud.runSimulation()
    hist_ud = simulation_ud.result().histogram2d()
    hist_ud.save("simulation_ud.int")

    simulation_du = get_simulation(ba.kvector_t(-1.0, 0.0, 0.0), ba.kvector_t(1.0, 0.0, 0.0))
    simulation_du.setSample(sample)
    simulation_du.runSimulation()
    hist_du = simulation_du.result().histogram2d()
    hist_du.save("simulation_du.int")

if __name__ == '__main__':
    run_simulation()