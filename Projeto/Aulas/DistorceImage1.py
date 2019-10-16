# from wand.image import Image

# cv2.imshow('image',im)
# im.show()
""" im = cv2.imread('IALearning/Projeto/Aulas/imagem.jpeg')# mudar path para funcionar
cv2.waitKey(0) """
from cv2 import cv2
import numpy
import random as rd
from PIL import Image
from PIL import ImageFilter as filter

img = Image.open('IALearning/Projeto/Aulas/imagem.jpeg')
width, height = img.size

leftrandom = width-rd.randint(0, width)
toprandom = height-rd.randint(0, height)
rightrandom = width-rd.randint(0, width-leftrandom)
bottonrandom = height-rd.randint(0, height-toprandom)

selection = (leftrandom, toprandom, rightrandom, bottonrandom)
part = img.crop(selection)
part = part.filter(filter.FIND_EDGES) # Mude o filtro aqui
# part.show()
cv2.waitKey(0)

img.paste(part, box=selection)
img.show()
# cv2.imshow('image', part)
# cv2.waitKey(0)


""" m = numpy.asarray(im)
width = im.shape[0]
height = im.shape[1]
m2 = numpy.zeros((width,height, 3))

A = m.shape[0] / 3.0
w = 1.0 / m.shape[1]

shift = lambda x: A * numpy.sin(2.0*numpy.pi*x * w)

for i in range(m.shape[0]):
    print(int(shift(i)))
    m2[:,i] = numpy.roll(m[:,i], int(shift(i)))

im2 = Image.fromarray(numpy.uint8(m2))
im2.show()
cv2.waitKey(0) """