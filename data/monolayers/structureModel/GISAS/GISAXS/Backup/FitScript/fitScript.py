import numpy
import bornagain as ba
from bornagain import deg, angstrom, nm, kvector_t

# ... 99%FitPrintService::update() -> Info. NCall:28 Chi2:5.02808674e+00
# Wall time since last call:133.17
# i0               6.246000e+09 limited(1.00e+08,1.00e+11)  8.430827e+09
# bg               1.576160e+00 limited(0.00e+00,5.00e+00)  2.160701e+00
# latticeConstant  1.321700e+01 limited(1.10e+01,1.50e+01)  1.294117e+01
# domainSize       8.770000e+02 limited(1.00e+02,5.00e+03)  8.770000e+02
# nNUncertainty    2.200000e+00 limited(5.00e-01,5.00e+00)  2.891970e+00

class SampleBuilder:
  def __init__(self):
    self.latticeConstant = 13.217*nm
    self.domainSize = 877.0*nm
    self.nNUncertainty = 1.685*nm

  def create_sample(self, params):
    self.latticeConstant = params["latticeConstant"]
    self.domainSize = params["domainSize"]
    self.nNUncertainty = params["nNUncertainty"]
    return self.samplelayer()

  def samplelayer(self):
    # Defining Materials
    material_air  = ba.MaterialBySLD("Air",       0.0,         0.0)
    material_oa   = ba.MaterialBySLD("OleicAcid", 8.52e-06,    1.3e-08)
    material_nc   = ba.MaterialBySLD("Particle",  4.119e-05,   3e-06)
    material_sio2 = ba.MaterialBySLD("SiO2",      2.26763e-05, 2.232e-07)
    material_si   = ba.MaterialBySLD("Si",        2.0064e-05,  3.5e-07)

    # Defining Layers
    layer_air = ba.Layer(material_air)
    layer_oa = ba.Layer(material_oa, 10.18)
    layer_sio2 = ba.Layer(material_sio2, 7.4)
    layer_si = ba.Layer(material_si)

    # Defining Form Factors
    formFactor = ba.FormFactorBox(8.58*nm, 8.58*nm, 8.58*nm)

    # Defining Particles
    particle = ba.Particle(material_nc, formFactor)
    particle_position = kvector_t(0.0*nm, 0.0*nm, -10.18*nm)
    particle.setPosition(particle_position)

    # Defining Interference Functions
    interference = ba.InterferenceFunction2DParaCrystal(self.latticeConstant, self.latticeConstant, 90.0*deg, 0.0*deg, 0.0*nm)
    interference.setDomainSizes(self.domainSize, self.domainSize)
    interference.setIntegrationOverXi(True)
    interference_pdf_1  = ba.FTDistribution2DGauss(self.nNUncertainty, self.nNUncertainty, 0.0*deg)
    interference_pdf_2  = ba.FTDistribution2DGauss(self.nNUncertainty, self.nNUncertainty, 0.0*deg)
    interference.setProbabilityDistributions(interference_pdf_1, interference_pdf_2)

    # Defining Particle Layouts and adding Particles
    layout_1 = ba.ParticleLayout()
    layout_1.addParticle(particle, 1.0)
    layout_1.setInterferenceFunction(interference)
    layout_1.setTotalParticleSurfaceDensity(0.00572445597905)

    # Adding layouts to layers
    layer_oa.addLayout(layout_1)

    # Defining Multilayers
    multiLayer = ba.MultiLayer()
    multiLayer.addLayer(layer_air)
    multiLayer.addLayer(layer_oa)
    multiLayer.addLayer(layer_sio2)
    multiLayer.addLayer(layer_si)
    return multiLayer


def create_simulation(params):
  i0 = params['i0']
  bg = params['bg']

  simulation = ba.GISASSimulation()

  detector = ba.RectangularDetector(981, 168.732, 1043, 179.396)
  detector.setPerpendicularToDirectBeam(1733.5, 105.0, 58.206)
  simulation.setDetector(detector)

  simulation.setDetectorResolutionFunction(ba.ResolutionFunction2DGaussian(0.254, 0.254))
  simulation.setBeamParameters(0.134*nm, 0.15*deg, 0.0*deg)
  simulation.setBeamIntensity(i0)
  simulation.getOptions().setUseAvgMaterials(True)
  background = ba.ConstantBackground(bg)
  simulation.setBackground(background)
  simulation.setRegionOfInterest(16.983, 62.960, 165.928, 159.477)
  simulation.addMask(ba.Rectangle(100.239, -5.575, 110.293, 98.987), True)  # mask beam stopper
  simulation.addMask(ba.Rectangle(83.510, -18.363, 85.344, 198.365), True)  # mask detector gap

  #simulation.getOptions().setIncludeSpecular(True)
  simulation.setTerminalProgressMonitor()

  sample_builder = SampleBuilder()
  sample = sample_builder.create_sample(params)
  simulation.setSample(sample)
  return simulation


# def run_simulation():
#   sample = get_sample()
#   simulation = get_simulation()
#   simulation.setSample(sample)
#   simulation.runSimulation()
#   return simulation.result()


if __name__ == '__main__':

  real_data = ba.IntensityDataIOFactory.readIntensityData("DD175_28_data.txt.gz").array()
  fit_objective = ba.FitObjective()
  fit_objective.addSimulationAndData(create_simulation, real_data, 1.0)
  fit_objective.initPrint(1)
  fit_objective.initPlot(1)

  params = ba.Parameters()
  params.add("i0", 6.246e+09,               min=1e8,     max=1e11,      step=0.1e8)
  params.add("bg", 1.57616,                     min=0,       max=5,         step=0.1)
  params.add("latticeConstant", 13.217*nm,  min=11.0*nm, max=15.0*nm,   step=0.1*nm)
  params.add("domainSize", 877,             min=100,     max=5000,      step=10)
  params.add("nNUncertainty", 2.2*nm,     min=0.5*nm,  max=5*nm,      step=0.01*nm)

  minimizer = ba.Minimizer()
  result = minimizer.minimize(fit_objective.evaluate, params)
  fit_objective.finalize(result)

# result = run_simulation()
# ba.plot_simulation_result(result)
