from writecertificate import writeimage
import pandas as pd

print("Enter Certificate template Name: ", end="")
template=input()
print("Enter CSV Filename: ", end="")
filename=input()
print("Enter Column Name containing to Data: ", end="")
col=input()
print("Enter TrueType Font Filename: ", end="")
font=input()
print("Enter Font Size: ", end="")
size=int(input())
print("Enter Space Separated x,y Coordianates of text to written: ", end="")
coorx,coory=map(int,input().split())
print("Enter Space Separated RGB values of Text Color: ", end="")
r,g,b=map(str,input().split())


data=pd.read_csv(filename)

for row in data[col]:
	
	writeimage("Certificate.png","pala.ttf",70,430, 400,row,"rgb("+"112"+","+"17"+","+"17"+")")

