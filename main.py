import matplotlib.backend_bases
import numpy as np
import matplotlib.pyplot as plt

x_cord = [1, 3, 5, 7, 10]  # x-координаты из таблицы
y_cord = [2, -5, 6, 2, -7]  # y-координаты из таблицы
x_size = [min(x_cord), max(x_cord)]
amplitude = max(y_cord) - min(y_cord)
y_size = [min(y_cord) - amplitude, max(y_cord) + amplitude]


def Li(i, x):
    buf = 1
    for j in range(len(x_cord)):
        if i != j:
            buf *= (x - x_cord[j]) / (x_cord[i] - x_cord[j])
    return buf


def lagrange(x):
    sum_ = 0
    for i in range(len(x_cord)):
        sum_ += y_cord[i] * Li(i, x)
    return sum_


def onclick(event: matplotlib.backend_bases.KeyEvent):
    global x_cord, y_cord
    if event.key == 'a':
        plt.clf()
        x_cord.append(event.xdata)
        y_cord.append(event.ydata)
        x_cord, y_cord = [i for i, j in sorted(zip(x_cord, y_cord))], [j for i, j in sorted(zip(x_cord, y_cord))]
        draw()


def draw():
    x = np.linspace(min(x_cord), max(x_cord))
    plt.xlim(x_size)
    plt.ylim(y_size)
    plt.plot(x, lagrange(x), '-g')
    plt.plot(x_cord, y_cord, 's')
    plt.grid(which='major')
    plt.draw()


def main():
    fig, ax = plt.subplots()
    draw()
    cid = fig.canvas.mpl_connect('key_press_event', onclick)
    plt.show()
    plt.draw()


if __name__ == '__main__':
    main()
