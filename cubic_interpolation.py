import numpy as np


def cubic_interpolation(grid, resize):
    return extrapolation(grid)


def extrapolation(grid):
    out = np.zeros(np.add(grid.shape, 2), dtype=grid.dtype)
    # Центральные клетки:
    out[1:grid.shape[0] + 1, 1:grid.shape[1] + 1] = grid
    # Вертикали и горизонтали:
    for i, num in enumerate(out[0, 1:out.shape[1]]):
        out[0, i] = max(0, min(1, out[2, i] + (out[1, i] - out[2, i]) * 2))
        k = out.shape[1] - 1
        out[k, i] = max(0, min(1, out[k - 2, i] + (out[k - 1, i] - out[k - 2, i]) * 2))
    for i, num in enumerate(out[1:out.shape[0], 0]):
        out[i, 0] = max(0, min(1, out[i, 2] + (out[i, 1] - out[i, 2]) * 2))
        k = out.shape[0] - 1
        out[i, k] = max(0, min(1, out[i, k - 2] + (out[i, k - 1] - out[i, k - 2]) * 2))
    # Углы:
    out[0, 0] = (out[1, 0] + out[0, 1]) / 2
    out[out.shape[0] - 1, 0] = (out[out.shape[0] - 2, 0] + out[out.shape[0] - 1, 1]) / 2
    out[0, out.shape[1] - 1] = (out[1, out.shape[1] - 1] + out[0, out.shape[1] - 2]) / 2
    out[out.shape[0] - 1, out.shape[1] - 1] = (out[out.shape[0] - 2, out.shape[1] - 1] + out[out.shape[0] - 1, out.shape[1] - 2]) / 2
    return out
