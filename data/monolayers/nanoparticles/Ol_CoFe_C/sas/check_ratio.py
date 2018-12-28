
#    sigParticleSize:     0.06232648 +/- 0.00345380 (5.54%) (init = 0.07143705)
#    sigD:                0.17779981 +/- 0.03862594 (21.72%) (init = 0.4038504)
#    i0_saxs:             0.02996434 +/- 2.5195e-04 (0.84%) (init = 0.02369477)
#    bg_saxs:             0 (fixed)
#    orderHermite:        5 (fixed)
#    orderLegendre:       10 (fixed)
#    i0Oleic:             0.69001465 +/- 0.07733582 (11.21%) (init = 0.9518238)
#    rOleic:              21 (fixed)
#    x:                   0.82431744 +/- 0.01406877 (1.71%) (init = 0.9860621)
#    sldCore_sans:        6.223416e-06 (fixed)
#    sldShell_sans:       6.101123e-06 (fixed)
#    sldSurfactant_sans:  7.8e-08 (fixed)
#    sldSolvent_sans:     5.664e-06 (fixed)
#    i0_sans:             0.13027763 +/- 0.00704655 (5.41%) (init = 0.1225224)
#    bg_sans:             0.01358112 +/- 7.5393e-04 (5.55%) (init = 0.01344027)

from scipy import special
import scipy.constants as sc

def superballVolume(r, p):
  def B(x,y):
    return special.gamma(x)*special.gamma(y)/special.gamma(x+y)
  return 2/p**2 * B(1/(2*p), (2*p+1)/(2*p)) * B(1/(2*p), (p+1)/p) * r**3

particleSize = 51.3053730
d = 34.3394593
pVal = 4.09294505
rCore = particleSize - d
vol_wustite = superballVolume(rCore, pVal)
vol_spinell = superballVolume(particleSize, pVal) - vol_wustite

a_wustite = 4.2125
a_spinell = 8.4384

x = 0.82431744
y = 0.47948822
N_Fe = 8*(3-x) * vol_spinell/a_spinell**3 + 4*y*vol_wustite/a_wustite**3
N_Co = 8*x * vol_spinell/a_spinell**3 + 4*(1-y)*vol_wustite/a_wustite**3
print(N_Fe/N_Co)

u = sc.u
m_Fe = 55.845*u
m_Co = 58.933*u
m_O = 15.999*u

density_wustite = 4*(y*m_Fe + (1-y)*m_Co + m_O)/(a_wustite*1e-10)**3 * 1e-3
density_spinell = 8*((3-x)*m_Fe + x*m_Co + 4*m_O)/(a_spinell*1e-10)**3 * 1e-3

print(f"rho_wustite: {density_wustite} g/mL")
print(f"rho_spinell: {density_spinell} g/mL")

i0_saxs = 0.02996434
i0_sans = 0.13027763

print(f"cm saxs = {i0_saxs*1e-8*(density_wustite*vol_wustite + density_spinell*vol_spinell)*1e3} mg/mL")
print(f"cm sans = {i0_sans*1e-8*(density_wustite*vol_wustite + density_spinell*vol_spinell)*1e3} mg/mL")