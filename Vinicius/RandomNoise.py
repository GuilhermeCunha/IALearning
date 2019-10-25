from cv2 import cv2
import random as rd
from PIL import Image, ImageDraw
import numpy as np
from PIL import ImageFilter as filter, ImageEnhance as enh

def flashOrShadow(img, gamma = 1000):
    """
    Função usada para atribuir luminosidade ou sombra a
    uma máscara para simular o flash de um celular ou uma sombra.\n
    Para simular o flash apenas passe uma imagem como parâmetro,
    o valor de gamma padrão é 1000.\n
    Para simular uma sombra passe ambos parâmetros; os melhores 
    valores de gamma para sombras são entre 0.1 e 1.\n
    Veja :meth:`~PIL.ImageEnhance.Brightness` e \n
    `https://hhsprings.bitbucket.io/docs/programming/examples/python/PIL/ImageEnhance.html#class-brightness`
    """
    return enh.Brightness(img).enhance(gamma) 

#Imagem original
img = Image.open('IALearning/Vinicius/imagem.jpeg') # Mude aqui o path da imagem
width, height = img.size

''' 
inicio randômico de tamanhos do corte que servirá de efeito
para posteriormente colar na imagem original. Os tamanhos
são iniciados de forma a não existir sobreposição de lados, 
impedindo a geração de uma exceção. O tamanho máximo do corte
é o tamanho da imagem e o tamanho mínimo é 1x1 px². O left tem
que ser menor que o right e o top tem que ser menor que o bottom
para que não exista exceção.
'''
leftrandom = rd.randint(0, width-2)
toprandom = rd.randint(0, height-2)
rightrandom = rd.randint(leftrandom + 1, width)
bottomrandom = rd.randint(toprandom + 1, height)

selection = (leftrandom, toprandom, rightrandom, bottomrandom)
part = img.crop(selection) # cria corte randômico da imagem original

part = part.filter(filter.GaussianBlur(radius=10)) # Mude os filtros padrões da classe ImageFilter aqui
part = part.filter(filter.MedianFilter(size=9))
part = flashOrShadow(part)
# part.show() # Mostrar parte cortada da imagem
# cv2.waitKey(0)

# rodar imagem original
rotation = rd.randint(-45, 45)
img = img.rotate(rotation, expand=True) 

# Máscara transparente para mudar formato do corte que contém o filtro
mask = Image.open('IALearning/Vinicius/mask_gradient.png') 

try:
    # Colar parte modificada em cima da imagem rotacionada no exato local que o corte foi tirado
    img.paste(part, selection, mask=mask.resize(part.size))
    # Rotacionar a imagem de volta para a posição original
    img = img.rotate(-(rotation)) 
except Exception as e:
    print("Part size: {0}\nSelection: {1}\nMask size: {2}\nMessage: {3}".format(part.size, selection, mask.size, str(e)))
else:
    img.show()
# cv2.imshow('image', part)
# cv2.waitKey(0)