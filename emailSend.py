from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory
import tkinter.font as tkFont
from tkinter.messagebox import showinfo
from pandas import read_csv

def inputColumnAndEmail():

    # Create tk window and config
    master = tk.Tk()
    master.title('Column name and email')

    fontStyle = tkFont.Font(family="Lucida Grande", size=22)
    tk.Label(master, text="Enter column name containing names of participants: ", font=fontStyle).grid(row=0)
    tk.Label(master, text="Enter column name containing email of participants: ", font=fontStyle).grid(row=1)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    col, email= None, None

    def colEmail():
        
        # Get info from button
        column, sizeImg = e1.get(), e2.get()

        temp_file = open("colemail.txt","w")
        temp_file.write('{} {}'.format(column, sizeImg))
        temp_file.close()

        master.destroy()
        master.quit()

    tk.Button(master, text="Submit", command=colEmail).grid(row=2)
    master.mainloop()

    temp_file=open('colemail.txt','r')
    col,email=map(str, temp_file.read().strip().split())
    temp_file.close(); os.remove('./colemail.txt')
    return (col, email)

def sendEmailPDF(path_to_pdf, subject, message, destination, password_path=None):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    # Uncomment and replace email_user with your email, replace password_user with you password.
    # email_user = ''
    # password_user = ''
    server.login(email_user, password_user)
    msg = MIMEMultipart()

    message = f'{message}'
    msg['Subject'] = subject
    msg['From'] = email_user
    msg['To'] = destination
    # Insert the text to the msg going by e-mail
    msg.attach(MIMEText(message, "plain"))
    # Attach the pdf to the msg going by e-mail
    with open(path_to_pdf, "rb") as f:
        attach = MIMEApplication(f.read(),_subtype="pdf")
    attach.add_header('Content-Disposition','attachment',filename='Certificate')
    msg.attach(attach)
    # send msg
    server.send_message(msg)

root = tk.Tk()
root.withdraw() # Use to hide tkinter window

showinfo("Info","On the next screen, choose text file containing message to participant.")
currdir = os.getcwd()
filename = askopenfilename(parent=root, initialdir=currdir, title='Please select a txt file', filetypes =[('Text file', '*.txt')])

with open(filename,'r') as f:
    message = f.read()

showinfo("Info","On the next screen, choose a CSV file for getting names and emails of participants.")
currdir = os.getcwd()
filename = askopenfilename(parent=root, initialdir=currdir, title='Please select a csv file', filetypes =[('CSV File', '*.csv')])

showinfo("Info","On the next screen, choose where the certificates are located.")
currdir = os.getcwd()
directory = askdirectory(parent=root, initialdir=currdir, title='Please select a directory')

col,emailcol = inputColumnAndEmail()

data=read_csv(filename)

cnt = 1
for i in data.index:
    row, email = data[col][i], data[emailcol][i]
    sendEmailPDF(directory+'/'+str(cnt)+'-'+row+'.pdf','Certificate',message,email)
    cnt+=1