import numpy  , cv2 
# opening the image
image = cv2.imread("image.jpg")
#converting image to grayscale for my algo to work 
bwImage = cv2.cvtColor( image , cv2.COLOR_RGB2GRAY )

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\\\"^`\". "

# reducing number of colors in image according to number of available characters
rImage =  bwImage // 4  

#freeing up some memory
del(bwImage) 
del(image) 

nImage = []
ncol = ""
for r in rImage :
    for col in r :
        ncol += chars[col]
        ncol += chars[col]
    nImage.append(ncol)
    ncol = ""

f = open("output.txt" , "w" )

for l in nImage :
    f.write(l)
    f.write("\n")

f.close()



