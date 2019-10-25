from PIL import Image, ImageDraw, ImageColor
from random import randint as rint
import numpy as np
import cv2

def blackscale_gradient():
    img = Image.new("RGB", (500,500), color="#FFFFFF")
    # img.show()
    draw = ImageDraw.Draw(img)

    r,g,b = 0, 0, 0
    dr = .5
    dg = .5
    db = .5
    for i in range(500):
        r,g,b = r+dr, g+dg, b+db
        draw.line((i,0,i,500), fill=(int(r),int(g),int(b)))
        
    img.putalpha(247)
    # img.save(name+".png", "PNG")
    img.show()

if __name__ == "__main__":
    """ for name in range(10):
        random_gradient(str(name)) """
    blackscale_gradient()