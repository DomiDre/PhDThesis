import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

cube_size = 10
pp_distance = 13
Nx = 3
Ny = 3
fig = plt.figure()
ax = fig.add_subplot(111)
M_direction = (0,1)
for ix in range(Nx):
    for iy in range(Ny):

        #1
        ax.add_patch(
            patches.Rectangle(
                (ix*2*pp_distance, iy*2*pp_distance),   # (x,y)
                cube_size,          # width
                cube_size,          # height
                fill=False
            )
        )
        ax.arrow(ix*2*pp_distance + cube_size/2,
                 iy*2*pp_distance + cube_size/4,
                 M_direction[0]*cube_size/2,
                 M_direction[1]*cube_size/2,
                 head_width=1, head_length=1, fc='k', ec='k')
        #2
        ax.add_patch(
            patches.Rectangle(
                (pp_distance+ix*2*pp_distance, iy*2*pp_distance),   # (x,y)
                cube_size,          # width
                cube_size,          # height
                fill=False
            )
        )
        ax.arrow(pp_distance+ix*2*pp_distance + cube_size/2,
                 iy*2*pp_distance + 3*cube_size/4,
                 M_direction[0]*cube_size/2,
                 -M_direction[1]*cube_size/2,
                 head_width=1, head_length=1, fc='k', ec='k')

        #3
        ax.add_patch(
            patches.Rectangle(
                (ix*2*pp_distance, pp_distance+iy*2*pp_distance),   # (x,y)
                cube_size,          # width
                cube_size,          # height
                fill=False
            )
        )
        ax.arrow(ix*2*pp_distance + cube_size/2,
                 pp_distance+iy*2*pp_distance + cube_size/4,
                 M_direction[0]*cube_size/2,
                 M_direction[1]*cube_size/2,
                 head_width=1, head_length=1, fc='k', ec='k')

        #4
        ax.add_patch(
            patches.Rectangle(
                (pp_distance+ix*2*pp_distance, pp_distance+iy*2*pp_distance),   # (x,y)
                cube_size,          # width
                cube_size,          # height
                fill=False
            )
        )
        ax.arrow(pp_distance+ix*2*pp_distance + cube_size/2,
                 pp_distance+iy*2*pp_distance + 3*cube_size/4,
                 M_direction[0]*cube_size/2,
                 -M_direction[1]*cube_size/2,
                 head_width=1, head_length=1, fc='k', ec='k')

ax.set_xlim(-5, 80)
ax.set_ylim(-5, 80)
ax.set_xlabel('$y \, / \, \mathrm{nm}$')
ax.set_ylabel('$x \, / \, \mathrm{nm}$')
fig.tight_layout()
plt.savefig('config1.png')
plt.show()