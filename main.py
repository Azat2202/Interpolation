import matplotlib.backend_bases
import numpy as np
import matplotlib.pyplot as plt

x_cord = [1, 3, 5, 7, 10]  # x-координаты из таблицы
y_cord = [2, -5, 6, 2, -7]  # y-координаты из таблицы
n = len(x_cord)


def Li(i, x):
    buf = 1
    for j in range(n):
        if i != j:
            buf *= (x - x_cord[j]) / (x_cord[i] - x_cord[j])
    return buf


def lagrange(x):
    sum_ = 0
    for i in range(n):
        sum_ += y_cord[i] * Li(i, x)
    return sum_


# def onclick(event: matplotlib.backend_bases.MouseEvent):
#     print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
#           ('double' if event.dblclick else 'single', event.button,
#            event.x, event.y, event.xdata, event.ydata))

def onclick(event: matplotlib.backend_bases.KeyEvent):
    print(event.xdata, event.ydata, event.key)


def main():
    x = np.linspace(min(x_cord) - 10, max(x_cord) + 10)
    fig, ax = plt.subplots()

    ax.plot(x, lagrange(x))

    plt.xlim([min(x_cord), max(x_cord)])
    amplitude = max(y_cord) - min(y_cord)
    plt.ylim([min(y_cord) - amplitude, max(y_cord) + amplitude])

    plt.grid(which='major')

    cid = fig.canvas.mpl_connect('key_press_event', onclick)

    plt.show()


if __name__ == '__main__':
    main()
