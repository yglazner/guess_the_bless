import os, sys
from PIL import Image



size = 128, 128

files = os.listdir(os.getcwd())

for f in files:
    if f.endswith("jpg") or f.endswith("png"):
        im = Image.open(f)
        im.thumbnail(size, Image.ANTIALIAS)
        if f.endswith("jpg"):
            im.save(f, "JPEG")
        if f.endswith("png"):
            im.save(f, "PNG")
        
