from PIL import Image
import numpy as np


def draw(h, w):
    iar = []
    for y in range(h):
        irow = []
        for x in range(w):
            irow.append(get_pxl(x, y))
        iar.append(irow)
    return np.asarray(iar, dtype='uint8')


def get_pxl(x: int, y: int):
    #z3 = ((x**2) + (y**2)) % 256
    z = 0.56 * y % (0.06 * x + 1) % 256
    return [z, z, z]


img = Image.fromarray(draw(2160, 4096))
img.save('10_4k2.png')

