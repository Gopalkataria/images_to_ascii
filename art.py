import numpy
import cv2
# opening the image
image = cv2.imread("image.jpg")
# converting image to grayscale for my algo to work
bwImage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# chars = "$@B%8&WM#*oahkbwmZO0QLJDEXznxrjft/\|()1{}[]?-_+~i!lI;:,\\\"^`\". "
# chars = "$@B%89WM#*oaihkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\\\"^`\".-_"
chars = "@L>*+=-_^`"

# reducing number of colors in image according to number of available characters
rImage = bwImage // 26
# rImage = bwImage // 3.6


# freeing up some memory
del(bwImage)
del(image)

nImage = []
ncol = ""
for row in rImage:
    for col in row:
        ncol += chars[int(col)]
        ncol += chars[int(col)]
    nImage.append(ncol)
    ncol = ""

f = open("output.html", "w")

height = len(nImage) * 20

width = len(nImage[0]) * 10


y = 20

f.write("""<html>
<title>ASCII image </title>
<body><pre>
""".format(height, width))
for line in nImage:
    f.write("\"")
    # f.write("< x=\"0\" y=\"{}\" fill=\"black\">\"".format(y))
    # y += 20
    f.write(line)
    # f.write("\"</text>")
    f.write("\"")
    f.write("\n")

f.write("</pre></body></html>")

f.close()


f = open("output.txt", "w")

for l in nImage:
    f.write(l)
    f.write("\n")

f.close()
