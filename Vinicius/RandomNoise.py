from cv2 import cv2
import random as rd
from PIL import Image
from PIL import ImageFilter as filter, ImageEnhance as enh

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
leftrandom = rd.randint(0, width-1)
toprandom = rd.randint(0, height-1)
rightrandom = rd.randint(leftrandom, width)
bottomrandom = rd.randint(toprandom, height)

selection = (leftrandom, toprandom, rightrandom, bottomrandom)
part = img.crop(selection) # cria corte randômico da imagem original

# part = part.filter(filter.FIND_EDGES) # Mude os filtros padrões da classe ImageFilter aqui
part = enh.Brightness(part).enhance(1000) # Mude atributos da imagem como luminosidade aqui - ImageEnhance
# part.show() # Mostrar parte cortada da imagem
# cv2.waitKey(0)

# Máscara transparente para mudar formato do corte que contém o filtro
mask = Image.open('IALearning/Vinicius/mask_gradient.png') 

# Colar parte modificada em cima da imagem original no exato local que o corte foi tirado
img.paste(part, box=selection, mask=mask.resize(part.size))
img.show()
# cv2.imshow('image', part)
# cv2.waitKey(0)