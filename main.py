__author__ = 'Marek'
import numpy as np
from pylab import show
from matplotlib.pyplot import scatter,plot

points = [(np.random.randint(0, 100), np.random.randint(0, 100)) for i in range(20)]

def add_points(list_in) -> list:
    list_out = []
    r = 5
    dx = .6 * r
    dy = .4 * r
    dr = np.sqrt(dx**2 + dy**2)/2
    for point in list_in:
        list_out.append((point[0] - dx, point[1]))
        list_out.append((point[0] + dx, point[1]))
        list_out.append((point[0], point[1] - dy))
        list_out.append((point[0], point[1] + dy))
        list_out.append((point[0] - dr, point[1] - dr))
        list_out.append((point[0] - dr, point[1] + dr))
        list_out.append((point[0] + dr, point[1] - dr))
        list_out.append((point[0] + dr, point[1] + dr))
    return list_out

def jarvis(list_in) -> list:
    final = [min(list_in, key=lambda t: t[1])]
    final = [(0, final[0][1])] + final
    n = (-1, -1)
    while not n == final[1]:
        angles = [angle(final[-2], final[-1], point) for point in list_in]
        index = angles.index(max(angles))
        n = list_in[index]
        final.append(n)
    return final[1:]

def angle(previous, actual, check) -> float:
    assert actual, tuple
    assert previous, tuple
    assert check, tuple
    a = np.sqrt((actual[0] - previous[0])**2 + (actual[1] - previous[1])**2)
    b = np.sqrt((actual[0] - check[0])**2 + (actual[1] - check[1])**2)
    c = np.sqrt((previous[0] - check[0])**2 + (previous[1] - check[1])**2)
    np.seterr(all='raise')
    try:
        return np.arccos((a**2 + b**2 - c**2)/(2 * a * b))
    except FloatingPointError:
        return 0

plot(*zip(*jarvis(add_points(points))))
scatter(*zip(*points), s=100)
scatter(*zip(*add_points(points)), s=20, c='g')
show()
