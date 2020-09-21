# https://www.freecodecamp.org/news/how-to-build-an-image-type-convertor-in-six-lines-of-python-d63c3c33d1db/

from PIL import Image
import sys
file = sys.argv[1]
img = Image.open(file)
rgb_img = img.convert('RGB')
rgb_img.save(file.replace("png", "jpg"), quality=95)
