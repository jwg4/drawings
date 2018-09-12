from random import randint, choice


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


def line_max(a, b):
    a = ( A for A in a )
    b = ( B for B in b )
    a_over = b_over = False
    a1 = b1 = (0, 0)
    ay = by = 0

    try:
        a1 = next(a)
    except StopIteration:
        a_over = True
    try:
        b1 = next(b)
    except StopIteration:
        b_over = True

    while not (a_over and b_over):
        if not a_over and (a1[0] <= b1[0] or b_over):
            ay = a1[1]
            x = a1[0]
            try:
                a1 = next(a)
            except StopIteration:
                a_over = True
        if not b_over and (b1[0] <= a1[0] or a_over):
            by = b1[1]
            x = b1[0]
            try:
                b1 = next(b)
            except StopIteration:
                b_over = True
        yield (x, max(ay, by))


def create_contour(level=0, xmax = 100):
    x = 0
    y = level
    while x < xmax:
        yield (x, y)
        x = x + 5 + randint(0, 10)
        y = y - 5 + randint(0, 10)
    yield (xmax, y)


if __name__ == '__main__':
    m = []
    for i in range(10):
        f = list(create_contour(i * 5))
        m = list(line_max(f, m))
        for line in draw_contour(m):
            print draw_line(*line)
