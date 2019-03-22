import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')
import matplotlib.patches as patches
import numpy as np
import uzkChemTem

temFilepath = cwd+"/EF3692_9.tif"
chapter = 'monolayers'
title = 'Ac-CoFe-C'

savefile = chapter+'_TEM_'+title
data = uzkChemTem.load_file(temFilepath)
x = np.array(data['x'])
y = np.array(data['y'])
image_data = np.array(data['data'])
x_range = np.logical_and(x > 70, x < 170) # np.logical_and(x > 260, x < 360)
y_range = np.logical_and(y > 200, y < 300) # np.logical_and(y > 330, y < 430)
plotX = x[x_range]
plotY = y[y_range]
plotData = data['data'][x_range, :][:, y_range]
nm_per_pixel = 6.2313182# data['nm_per_pixel']

scaleBar = 10

label_x0 = 0.64
label_y0 = 0.9
label_y1 = None

fig = plt.figure(frameon=False, figsize=(1,1))
ax = plt.Axes(fig, [0., 0., 1., 1.], )
ax.set_axis_off()
fig.add_axes(ax)
ax.pcolormesh(plotX, plotY, plotData.T, cmap="gray")#, vmin=0.0025, vmax= 0.007)
ax.set_aspect('equal')
# ax.set_xticklabels('')
# ax.set_yticklabels('')
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(plotX[0], plotX[-1])
ax.set_ylim(plotY[0], plotY[-1])

t = ax.text(
  plotX[0]+39.9, plotY[0]+100, str(scaleBar) + ' nm',
  horizontalalignment='center',
  color='black')

ax.figure.canvas.draw()
bb = t.get_window_extent(renderer= fig.canvas.renderer)
transf = ax.transData.inverted()
transfBb = bb.transformed(transf)
textWidth = transfBb.width
textHeight = transfBb.height

t.remove()
offsetTextScalebar = max(textWidth, scaleBar)
rightOffset = 0.5*nm_per_pixel
bottomOffset = 0.5 * nm_per_pixel
ax.add_patch(
  patches.Rectangle(
    (plotX[-1] - rightOffset - textWidth,\
    plotY[0] + bottomOffset),   # (x,y)
    textWidth,          # width
    textHeight,          # height
    color='black',
    alpha=0.5,
    linewidth=0
  ),
)
ax.text(
  plotX[-1] - rightOffset - offsetTextScalebar/2,
  plotY[0] + bottomOffset + textHeight*1/4,
  '$'+str(scaleBar)+' \, nm$',\
  horizontalalignment='center',
  color='#FAFAFA')

ax.add_patch(
  patches.Rectangle(
    (plotX[-1] - rightOffset - offsetTextScalebar/2 - scaleBar*1/2.,\
    plotY[0] + bottomOffset + textHeight*1/20),   # (x,y)
    scaleBar,          # width
    textHeight*1/40,          # height
    color='#FAFAFA'
  )
)
fig.savefig(cwd+'/'+savefile, bbox_inches='tight')
# plt.show()