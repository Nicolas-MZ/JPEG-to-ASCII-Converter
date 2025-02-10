from PIL import Image
import numpy as np

class ImageConsi:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.image = Image.open(name)
    def resize(self):
        self.image.thumbnail(self.size)
    def convert_grayscale(self):
        return self.image.convert('L')
    def auto_convert(self):
        self.resize()
        image = self.convert_grayscale()
        return image
    

class ConvertMatriz:
    def __init__(self, image):
        self.image = image
    def convert_array(self):
        matriz = np.asarray(self.image)
        return matriz
    

def ascii_chars(pixel, ascii_char):
    num_char = len(ascii_char)
    char = 256 // num_char
    ascii_character = ascii_char[min(pixel // char, num_char - 1)]
    return ascii_character


ascii_char = '@#8&M0oahwbdqCXnvxjft()1[]-+<>;^{}|!?*%$'

print('-' * 30)
print("   JPEG-TO-ASCII-CONVERTER")
print('-'* 30)

name_image = str(input("Digite o nome do arquivo (sem a extensão .jpeg): "))
name_image = f'{name_image}.jpeg'

size = (120,160)
image = ImageConsi(name_image, size)
image_bw = image.auto_convert()

if image_bw:
    convert_matriz = ConvertMatriz(image_bw)
    data_im = convert_matriz.convert_array()
    
    if data_im is not None: 
        ascii_art = ''
        for row in data_im:
            for pixel in row:
                ascii_art += ascii_chars(pixel, ascii_char)
            ascii_art += '\n'

        with open('ascii_art.txt', 'w') as ascii:
            ascii.write(ascii_art)
        print("Conversão bem-sucedida!!")

else:
    print("Houve algum problema na execução, por favor tente novamente.")

