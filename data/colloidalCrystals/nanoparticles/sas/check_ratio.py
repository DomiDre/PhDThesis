from scipy import special

def superballVolume(r, p):
  def B(x,y):
    return special.gamma(x)*special.gamma(y)/special.gamma(x+y)
  return 2/p**2 * B(1/(2*p), (2*p+1)/(2*p)) * B(1/(2*p), (p+1)/p) * r**3

particleSize = 52.769999
d = 18.9209031
pVal = 2.18290421
rCore = particleSize - d
vol_wustite = superballVolume(rCore, pVal)
vol_spinell = superballVolume(particleSize, pVal) - vol_wustite

a_wustite = 4.2125
a_spinell = 8.4384

x = 0.27099
y = 0.30502398
N_Fe = 8*(3-x) * vol_spinell/a_spinell**3 + 4*y*vol_wustite/a_wustite**3
N_Co = 8*x * vol_spinell/a_spinell**3 + 4*(1-y)*vol_wustite/a_wustite**3
print(N_Fe/N_Co)