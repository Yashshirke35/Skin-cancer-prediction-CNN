import tkinter as tk
from PIL import Image,ImageTk
# from tkvideo import tkvideo


root=tk.Tk()
root.configure(background='white')
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))
root.title("Skin Cancer Detection")



# video_label = tk.Label(root)
# video_label.pack()

# player = tkvideo("127351 (720p).mp4", video_label, loop=1, size=(w, h))
# player.play()


image2=Image.open("s1.jpeg")
image2=image2.resize((w,h),Image.ANTIALIAS)

background_image= ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image
background_label.place(x=0,y=0)


label=tk.Label(root,text="Skin Cancer Detection ",font=("Calibri",40),
               bg="light gray",
               width=60,
               height=1)
label.place(x=0,y=0)        



def log():
    from subprocess import call
    call(['python','Login from1.py'])

btn=tk.Button(root,text="Login",command=log,font=("Arial",18),width=9, height=2,bd=0,
              bg="light gray",
              #fg="white",
            )
btn.place(x=1200,y=00)

def reg():
    from subprocess import call
    call(['python','final Reg.py'])

btn=tk.Button(root,text="Register",command=reg,font=("Arial",18),width=7,height=2,bd=0,
              bg="light gray",
              #fg="white",
            )
btn.place(x=1400,y=00)







register1=tk.Label(root,text="Skin care is a set of practices that can improve the appearance of your skin, \n relieve skin conditions, and support the integrity of your skin. \n Here are some tips for healthy skin: Cleanse: Wash your face gently with warm water and a mild cleanser. \n You can apply the cleanser in circles with your fingertips. Protect from the sun: Avoid intense sun exposure and use sunscreen. \n You can also wear protective clothing and avoid tanning beds and sunlamps. \n Moisturize: Use gentle moisturizers, lotions, or creams to prevent dry skin. Hydrate: Drink plenty of water to stay hydrated.\n  Reduce stress: Stress can harm your skin, so try to keep it in check. Sleep: \n Get enough sleep, which is about 9 hours a night for teens and 7-8 hours for adults. \n Exfoliate: Exfoliate to remove dead skin cells and brighten your complexion.\n  Monitor your skin: If you notice any changes to your skin, like a rash or mole that changes size or color, talk to your doctor. \n Some other skin care products you can use include toners and serums. " ,
                   font=('Cambria',15),height=20,).place(x=300,y=300)

import webbrowser

def open_browser():
    webbrowser.open("https://www.practo.com/pune/treatment-for-skin-cancer-screening")
link = tk.Label(root, text="https://www.practo.com/pune/treatment-for-skin-cancer-screening", fg="blue", cursor="hand2")
link.place(x=700,y=700)

# Bind the label to open the link
link.bind("<Button-1>", lambda e: open_browser())

root.mainloop()