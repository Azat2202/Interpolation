import numpy as np


def bilinear(grid: np):
    new_grid = dilation1(grid, (7, 7))
    x_dim, y_dim = 7, 7
    print(x_dim, y_dim)
    # for x, line in enumerate(new_grid):
    #     for y, num in enumerate(new_grid):
    x = 0
    y = 17
    Q12 = (x // x_dim * 7, y // y_dim * 7, grid[y // y_dim, x // x_dim])
    Q22 = ((x // x_dim + 1) * 7, y // y_dim * 7, grid[y // y_dim, x // x_dim + 1])
    Q11 = (x // x_dim * 7, (y // y_dim + 1) * 7, grid[y // y_dim + 1, x // x_dim ])
    Q21 = ((x // x_dim + 1) * 7, (y // y_dim + 1) * 7, grid[y // y_dim + 1, x // x_dim + 1])
    print(grid)
    print(Q12)
    print(Q22)
    print(Q11)
    print(Q21)
    return new_grid


def dilation1(X, d):
    Xd_shape = np.multiply(X.shape, d) - d + 1  # создаем размер будущего массива взяв вводный массив и умножив на нужный размер
    Xd = np.zeros(Xd_shape, dtype=X.dtype)  # массив нулей этой размерности
    Xd[0:Xd_shape[0]:d[0], 0:Xd_shape[1]:d[1]] = X  # ну теперь тут ОЧЕВ
    return Xd
