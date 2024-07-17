from PIL import Image
import numpy as np

im = Image.open(input("Enter image name: "))

pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width : (i + 1) * width] for i in range(height)]

bin_conv_list = []

for i in range(len(pixels)):
    for j in range(len(pixels[i])):
        if pixels[i][j][0] % 2 == 0:
            bin_conv_list.append(0)
        else:
            bin_conv_list.append(1)

# print(bin_conv_list)

pixel_group = []
pixel_img = []

for i in range(len(bin_conv_list)):
    pixel_group.append(bin_conv_list[i])
    if (i + 1) % 8 == 0:
        pixel_img.append(pixel_group)
        pixel_group = []


# print(pixel_img[0])
# print(bin_conv_list[:10])

# print(pixel_img)
output = []
for batch in pixel_img:
    b = "".join([str(e) for e in batch])
    d = int(b, base=2)
    output.append(chr(d))

print(output[:100])
