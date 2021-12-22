from bitarray import bitarray
from bitarray.util import ba2int
import numpy as np


def get_enh(line):
    return bitarray(''.join([('0' if c == '.' else '1') for c in line]))


def get_image(lines):
    return np.array([[(0 if c == '.' else 1) for c in l.strip()] for l in lines])


def print_image(image):
    num_rows, num_cols = image.shape
    for j in range(0, num_rows):
        print(''.join(['.' if image[j][i] == 0 else '#' for i in range(0, num_cols)]))


def get_relevant_pixel(coord, image):
    num_rows, num_cols = image.shape
    x, y = coord
    value = ''
    for j in [y - 1, y, y + 1]:
        for i in [x - 1, x, x + 1]:
            value += str(int(image[0][0])) if i < 0 or i >= num_cols or j < 0 or j >= num_rows else str(
                int(image[j][i]))
    return bitarray(value)


lines = open("input.txt", "r").readlines()

enh = get_enh(lines[0].strip())
print(enh)

image = get_image(lines[2:])
num_rows, num_cols = image.shape

nb_step = 50
image = np.vstack((np.zeros((2 * nb_step + 2, num_cols)), image))
image = np.vstack((image, np.zeros((2 * nb_step + 2, num_cols))))
image = np.hstack((np.zeros((num_rows + 4 * nb_step + 4, 2 * nb_step + 2)), image))
image = np.hstack((image, np.zeros((num_rows + 4 * nb_step + 4, 2 * nb_step + 2))))

num_rows, num_cols = image.shape
for s in range(0, nb_step):
    print('step ' + str(s))
    tmp_image = np.zeros(image.shape)
    for i in range(0, num_cols):
        for j in range(0, num_rows):
            tmp_image[j][i] = enh[ba2int(get_relevant_pixel((i, j), image))]
    image = tmp_image

print_image(image)
print(np.sum(image))
