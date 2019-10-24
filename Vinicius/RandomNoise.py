from cv2 import cv2
import random as rd
from PIL import Image, ImageDraw
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

def blackscale_gradient():
    img = Image.new("RGB", (1000, 750), "#FFFFFF")
    # img.show()
    draw = ImageDraw.Draw(img)

    r,g,b = 0, 0, 0
    gradient = 0.255
    for i in range(1000):
        r,g,b = r+gradient, g+gradient, b+gradient
        draw.line((i,0,i,750), fill=(int(r),int(g),int(b)))
    # img.save(name+".png", "PNG")
    # img.show()
    return img
    
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

# part = part.filter(filter.FIND_EDGES) # Mude os filtros padrões da classe ImageFilter aqui
# part = flashOrShadow(part)
# part.show() # Mostrar parte cortada da imagem
# cv2.waitKey(0)

# Máscara transparente para mudar formato do corte que contém o filtro
mask = Image.open('IALearning/Vinicius/mask_gradient.png') 

try:
    # Colar parte modificada em cima da imagem original no exato local que o corte foi tirado
    # img.paste(part, box=selection, mask=mask.resize(part.size))
    img = img.alpha_composite(img, blackscale_gradient())
except Exception as e:
    print("Part size: {0}\nSelection: {1}\nMask size: {2}\nMessage: {3}".format(part.size, selection, mask.size, str(e)))
else:
    img.show()
# cv2.imshow('image', part)
# cv2.waitKey(0)