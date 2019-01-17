
double precision function fm_sum(N)
    implicit none
    integer, intent(in) :: N
    integer :: i, j, i2, j2
    double precision :: sum_value
    sum_value = 0d0
    do i=-N, N
        i2 = i**2
        do j=-N, N
            if (i == 0 .and. j == 0) cycle
            j2 = j**2
            sum_value  = sum_value + (3d0*j2 / (i2 + j2)**(2.5d0) - 1d0/(i2 + j2)**(1.5d0))
        end do
    end do
    fm_sum = sum_value
end function fm_sum

double precision function afm_sum(N)
    implicit none
    integer, intent(in) :: N

    integer :: i, j, i2, j2, prefac
    double precision :: sum_value
    sum_value = 0d0
    do i=-N, N
        i2 = i**2
        prefac = (-1)**i
        do j=-N, N
            if (i == 0 .and. j == 0) cycle
            j2 = j**2
            sum_value  = sum_value + prefac*(3d0*j2 / (i2 + j2)** (2.5d0) - 1d0 / (i2 + j2)** (1.5d0))
        end do
    end do
    afm_sum = sum_value
end function afm_sum
