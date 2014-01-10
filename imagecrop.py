from PIL import Image, ImageChops

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

im = Image.open("img1.jpg")
#For trimming the image, call this function.
#im = trim(im)
im = im.convert("RGBA")

pixels = im.load() 
# Loop from left to right for better replacement of pixels. 
for i in range(im.size[1]):    # for every pixel from left to right
    for j in range(im.size[0]):
    	if pixels[j,i] <= (255,255,255,255) and pixels[j,i] >= (245,245,245,245) :  # Check for grey shade in white. 
    		pixels[j,i] = (0,0,0,0) # Put any backgroud color which matches your site theme.
    	else:
    		break
for i in reversed(range(im.size[1])):    # for every pixel from right to left
    for j in reversed(range(im.size[0])):
    	if pixels[j,i] <= (255,255,255,255) and pixels[j,i] >= (245,245,245,245) : 
    		pixels[j,i] = (0,0,0,0) 
    	else:
    		break
    		
# im.save("img2.png","PNG") # For storing transperant image in png format 
im.save("img2.jpg", "JPEG")

