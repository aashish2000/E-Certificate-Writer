from PIL import Image, ImageDraw, ImageFont
import img2pdf
import os
# create Image object with the input image

def writeimage(template,font,size,coorx,coory,msg,rgb):
	image = Image.open(template)

	# initialise the drawing context with
	# the image object as background

	draw = ImageDraw.Draw(image)

	font = ImageFont.truetype(font, size=size)
	 
	# starting position of the message
	 
	(x, y) = (coorx, coory)
	message = msg
	color = rgb # black color
	 
	# draw the message on the background

	draw.text((x, y), message, fill=color, font=font)

	# save the edited image

	if image.mode == "RGBA":
		image = image.convert("RGB")

	image.save("./Output/"+msg+".png")


	with open("./Output/"+msg+".pdf","wb") as f:
		f.write(img2pdf.convert("./Output/"+msg+".png"))
	
	os.remove("./Output/"+msg+".png")

	image.close()

	f.close() 