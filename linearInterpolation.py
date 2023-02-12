import numpy as np


def bilinear(grid: np, resize):
    new_grid = dilation1(grid, resize)
    x_dim, y_dim = resize
    new_x_dim, new_y_dim = new_grid.shape
    for x, line in enumerate(new_grid):
        for y, num in enumerate(line):
            if num != 0:
                continue
            elif x == new_x_dim - 1:
                new_grid[x, y] = linear_intorpolation(y, y // y_dim * y_dim, grid[x // x_dim, y // y_dim],
                                                      (y // y_dim + 1) * y_dim, grid[x // x_dim, y // y_dim + 1])
            elif y == new_y_dim - 1:
                new_grid[x, y] = linear_intorpolation(x, x // x_dim * x_dim, grid[x // x_dim, y // y_dim],
                                                      (x // x_dim + 1) * x_dim, grid[x // x_dim + 1, y // y_dim])
            else:
                Q12 = (x // x_dim * x_dim, y // y_dim * y_dim, grid[x // x_dim, y // y_dim])
                Q22 = ((x // x_dim + 1) * x_dim, y // y_dim * y_dim, grid[x // x_dim + 1, y // y_dim])
                Q11 = (x // x_dim * x_dim, (y // y_dim + 1) * y_dim, grid[x // x_dim, y // y_dim + 1])
                Q21 = ((x // x_dim + 1) * x_dim, (y // y_dim + 1) * y_dim, grid[x // x_dim + 1, y // y_dim + 1])
                new_grid[x, y] = interpolation_func(x, y, Q11, Q21, Q12, Q22)
    return new_grid


def linear_intorpolation(x, x0, y0, x1, y1):
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)


def interpolation_func(x, y, Q11, Q21, Q12, Q22) -> float:
    x1, y1 = Q11[:2]
    x2, y2 = Q22[:2]
    # https://wikimedia.org/api/rest_v1/media/math/render/svg/29f2d04b9fc6a4f69e385aaf1ccb935ecfe46bf8
    return (Q11[2] * (x2 - x) * (y2 - y)) / ((x2 - x1) * (y2 - y1)) + \
           (Q21[2] * (x - x1) * (y2 - y)) / ((x2 - x1) * (y2 - y1)) + \
           (Q12[2] * (x2 - x) * (y - y1)) / ((x2 - x1) * (y2 - y1)) + \
           (Q22[2] * (x - x1) * (y - y1)) / ((x2 - x1) * (y2 - y1))


def dilation1(X, d):
    Xd_shape = np.multiply(X.shape,
                           d) - d + 1  # создаем размер будущего массива взяв вводный массив и умножив на нужный размер
    Xd = np.zeros(Xd_shape, dtype=X.dtype)  # массив нулей этой размерности
    Xd[0:Xd_shape[0]:d[0], 0:Xd_shape[1]:d[1]] = X  # ну теперь тут ОЧЕВ
    return Xd
