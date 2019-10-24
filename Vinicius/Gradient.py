from PIL import Image, ImageDraw
from random import randint as rint
import numpy as np
import cv2

def blackscale_gradient():
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
        
    graddata = np.ndarray((64, 64))
    img2 = Image.new("L", (64, 64))  # single band
    for i in range(64):
        graddata[:, i] = i * 4
    img2.putdata(graddata.flatten())
    # img.save(name+".png", "PNG")
    img2.show()

if __name__ == "__main__":
    """ for name in range(10):
        random_gradient(str(name)) """
    blackscale_gradient()