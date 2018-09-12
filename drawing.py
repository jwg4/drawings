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
    """
        >>> list(line_max([(0, 41), (63, 49), (86, 58), (100, 58)], [(0, 42), (34, 50), (56, 53), (100, 53)]))
        [(0, 42), (34, 50), (56, 53), (86, 58), (100, 58)]
    """
    a = ( A for A in a )
    b = ( B for B in b )
    a_over = b_over = False
    a1 = b1 = (0, 0)
    x = ay = by = 0
    old_my = None

    try:
        a1 = next(a)
        ay = a1[1]
    except StopIteration:
        a_over = True
    try:
        b1 = next(b)
        by = b1[1]
    except StopIteration:
        b_over = True

    while not (a_over and b_over):
        if not a_over and (a1[0] <= b1[0] or b_over):
            my = max(ay, by)
            if my != old_my:
                yield (x, my)
                old_my = my
            ay = a1[1]
            x = a1[0]
            try:
                a1 = next(a)
            except StopIteration:
                a_over = True
        if not b_over and (b1[0] <= a1[0] or a_over):
            my = max(ay, by)
            if my != old_my:
                yield (x, my)
                old_my = my
            by = b1[1]
            x = b1[0]
            try:
                b1 = next(b)
            except StopIteration:
                b_over = True
    yield (x, my)


def create_contour(level=0, xmax=100, scale=5):
    x = 0
    d = 1
    y = level
    while x < xmax:
        if d == 0:
            d = randint(0, 3 * scale)
        else:
            d = 0
        yield (x, y + d)
        y = y - scale + randint(0, 2 * scale)
        x = x + scale + randint(0, scale)
    yield (xmax, y)


if __name__ == '__main__':
    m = []
    height = 0
    n = 15
    for i in range(n):
        size = n - i + 1
        height = height + size
        f = list(create_contour(height, 100, size))
        m = list(line_max(f, m))
        for line in draw_contour(m):
            print draw_line(*line)
