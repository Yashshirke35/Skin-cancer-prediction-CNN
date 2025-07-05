import tkinter as tk 
import tkinter
import sqlite3
import random
from tkinter import messagebox as ms
from PIL import Image,ImageTk
from tkinter.ttk import *

root=tk.Tk()
root.configure(background='#73A16C')

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))
# oot.title("Background Image")

image2=Image.open('s4.jpg')
image2=image2.resize((w,h),Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root,image=background_image)
background_label.image = background_image
background_label.place(x=0,y=0)

#############################################################################################################


Email = tk.StringVar()
password = tk.StringVar() 
 
def login():
 

    with sqlite3.connect('skin.db') as db:
         c = db.cursor()

        
         db = sqlite3.connect('skin.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                        "(name TEXT, address TEXT,  Email TEXT, country TEXT, Phoneno TEXT, Gender TEXT, password TEXT)")
         db.commit()
         
         
         find_entry = ('SELECT * FROM registration WHERE Email = ? and password = ?')
         
         c.execute(find_entry, [(Email.get()), (password.get())])
         result = c.fetchall()
         if result:
            msg = ""
          
            print(msg)
            ms.showinfo("messege", "Login sucessfully")
            

            from subprocess import call
            call(['python','GUI_Master.py'])
            
           
         
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')





# New_Password=tk.StringVar()
# def forget():
#     con=sqlite3.connect("project11.db")
#     con.execute("""
#                 update registration set New_Password= Password where pass)

###############################################################################################################

label=tk.Label(root,text="Skin Cancer Detection ",font=("Calibri",40),
               bg="#e4b7a0",
               width=60,
               height=1)
label.place(x=0,y=0)        



a11=tk. Label(root,text='Login here ',fg='black',bg ='#e4b7a0',font=('Forte',25)).place(x=230,y=200)

canvas1=tk.Canvas(root,border=0,background="#e4b7a0")
canvas1.place(x=50,y=280,width=500,height=400)

#login=Label(root,text="Login",font=('Arial',25),foreground='green').place(x=270,y=350)
a11=tk. Label(root,text='Enter Email',bg='#e4b7a0',font=('Cambria',14)).place(x=120,y=400)
a12=tk. Label(root,text='Enter Password',bg='#e4b7a0',font=('Cambria',14)).place(x=120,y=450)

b11=tk.Entry(root,width=40, textvariable=Email,bg='#e4b7a0').place(x=270,y=400,)
b12=tk. Entry(root,width=40,show='*', textvariable=password,bg='#e4b7a0').place(x=270,y=455,)


def forgot():
    from subprocess import call
    call(['python','forgot password.py'])


button2=tk.Button(root,text="Forgot Password?",fg='blue',bg='#e4b7a0',command=forgot)
button2.place(x=400,y=500)



button2=tk.Button(root,text="Login",font=("Bold",9),command=login,width=50,bg='#e4b7a0')
button2.place(x=130,y=560)

a=tk. Label(root,text='Not a Member?',font=('Cambria',11),bg='#e4b7a0').place(x=350,y=657)

def reg():
    from subprocess import call
    call(['python','final reg.py'])

button1=tk.Button(root,text="sign up",fg='blue',bg='#e4b7a0',command=reg)
button1.place(x=450,y=653,width=55)



root.mainloop()