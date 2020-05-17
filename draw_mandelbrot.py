from PIL import Image
from numba import jit
import numpy as np


@jit
def mandel(x, y, max_iters):
    """
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a fixed number of iterations.
    """
    c = complex(x,y)
    z = 0j
    for i in range(max_iters):
        z = z*z + c
        if z.real * z.real + z.imag * z.imag > 4:
            return i

    return 0

@jit(nopython=True)
def create_fractal(min_x, max_x, min_y, max_y, width, height, iters):
    #image = np.empty((width,height))
    image = []
    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height
    for x in range(width):
        real = min_x + x * pixel_size_x
        row = []
        for y in range(height):
            imag = min_y + y * pixel_size_y
            color = int(mandel(real, imag, iters))
            #image[y, x] = color
            row.append(color)
        image.append(row)

    return image

img = create_fractal(-0.74877,-0.74872,0.06505,0.06510, 1024, 2048, 2048)

#img = create_fractal(-0.74877, -0.74872, 0.06505, 0.065, 1024, 1024, 2048)
#img = create_fractal(-0.7778078101931726, -0.7778078101931695, 0.1316451080032044, 0.1316451080032076, 1024, 1024, 2048)
img = np.asarray(img, dtype='uint8')
Image.fromarray(img).save('fractal_custom.png')

