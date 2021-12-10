from math import sqrt

import numpy as np
from PIL import Image


def load_image(filepath: str) -> Image:
    return Image.open(filepath).convert("L")


def grad_inf(ims: Image) -> Image:
    pixs = np.asarray(ims).astype("uint8")
    pixd = pixs.copy()
    height, width = pixs.shape

    for j in range(1, height-1):
        for i in range(1, width-1):
            acc = max(abs(int(pixs[j-1, i]) - int(pixs[j, i])), abs(int(pixs[j+1, i]) - int(pixs[j, i])), abs(
                int(pixs[j, i-1]) - int(pixs[j, i])), abs(int(pixs[j, i+1]) - int(pixs[j, i])))
            pixd[j, i] = acc
    return Image.fromarray(pixd)


def grad_plus_inf(ims: Image) -> Image:
    pixs = np.asarray(ims).astype("uint8")
    pixd = pixs.copy()
    height, width = pixs.shape

    for j in range(1, height-1):
        for i in range(1, width-1):
            pixd[j, i] = max(int(pixs[j-1, i]) - int(pixs[j, i]), int(pixs[j+1, i]) - int(pixs[j, i]), int(pixs[j, i-1]) - int(pixs[j, i]), int(pixs[j, i+1]) - int(pixs[j, i]), 0)
    return Image.fromarray(pixd)


def grad_minus_inf(ims: Image) -> Image:
    pixs = np.asarray(ims).astype("uint8")
    pixd = pixs.copy()
    height, width = pixs.shape

    for j in range(1, height-1):
        for i in range(1, width-1):
            pixd[j, i] = max(int(pixs[j, i]) - int(pixs[j-1, i]), int(pixs[j, i]) - int(pixs[j+1, i]), int(pixs[j, i]) - int(pixs[j, i-1]), int(pixs[j, i]) - int(pixs[j, i+1]), 0)
    return Image.fromarray(pixd)


def dilation(ims: Image, n: int) -> Image:
    pixs = np.asarray(ims).astype("uint8")
    pixd = pixs.copy()
    height, width = pixs.shape

    for _ in range(n):
        tmp = pixd.copy()
        for j in range(1, height-1):
            for i in range(1, width-1):
                tmp[j, i] = max(pixd[j-1, i], pixd[j+1, i],
                                pixd[j, i-1], pixd[j, i+1], pixd[j, i])
        pixd = tmp
    return Image.fromarray(pixd)


def erosion(ims: Image, n: int) -> Image:
    pixs = np.asarray(ims).astype("uint8")
    pixd = pixs.copy()
    height, width = pixs.shape

    for _ in range(n):
        tmp = pixd.copy()
        for j in range(1, height-1):
            for i in range(1, width-1):
                tmp[j, i] = min(pixd[j-1, i], pixd[j+1, i],
                                pixd[j, i-1], pixd[j, i+1], pixd[j, i])
        pixd = tmp
    return Image.fromarray(pixd)


if __name__ == "__main__":
    image = load_image("image.jpg")

    image_contours = grad_inf(image)
    image_contours.show("Contours image test")
    image_contours.save("image_grad.png")
    image_contours_plus = grad_plus_inf(image)
    image_contours_plus.show("Contours image test")
    image_contours_plus.save("image_grad_plus.png")
    image_contours_minus = grad_minus_inf(image)
    image_contours_minus.show("Contours image test")
    image_contours_minus.save("image_grad_minus.png")

    dilated_image = dilation(image, 10)
    dilated_image.show("Dilation image test")
    image_contours.save("dilated_image.png")

    eroded_image = erosion(image, 10)
    eroded_image.show("Erosion image test")
    image_contours.save("eroded_image.png")
