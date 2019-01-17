double precision function field_sum(N, z)
    implicit none
    integer, intent(in) :: N
    double precision, intent(in) :: z
    integer :: i, j, i2, j2
    double precision :: z2, sum_value
    z2 = z**2
    sum_value = 0d0
    do i=-N, N
        i2 = i**2
        do j=-N, N
            j2 = j**2
            sum_value  = sum_value + (2d0*i2 - j2 - z2) / (i2 + j2 + z2)**(2.5d0)
        end do
    end do
    field_sum = sum_value
end function field_sum

double precision function optimized_field_sum(N, z)
    implicit none
    integer, intent(in) :: N
    double precision, intent(in) :: z
    integer :: i, j
    double precision :: i2, j2
    double precision :: z2, double_sum, single_sum
    z2 = z**2
    double_sum = 0d0
    single_sum = 0d0
    do i=1, N
        i2 = i**2
        do j=1, N
            j2 = j**2
            double_sum  = double_sum + (2d0*i2 - j2 - z2) / (i2 + j2 + z2)**(2.5d0)
        end do
    end do

    do i=1, N
        i2 = i**2
        single_sum  = single_sum + (i2 - 2*z2) / (i2 + z2)**(2.5d0)
    end do

    optimized_field_sum = -1/z**3 + 2*single_sum + 4*double_sum
end function optimized_field_sum
