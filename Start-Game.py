from tkinter import *
import tkinter
import os

win= Toplevel()
win.title("Game")
win.geometry("1000x700")

happy=0
sad=0
angry=0

# bg = PhotoImage(file = "800x600.png")
  
# # Show image using label
# label1 = Label( win, image = bg)
# label1.place(x = 0, y = 0)

Label(win, text="How are you feeling?",
font=('Poppins bold', 25)).pack(pady= 20)
Label(win, text="Let's play a puzzle based on your mood ;)",
font=('Poppins bold', 12)).pack(pady= 20)

def incr_happy():
    happy =+ 1
    print("happy:"+str(happy))
    win.destroy()
    os.system('python happypuzzle.py')
    # win.quit()

def incr_sad():
    sad =+ 1
    print("sad:"+str(sad))
    win.destroy()
    os.system('python sadpuzzle.py')

def incr_angry():
    angry =+ 1
    print("angry:"+str(angry))
    win.destroy()
    os.system('python angrypuzzle.py')


happy_img= PhotoImage(file='happy.png')
happy_label= Label(image=happy_img)
button1= Button(win, image=happy_img,command=incr_happy,borderwidth=0, height= 300, width=200)
button1.pack(pady=30)
button1.place(x=100,y=170)
text1= Label(win, text= "HAPPY")
text1.pack(pady=30)
text1.place(x=180,y=480)
# button1.grid(row=1,column=1)

sad_img= PhotoImage(file='cryr.png')
sad_label= Label(image=sad_img)
button2= Button(win, image=sad_img,command=incr_sad,borderwidth=0, height= 300, width=200)
button2.pack(pady=30)
button2.place(x=380,y=170)
text2= Label(win, text= "SAD")
text2.pack(pady=30)
text2.place(x=470,y=480)
# button2.grid(row=1,column=2)

angry_img= PhotoImage(file='angryr.png')
angry_label= Label(image=angry_img)
button3= Button(win, image=angry_img,command=incr_angry,borderwidth=0,height= 300, width=200)
button3.pack(pady=30)
button3.place(x=650,y=170)
text3= Label(win, text= "ANGRY")
text3.pack(pady=30)
text3.place(x=730,y=480)
# button3.grid(row=1,column=3)

print(happy)
print(sad)
print(angry)

win.mainloop()