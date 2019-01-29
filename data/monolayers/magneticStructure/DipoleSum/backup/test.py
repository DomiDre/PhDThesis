import numpy as np


N = 100
s = 5/2
i_list = np.arange(-N, N)
j_list = np.arange(-N, N)

i2_list = i_list**2
j2_list = j_list**2

result = 0
# for i2 in i2_list:
#   for j2 in j2_list:
#     if i2 >0 and j2>0:
#       result += j2 / (i2+j2)**s
for i2 in i2_list:
  for j2 in j2_list:
    if i2 >0 and j2>0:
      result += 1 / (i2+j2)**(s-1)
result /= 2

print(N, s, result)