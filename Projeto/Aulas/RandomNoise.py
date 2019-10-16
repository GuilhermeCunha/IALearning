# from wand.image import Image

# cv2.imshow('image',im)
# im.show()
""" im = cv2.imread('IALearning/Projeto/Aulas/imagem.jpeg')# mudar path para funcionar
cv2.waitKey(0) """
from cv2 import cv2
import numpy
import random as rd
from PIL import Image
from PIL import ImageFilter as filter, ImageEnhance as enh
from PIL import ImageOps as ops

BG_COLOR = 209
BG_SIGMA = 5
MONOCHROME = 1

def add_noise(img, sigma=BG_SIGMA):
    """
    Adds noise to the existing image
    """
    width, height, ch = img.shape
    n = noise(width, height, sigma=sigma)
    img = img + n
    return img.clip(0, 255)


def noise(width, height, ratio=1, sigma=BG_SIGMA):
    """
    The function generates an image, filled with gaussian nose. If ratio parameter is specified,
    noise will be generated for a lesser image and then it will be upscaled to the original size.
    In that case noise will generate larger square patterns. To avoid multiple lines, the upscale
    uses interpolation.

    :param ratio: the size of generated noise "pixels"
    :param sigma: defines bounds of noise fluctuations
    """
    mean = 0
    assert width % ratio == 0, "Can't scale image with of size {} and ratio {}".format(width, ratio)
    assert height % ratio == 0, "Can't scale image with of size {} and ratio {}".format(height, ratio)

    h = int(height / ratio)
    w = int(width / ratio)

    result = numpy.random.normal(mean, sigma, (w, h, MONOCHROME))
    if ratio > 1:
        result = cv2.resize(result, dsize=(width, height), interpolation=cv2.INTER_LINEAR)
    return result.reshape((width, height, MONOCHROME))

def texture(image, sigma=BG_SIGMA, turbulence=2):
    """
    Consequently applies noise patterns to the original image from big to small.

    sigma: defines bounds of noise fluctuations
    turbulence: defines how quickly big patterns will be replaced with the small ones. The lower
    value - the more iterations will be performed during texture generation.
    """
    result = numpy.asarray(image) # image.astype(float)
    cols, rows, ch = result.shape
    ratio = cols
    while not ratio == 1:
        result += noise(cols, rows, ratio, sigma=sigma)
        ratio = (ratio // turbulence) or 1
    cut = numpy.clip(result, 0, 255)
    return cut.astype(numpy.uint8)


#Imagem original
img = Image.open('IALearning/Projeto/Aulas/imagem.jpeg')
width, height = img.size

leftrandom = width-rd.randint(0, width)
toprandom = height-rd.randint(0, height)
rightrandom = width-rd.randint(0, width-leftrandom)
bottonrandom = height-rd.randint(0, height-toprandom)

selection = (leftrandom, toprandom, rightrandom, bottonrandom)
part = img.crop(selection) # cria corte randômico da imagem original

# part = part.filter(filter.FIND_EDGES) # Mude os filtros padrões da classe ImageFilter aqui
# part = enh.Brightness(part).enhance(0.25) # Mude atributos da imagem como luminosidade aqui - ImageEnhance
part = add_noise(texture(part, sigma=4), sigma=10)
# part.show() # Mostrar parte cortada da imagem
cv2.waitKey(0)

# Mascara transparente para mudar formato do corte que contém o filtro
mask = Image.open('IALearning/Projeto/Aulas/mask_circle_01.png') 

# Colar parte modificada em cima da imagem original
img.paste(part, box=selection, mask=mask.resize(part.size))
img.show()
# cv2.imshow('image', part)
# cv2.waitKey(0)


""" m = numpy.asarray(part)
widthpart, heightpart = part.size
m2 = numpy.zeros((width, height, 3))

A = m.shape[0] / 3.0
w = 1.0 / m.shape[1]

shift = lambda x: A * numpy.sin(2.0*numpy.pi*x * w)

for i in range(m.shape[0]):
    # print(int(shift(i)))
    m2[:,i] = numpy.roll(m[:,i], int(shift(i)))

im2 = Image.fromarray(numpy.uint8(m2))
# im2.show()
# cv2.waitKey(0) """