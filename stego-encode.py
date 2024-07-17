from PIL import Image
import numpy as np


im = Image.open(input("Enter image name: "))
pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width : (i + 1) * width] for i in range(height)]

# print(pixels[0][0][1])

message = input("Enter your message: ")

bin_conv = []

print(len(pixels), len(pixels[0]), len(pixels[0][0]))

for s in message:
    ascii_val = ord(s)
    binary_val = bin(ascii_val)
    # print(binary_val[2:])
    bin_conv.append("0" * (8 - len(binary_val[2:])) + binary_val[2:])
    print(bin_conv[-1])


bin_conv_list = []

for i in range(len(bin_conv)):
    for s in bin_conv[i]:
        bin_conv_list.append(int(s))

k = 0

for i in range(len(pixels)):
    for j in range(len(pixels[0])):
        if k >= len(bin_conv_list):
            continue
        pixel_num = pixels[i][j][0]
        if bin_conv_list[k] == 0:
            pixel_num = pixel_num & 0
        else:
            pixel_num = pixel_num | 1

        k += 1
        pixels[i][j] = (pixel_num, pixels[i][j][1], pixels[i][j][2])

print(np.array(pixels).shape)
img = Image.fromarray(np.array(pixels).astype(np.uint8), "RGB")
img.save("output.png")
