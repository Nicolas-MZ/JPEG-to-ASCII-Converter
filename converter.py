from PIL import Image


## Open an image and convert it to grayscale using the 'L' mode

im_cl = Image.open("evildog.jpg")
im_bw = im_cl.convert('L')
im_bw.save("evildog_bw.png")

