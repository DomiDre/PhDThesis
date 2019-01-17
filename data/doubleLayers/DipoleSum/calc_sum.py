import numpy as np
import fieldsum

N = 1000
# z_val = 10
# # fm_result = fieldsum.optimized_field_sum(N, z_val)
# fm_result = fieldsum.field_sum(N, z_val)
# print(z_val, fm_result)
      
if 1:
  with open('field_sums.xy', 'w') as f:
    f.write('#Generated dipole sums of a layer.\n')
    f.write(f'#Number of Sites N = {N}.\n')
    f.write('#z \t f(z)\n')
    for z_val in np.arange(0.1, 5, 0.05):
      fm_result = fieldsum.optimized_field_sum(N, z_val)
      print(z_val, fm_result)
      f.write(f'{z_val}\t{fm_result}\n')
