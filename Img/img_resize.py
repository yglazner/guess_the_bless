import os
from PIL import Image
size = 128, 128

files_list = os.listdir()
for file in files_list:
    if file.endswith(".jpg") or file.endswith(".png"):
        try:
            outfile = file
            im = Image.open(file)
            im.thumbnail(size, Image.ANTIALIAS)
            if file.endswith(".jpg"):
                im.save(outfile, "JPEG")
            if file.endswith(".png"):
                im.save(outfile, "PNG")
        except IOError:
            print ("cannot create thumbnail for '%s'" % file)


