module dipole_sum
implicit none
  double precision, parameter :: pi = acos(-1d0)
  double precision, parameter :: rad_to_deg = 180d0/pi
  double precision, parameter :: deg = pi/180d0

  double precision, parameter :: mu0 = 201.335452066344 ! T^2 nm^3 / eV
  double precision, parameter :: kB = 8.6173303d-5 ! eV/T
  double precision, parameter :: muB = 5.7883818012d-5 ! eV/T
  double precision, parameter :: eV = 1.6021766208e-19 ! 1eV in J
  double precision, parameter :: eps = tiny(0d0)

  ! init parameters
  double precision :: mu ! in muB
  double precision :: a  ! in nm

contains
subroutine get_b_xy_dipole_fm(&
  xspace, yspace, zcoordinate, ncubes_x, ncubes_y,&
  Nx, Ny, Bmag, Bx, By, Bz)
  double precision, dimension(Nx), intent(in) :: xspace
  double precision, dimension(Ny), intent(in) :: yspace
  double precision, intent(in) :: zcoordinate
  integer, intent(in) :: ncubes_x, ncubes_y

  integer, intent(in) :: Nx, Ny

  double precision, dimension(Nx, Ny), intent(out) :: Bmag, Bx, By, Bz

  double precision, dimension(3) :: vec_B, rvector, r_unit, vec_mu, muDotr
  double precision :: mag_r, Bval
  integer :: ix, iy, i, j
  !
  Bmag = 0d0
  Bx = 0d0
  By = 0d0
  Bz = 0d0
  rvector(3) = zcoordinate
  do i = -ncubes_x, ncubes_x
    do j = -ncubes_y, ncubes_y
      vec_mu = mu*muB*(/ 1, 0, 0/)
      do ix=1, Nx
        rvector(1) = xspace(ix) - i*a
        do iy=1, Ny
          rvector(2) = yspace(iy) - j*a

          mag_r = sqrt(dot_product(rvector, rvector))
          if (mag_r < 1d-3*a) then
            Bmag(ix, iy) = Bmag(ix, iy) + 8*pi/3*sqrt(dot_product(vec_mu, vec_mu))
            Bx(ix, iy) = Bx(ix, iy) + 8*pi/3*vec_mu(1)
            By(ix, iy) = By(ix, iy) + 8*pi/3*vec_mu(2)
            Bz(ix, iy) = Bz(ix, iy) + 8*pi/3*vec_mu(3)
            cycle
          end if
          r_unit = rvector / mag_r
          muDotr = dot_product(vec_mu, r_unit)
          vec_B = (3 * muDotR * r_unit - vec_mu)/mag_r**3
          Bval = sqrt(vec_B(1)**2 + vec_B(2)**2 + vec_B(3)**2)
          Bmag(ix, iy) = Bmag(ix, iy) + Bval
          if (.NOT. (Bval .EQ. 0d0)) then
            Bx(ix, iy) = Bx(ix, iy) + vec_B(1)
            By(ix, iy) = By(ix, iy) + vec_B(2)
            Bz(ix, iy) = Bz(ix, iy) + vec_B(3)
          endif
        end do
      end do
    end do
  end do
  Bx = Bx / Bmag
  By = By / Bmag
  Bz = Bz / Bmag
  Bmag = mu0/4/pi * Bmag
end subroutine get_b_xy_dipole_fm

subroutine get_b_xy_dipole_afm(&
  xspace, yspace, zcoordinate, ncubes_x, ncubes_y,&
  Nx, Ny, Bmag, Bx, By, Bz)
  double precision, dimension(Nx), intent(in) :: xspace
  double precision, dimension(Ny), intent(in) :: yspace
  double precision, intent(in) :: zcoordinate
  integer, intent(in) :: ncubes_x, ncubes_y

  integer, intent(in) :: Nx, Ny

  double precision, dimension(Nx, Ny), intent(out) :: Bmag, Bx, By, Bz

  double precision, dimension(3) :: vec_B, rvector, r_unit, vec_mu, muDotr
  double precision :: mag_r, Bval
  integer :: ix, iy, i, j
  !
  Bmag = 0d0
  Bx = 0d0
  By = 0d0
  Bz = 0d0
  rvector(3) = zcoordinate
  do i = -ncubes_x, ncubes_x
    do j = -ncubes_y, ncubes_y
      vec_mu = mu*muB*(/ (-1)**j, 0, 0/)
      do ix=1, Nx
        rvector(1) = xspace(ix) - i*a
        do iy=1, Ny
          rvector(2) = yspace(iy) - j*a
          mag_r = sqrt(dot_product(rvector, rvector))
          if (mag_r < 1d-3*a) then
            Bmag(ix, iy) = Bmag(ix, iy) + 8*pi/3*sqrt(dot_product(vec_mu, vec_mu))
            Bx(ix, iy) = Bx(ix, iy) + 8*pi/3*vec_mu(1)
            By(ix, iy) = By(ix, iy) + 8*pi/3*vec_mu(2)
            Bz(ix, iy) = Bz(ix, iy) + 8*pi/3*vec_mu(3)
            cycle
          end if
          r_unit = rvector / mag_r
          muDotr = dot_product(vec_mu, r_unit)
          vec_B = (3 * muDotR * r_unit - vec_mu)/mag_r**3
          Bval = sqrt(vec_B(1)**2 + vec_B(2)**2 + vec_B(3)**2)
          Bmag(ix, iy) = Bval
          if (.NOT. (Bval .EQ. 0d0)) then
            Bx(ix, iy) = Bx(ix, iy) + vec_B(1)
            By(ix, iy) = By(ix, iy) + vec_B(2)
            Bz(ix, iy) = Bz(ix, iy) + vec_B(3)
          endif
        end do
      end do
    end do
  end do
  Bx = Bx / Bmag
  By = By / Bmag
  Bz = Bz / Bmag
  Bmag = mu0/4/pi * Bmag
end subroutine get_b_xy_dipole_afm
end module dipole_sum