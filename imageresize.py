import os, sys, glob
import Image

os.chdir("../DP/") #image folder path
THUMB_SIZE = 200, 200
for infile in glob.glob("*.jpg"):
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
    	    width, height = im.size
	    
	    if width > height:
   	        delta = width - height
		left = int(delta/2)
		upper = 0
		right = height + left
		lower = height 
	    else:
		delta = height - width
		left = 0
		upper = int(delta/2)
		right = width
		lower = width + upper

	    im = im.crop((left, upper, right, lower))
            im.thumbnail(THUMB_SIZE, Image.ANTIALIAS)
            im.save(outfile, "JPEG")
        except IOError:
            print "cannot create thumbnail for '%s'" % infile
