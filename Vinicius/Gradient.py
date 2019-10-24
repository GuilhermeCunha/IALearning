from PIL import Image, ImageDraw
from random import randint as rint
import cv2

def random_gradient():
    img = Image.new("RGB", (500,500), "#FFFFFF")
    # img.show()
    draw = ImageDraw.Draw(img)

    r,g,b = 0, 0, 0
    dr = .5
    dg = .5
    db = .5
    for i in range(500):
        r,g,b = r+dr, g+dg, b+db
        draw.line((i,0,i,500), fill=(int(r),int(g),int(b)))

    # img.save(name+".png", "PNG")
    img.show()

if __name__ == "__main__":
    """ for name in range(10):
        random_gradient(str(name)) """
    random_gradient()