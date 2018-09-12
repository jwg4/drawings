from random import uniform

PI = 3.14159


class Cartesian(object):
    def __init__(self, *args, **kwargs):
        pass


class Cylindrical(object):
    def __init__(self, *args, **kwargs):
        pass


EYE_POINT = Cartesian(0, 0, 1)

SCOPE_1 = PI / 4.0
SCOPE_2 = 0.5

PICTURE_CYLINDER = [
    Cylindrical(r=1, theta=SCOPE_1, z=-SCOPE_2),
    Cylindrical(r=1, theta=SCOPE_1, z=0),
    Cylindrical(r=1, theta=0, z=0),
]


def project_rectangle(r, theta, width, height):
    pj_base = (theta, 0 - 1.0/r)
    pj_height = height / r
    pj_width = width / r

    return (
        (pj_base[0] - pj_width / 2.0, pj_base[1]),
        (pj_base[0] + pj_width / 2.0, pj_base[1] + pj_height)
    )


def generate_rectangles(n, r1, r2, theta1, theta2):
    MEAN_WIDTH = 0.4
    MEAN_HEIGHT = 0.6

    for i in range(0, n+1):
        r = r1 + i * ((r2 - r1) / (n-1))
        theta = uniform(theta1, theta2)
        width = uniform(MEAN_WIDTH * 0.5, MEAN_WIDTH * 1.5)
        height = uniform(MEAN_HEIGHT * 0.5, MEAN_HEIGHT * 1.5)
        yield (r, theta, width, height)


if __name__ == '__main__':
    N = 2
    for rect in generate_rectangles(N, 5, 10, 0, SCOPE_1):
        projection = project_rectangle(*rect)
        print(projection)
