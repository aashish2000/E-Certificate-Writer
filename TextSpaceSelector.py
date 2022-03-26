from tkinter import *
from PIL import Image, ImageTk
import os

def spaceSelector(template):
    root = Tk()
    root.title('Image')
    
    # Adding the image
    File = template
    canvas = Canvas(root)
    img = ImageTk.PhotoImage(Image.open(File), master = canvas)
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    def printcoords(event):
        
    	# Get mouseclick coordinates
        x,y = event.x, event.y

        # Write to temp file
        temp_file = open("coords.txt","w")
        temp_file.write('{} {}'.format(x,y))
        temp_file.close()

        root.destroy()
        root.quit()

    # Mouseclick event
    panel.bind("<Button 1>", printcoords)
    root.mainloop()
    
    # Get coordinates from temp file
    temp_file=open('coords.txt','r')
    xcoor,ycoor=map(int, temp_file.read().strip().split())
    temp_file.close(); os.remove('./coords.txt')
    return (xcoor,ycoor)