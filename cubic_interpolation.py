import numpy as np


def cubic_interpolation(grid, resize):
    return extrapolation(grid)


def extrapolation(grid):
    out = np.zeros(np.add(grid.shape, 2), dtype=grid.dtype)  # массив нулей этой размерности
    out[1:grid.shape[0] + 1, 1:grid.shape[1] + 1] = grid  # ну теперь тут ОЧЕВ
    return out
