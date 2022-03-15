#Import required libraries
from tkinter import *
#Create an instance of tkinter frame
win= Tk()
#Define the geometry of the window
win.geometry("750x250")

def setup_hover_button(button_name):
    colour = button_name.cget("background")
    button_name.bind('<Enter>', on_enter)
    button_name.bind('<Leave>', lambda e: on_leave(e,colour))
#Define functions
def on_enter(e):
    e.widget.config(background="Orange", foreground= "white")

def on_leave(e, colour):
    e.widget.config(background=colour, foreground= 'black')

#Create a Button
button= Button(win, text= "Click Me", font= ('Helvetica 13 bold'), background = "blue")
button.pack(pady= 20)

button2= Button(win, text= "Click Me", font= ('Helvetica 13 bold'), background = "red")
button2.pack(pady= 20)

setup_hover_button(button)
setup_hover_button(button2)
win.mainloop()
