from PIL import Image
import numpy as np

## Function that converts a pixel value into a corresponding ASCII character
def ascii_chars(pixel, ascii_char):
    num_char = len(ascii_char)
    char = 256 // num_char  # Defines the brightness range for each character
    ascii_character = ascii_char[min(pixel // char, num_char - 1)]
    return ascii_character


ascii_char = '@#8&M0oahwbdqCXnvxjft()1[]-+<>;^{}|!?*%$'  # Set of characters for conversion


## Open an image, convert it to grayscale ('L' mode), and resize it
im_cl = Image.open("Robot.jpeg")  # Open the image
size = (120, 160)  # Define the thumbnail size
im_cl.thumbnail(size)  # Resize while maintaining the aspect ratio

im_bw = im_cl.convert('L')  # Convert to grayscale
im_bw.save("Robot_bw.jpeg")  # Save the converted image


## Convert the image into a NumPy array
data_im = np.asarray(im_bw)


## Iterate through each pixel and generate ASCII art
ascii_art = ''
for row in data_im:
    for pixel in row:
        ascii_art += ascii_chars(pixel, ascii_char)  # Convert each pixel to an ASCII character
    ascii_art += '\n'  # Add a new line at the end of each row

with open('ascii_art.txt', 'w') as f:
    f.write(ascii_art)
