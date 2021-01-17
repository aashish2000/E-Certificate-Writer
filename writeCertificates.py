# Required imports
from pandas import read_csv
import os
import tkinter as tk
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import showinfo, askquestion
from tkinter.colorchooser import askcolor
from ImgUtil import writeImage
from TextSpaceSelector import spaceSelector

# Utility function to collect column name and font size

def inputColumnAndSize():

	# Create tk window and config
	master = tk.Tk()
	master.title('Column name and font size')

	fontStyle = tkFont.Font(family="Lucida Grande", size=22)
	tk.Label(master, text="Enter column name containing names of participants: ", font=fontStyle).grid(row=0)
	tk.Label(master, text="Font size of text: ", font=fontStyle).grid(row=1)

	e1 = tk.Entry(master)
	e2 = tk.Entry(master)

	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)

	col, size= None, None

	def colSize():
		
		# Get info from button
		column, sizeImg = e1.get(), e2.get()

		temp_file = open("colsize.txt","w")
		temp_file.write('{} {}'.format(column, sizeImg))
		temp_file.close()

		master.destroy()
		master.quit()

	tk.Button(master, text="Submit", command=colSize).grid(row=2)
	master.mainloop()

	temp_file=open('colsize.txt','r')
	col,size=map(str, temp_file.read().strip().split())
	size=int(size)
	temp_file.close(); os.remove('./colsize.txt')
	return (col, size)

# Accept user input for required details

root = tk.Tk()
root.withdraw() # Use to hide tkinter window

showinfo("Info","On the next screen, choose a template image.")
currdir = os.getcwd()
template = askopenfilename(parent=root, initialdir=currdir, title='Please select an image', filetypes =[('PNG File', '*.png'), ('JPEG File', '*.jpg')])

showinfo("Info","On the next screen, choose a CSV file for getting names of participants.")
currdir = os.getcwd()
filename = askopenfilename(parent=root, initialdir=currdir, title='Please select a csv file', filetypes =[('CSV File', '*.csv')])

msgBox=askquestion('Info', 'Do you want to add participant images?')
if msgBox=='yes':
	imgParticipantCheck=True
else:
	imgParticipantCheck=False

if (imgParticipantCheck):
	showinfo("Info","On the next screen, choose where the participant images are located.")
	currdir = os.getcwd()
	img_directory = askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
else: 
	img_directory=None

showinfo("Info","On the next screen, choose a font.")
currdir = os.getcwd()
font = askopenfilename(parent=root, initialdir=currdir, title='Please select a csv file', filetypes =[('TrueType font file', '*.ttf')])

col,size=inputColumnAndSize()

showinfo("Info","On the next screen, choose a color for the font.")
r,g,b=askcolor()[0]
r,g,b=str(int(r)),str(int(g)),str(int(b))

showinfo("Info","On the next screen, click where text should be placed.")
coorx,coory=spaceSelector(template)

if (imgParticipantCheck):
	showinfo("Info", "On the next screen, click where image of participant should be placed.")
	coorximg,cooryimg=spaceSelector(template)
else:
	coorximg,cooryimg=None,None

showinfo("Info","On the next screen, choose where the output files should be saved.")
currdir = os.getcwd()
directory = askdirectory(parent=root, initialdir=currdir, title='Please select a directory')

# Open CSV File
data=read_csv(filename)

for sno, row in enumerate(data[col],1): # Scan names row by row
	writeImage(template,font,size,coorx,coory,row,"rgb("+r+","+g+","+b+")", directory,coorximg,cooryimg,img_directory,imgParticipantCheck,sno)

showinfo("Info","Certificates generated successfully!")


