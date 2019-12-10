import numpy as np
from matplotlib import pyplot as plt


def find_smallest_layer():
    with open("data8.txt") as in_data:
        image = np.array([int(x) for x in in_data.read().strip()], dtype=np.uint8)
        layers = image.shape[0] // (25 * 6)
        image = image.reshape((layers, 6, 25))
        fewest_zeros = 151
        a_times_b = 0

        for i in range(layers):
            histo = np.histogram(image[i], bins=[0, 1, 2, 3])[0]
            print(histo)
            if histo[0] < fewest_zeros:
                fewest_zeros = histo[0]
                a_times_b = histo[1] * histo[2]

        print(a_times_b)

        final_image = np.zeros(image.shape[1:], dtype=np.uint8)
        for y in range(final_image.shape[0]):
            for x in range(final_image.shape[1]):
                for i in range(layers):
                    if image[i, y, x] != 2:
                        final_image[y, x] = image[i, y, x]
                        break
        plt.imshow(final_image)
        plt.show()


if __name__ == "__main__":
    find_smallest_layer()
