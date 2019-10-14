from PIL import ImageFilter as filter
from PIL import Image as img

imagem = img.open("IALearning/Projeto/Aulas/digitalizacao.png")

blur = imagem.filter(filter.SMOOTH_MORE)

img._show(blur)