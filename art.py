import numpy  , cv2 
# opening the image
image = cv2.imread("image.jpg")
#converting image to grayscale for my algo to work 
bwImage = cv2.cvtColor( image , cv2.COLOR_RGB2GRAY )

#chars = "$@B%8&WM#*oahkbwmZO0QLJDEXznxrjft/\|()1{}[]?-_+~i!lI;:,\\\"^`\". "
chars = "$@B%8&WM#*oaihkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\\\"^`\".  "
#chars  = "$@ZLIhlai{}\-:. "

# reducing number of colors in image according to number of available characters
rImage =  bwImage // 3.6


#freeing up some memory
del(bwImage) 
del(image) 

nImage = []
ncol = ""
for r in rImage :
    for col in r :
        ncol += chars[int(col) ]
        ncol += chars[int(col)]
    nImage.append(ncol)
    ncol = ""

f = open("output.txt" , "w" )

for l in nImage :
    f.write(l)
    f.write("\n")

f.close()



