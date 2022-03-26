from PIL import Image, ImageDraw, ImageFont
import img2pdf
import os

def writeImage(template,font,size,coorx,coory,msg,rgb,directory,coorximg,cooryimg,img_directory,imgParticipantCheck,sno):
	image = Image.open(template)
	if (imgParticipantCheck):
		try:
			img_p = Image.open(img_directory+'/'+str(sno)+'-'+msg+".png")
		except:
			img_p = Image.open(img_directory+'/'+str(sno)+'-'+msg+".jpg")

		participant_img = img_p.copy()
		participant_img.thumbnail((100,100)) # Resizing participant image
		coorximg -= 50
		cooryimg -= 50

	# Initialise the drawing context with the image object as background
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype(font, size=size)
	
	# Starting position of the message
	width, ht = font.getsize(msg)[0], font.getsize(msg)[1]
	(x, y) = (coorx-(width/2), coory-(ht/2))
	message = msg # Name
	color = rgb # Colour
	
	# Draw the message on the background
	draw.text((x, y), message, fill=color, font=font)

	if (imgParticipantCheck):
		image.paste(participant_img, (coorximg, cooryimg))

	# Save the edited image
	if image.mode == "RGBA":
		image = image.convert("RGB")
	image.save(directory+'/'+str(sno)+'-'+msg+".png")
	
	# Save as pdf
	with open(directory+'/'+str(sno)+'-'+msg+".pdf","wb") as f:
		f.write(img2pdf.convert(directory+'/'+str(sno)+'-'+msg+".png"))

	# Remove existing pictures
	os.remove(directory+'/'+str(sno)+'-'+msg+".png")
	image.close()
	f.close() 