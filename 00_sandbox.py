#Import required libraries
from tkinter import *
#Create an instance of tkinter frame
win= Tk()
#Define the geometry of the window
win.geometry("750x250")

#Define functions
def on_enter(e):
    original_colour = button.cget("background")
    button.config(background="Orange", foreground= "white", font=original_colour)

def on_leave(e):
    new_colour = button.cget("font")
    button.config(background=new_colour, foreground= 'black')

#Create a Button
button= Button(win, text= "Click Me", font= ('Helvetica 13 bold'), background = "red")
button.pack(pady= 20)

#Bind the Enter and Leave Events to the Button
button.bind('<Enter>', on_enter)
button.bind('<Leave>', on_leave)
win.mainloop()