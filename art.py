#!/usr/bin/python3

from cv2 import imread, cvtColor, COLOR_RGB2GRAY
from sys import argv


def write_html(nImage, fname ):
    f = open( fname + ".html", "w")

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


def write_txt(nImage , fname ):

    f = open( fname + ".txt", "w")

    for l in nImage:
        f.write(l)
        f.write("\n")

    f.close()


def convert_ascii(name, chars_given , fname ):
    # opening the image
    image = imread(name)
    # converting image to grayscale for my algo to work
    bwImage = cvtColor(image, COLOR_RGB2GRAY)

    # other character lists for fun to try out
    #chars = "$@B%8&WM#*oahkbwmZO0QLJDEXznxrjft/\|()1{}[]?-_+~i!lI;:,\\\"^`\". "
    #chars = "$@B%89WM#*oaihkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\\\"^`\".-_"
    #chars = "@L>*+=-_^`"
    chars = "@>#*+=-:. "
    #chars = "!@#$%^&*()#- {}:';?><.,|`~" 
    #chars = " .:-=+*#>"
    #chars = "#C=A_T.S "
    
    if ( chars_given ) :
            chars = chars_given 

    # reducing number of colors in image according to number of available characters
    rImage = bwImage // (int( 255 / len(chars)) + 1 )

    # freeing up some memory
    del(bwImage)
    del(image)

    # a new array which gonna store all the ascii chars
    nImage = []
    ncol = ""
    for row in rImage:
        for col in row:
            ncol += chars[int(col)]
            ncol += chars[int(col)]
        nImage.append(ncol)
        ncol = ""

    write_txt(nImage , fname )
    write_html(nImage, fname )


if __name__ == "__main__":
    if ( len(argv) >= 4  ) :
        convert_ascii(argv[1], argv[3], argv[2])
    else :
        convert_ascii(argv[1] , ""  , argv[2] ) 

