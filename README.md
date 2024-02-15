## images_to_ascii

### converting images to ascii for some random fun. 
### works by first making the image grayscale, and finding a corresponding character for each pixel.

<br/>

output in html and txt format 

<br/>

just climb into this directory and 
<br/> <code> ./art.py < image-name > < file-name > < (optional) characters > </code> <br/>

image-name = name of the input image , recommended size beloxe 400x400 pixels, but any png or jpg will do 
<br/>
file-name = output file name without extension, automatically a proper html and txt file will be generated 
<br/>
characters = a string with characters, eg "$%^&- " to use in ascii art. order can be random, but characters will be assigned in order of descending level of darkness, so first characters replace dark colors, with the last ones replace the lighter ones. 

<br/> characters can be omitted, in that case a built in one will be used
<br/>
### Its just a fun project and I have no intentions to maintain it, so don't create pull requests. feel free to fork it and make it your own 
<br/>


