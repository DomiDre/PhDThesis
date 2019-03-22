f2py3 -m dipole_sum --opt=-O3 --f90flags='-fopenmp' -lgomp \
      -c DipoleSum.f90
