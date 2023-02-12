import matplotlib.pyplot as plt
import numpy as np
from linearInterpolation import bilinear
from cubic_interpolation import cubic_interpolation

methods = ['None', 'Bilinear', 'Bicubic']
# Fixing random state for reproducibility
np.random.seed()

grid = np.random.rand(15, 15)

fig, axs = plt.subplots(nrows=1, ncols=3, subplot_kw={'xticks': [], 'yticks': []})
cmap = 'viridis'
for ax, interp_method in zip(axs.flat, methods):
    if interp_method == 'None':
        ax.imshow(grid, cmap=cmap)
    elif interp_method == 'Bilinear':
        ax.imshow(bilinear(grid, (30, 30)), cmap=cmap)
    elif interp_method == 'Bicubic':
        ax.imshow(cubic_interpolation(grid, (30, 30)))
    ax.set_title(str(interp_method))

# fig = plt.figure(figsize=(7, 4))
# ax_3d = fig.add_subplot(projection='3d')
# ax_3d.set_xlabel('x')
# ax_3d.set_ylabel('y')
# ax_3d.set_zlabel('z')
# z = bilinear(grid, (30, 30))
# x = np.linspace(-1, 1, z.shape[0])
# y = np.linspace(-1, 1, z.shape[1])
# x_2d, y_2d = np.meshgrid(x, y)
# ax_3d.plot_surface(x_2d, y_2d, z, cmap='plasma')

plt.tight_layout()
plt.show()
