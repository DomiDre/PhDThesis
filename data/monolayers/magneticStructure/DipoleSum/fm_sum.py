import numpy as np
import dipolesum

N = 100
# i_list = np.arange(-N, N+1)
# j_list = np.arange(-N, N+1)

# i2_list = i_list**2
# j2_list = j_list**2

# result = 0
# for i2 in i2_list:
#   for j2 in j2_list:
#     if i2 != 0 or j2 != 0:
#       result = result + (3*j2/(i2+j2)**(2.5) - 1/(i2+j2)**(1.5))

# print(N, result)

# 
fm_result = dipolesum.fm_sum(N)
print(N, fm_result)
afm_result = dipolesum.afm_sum(N)
print(N, afm_result)

print(afm_result - fm_result)

# 10000 4.516528012975453
# 10000 5.098872986929395
