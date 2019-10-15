import cv2
import numpy

im = cv2.imread('image.png')# mudar path para funcionar
cv2.imshow('image',im)
# cv2.waitKey(0)

m = numpy.asarray(im)
m2 = numpy.zeros((im.size[0],im.size[1], 3))
width = im.size[0]
height = im.size[1]

A = m.shape[0] / 3.0
w = 1.0 / m.shape[1]

shift = lambda x: A * numpy.sin(2.0*numpy.pi*x * w)

for i in range(m.shape[0]):
    print(int(shift(i)))
    m2[:,i] = numpy.roll(m[:,i], int(shift(i)))

im2 = Image.fromarray(numpy.uint8(m2))
im2.show()
cv2.waitKey(0)