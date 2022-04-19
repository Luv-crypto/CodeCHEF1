import os
from PIL import Image

SQUARE_FIT_SIZE = 1000
LOGO_FILENAME = "catlogo.png"

logoimage = Image.open(LOGO_FILENAME)
logowidth, logoheight = logoimage.size
os.makedirs("withLogo", exist_ok=True)

for filename in os.listdir("."):
    if (
        not (filename.endswith(".png") or filename.endswith(".jpeg"))
        or filename == LOGO_FILENAME
    ):

        continue
    im = Image.open(filename)
    width, height = im.size
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE

        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
    print(f"Resizing {filename}..")
    im = im.resize((width, height))
    print(f"adding logo to {filename}..")
    im.paste(logoimage, (width - logowidth, height - logoheight), logoimage)
    print(filename)
    im.save(os.path.join("withLogo", filename))
