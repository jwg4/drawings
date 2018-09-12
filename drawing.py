from random import randint


def draw_line(a, b, color="black"):
    TEMPLATE = "    \draw[%s] (%.02f,%.02f) -- (%.02f,%.02f);"
    s = TEMPLATE % (color, a[0], a[1], b[0], b[1])
    return s


def draw_contour(contour):
    contour = list(contour)
    start = contour[0]
    for point in contour[1:]:
        corner = (point[0], start[1])
        yield (start, corner)
        yield (corner, point)
        start = point


def line_max(x, y):
    return x


def create_contour(xmax = 100):
    x = 0
    y = 0
    while x < xmax:
        yield (x, y)
        x = x + 5 + randint(0, 10)
        y = y - 5 + randint(0, 10)
    yield (xmax, y)


if __name__ == '__main__':
    m = None
    for i in range(10):
        print(i)
        f = create_contour()
        m = line_max(f, m)
        for line in draw_contour(m):
            print draw_line(*line)
