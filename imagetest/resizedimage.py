from PIL import Image

itsimage = Image.open("ideation.jpeg")

width, height = itsimage.size
weirdimage = itsimage.resize((width, height + 300))
weirdimage.save("weird.jpeg")

itsimage.rotate(25).save("rotated25.jpeg")
itsimage.rotate(25, expand=True).save("rotated25_expanded.jpeg")

itsimage.transpose(Image.FLIP_LEFT_RIGHT).save("horizontal_flip.jpeg")
itsimage.transpose(Image.FLIP_TOP_BOTTOM).save("vertical_flip.jpeg")