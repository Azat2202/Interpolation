import matplotlib.pyplot as plt
import numpy as np
from linearInterpolation import bilinear

methods = ['None', 'Bilinear']
# Fixing random state for reproducibility
np.random.seed(22022004)

grid = np.random.rand(4, 4)

fig, axs = plt.subplots(nrows=1, ncols=2, subplot_kw={'xticks': [], 'yticks': []})

for ax, interp_method in zip(axs.flat, methods):
    if interp_method == 'None':
        ax.imshow(grid)
    elif interp_method == 'Bilinear':
        # bilinear(grid)
        ax.imshow(bilinear(grid))
    ax.set_title(str(interp_method))

plt.tight_layout()
plt.show()
