from PIL import Image

myimage = Image.open("image.jpeg")
myimagecopy = myimage.copy()

croppedIm = myimage.crop((211, 201, 620, 620))
myimagecopy.paste(myimage, (200, 220))
myimagecopy.save("pasted.jpeg")

myimagewidth, myimageheight = myimage.size
croppedImwidth, croppedImheight = croppedIm.size

myimagetwo = myimage.copy()
for left in range(0, myimagewidth, croppedImwidth):
    for top in range(0, myimageheight, croppedImheight):
        print(left, top)
        myimagetwo.paste(croppedIm, (left, top))

myimagetwo.save("allinone.jpeg")
