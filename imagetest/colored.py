from PIL import Image

im = Image.new("RGBA", (100, 100))
for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (256, 0, 0))

for x in range(100):
    for y in range(50, 100):
        im.putpixel((x, y), (0, 0, 256))

im.save("doublecolored.png")
