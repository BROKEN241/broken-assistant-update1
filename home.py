import os
import tkinter
from tkinter import *
import sys
from PIL import Image, ImageTk
import wikipedia
import pyttsx3
from time import strftime

# Speak Function
def speak():
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voices',voice[0].id)
    engine.runAndWait()

# Button Commands
def progress():
    print("In progress")

def pause():
    print("Paused.")    


# Window
window = tkinter.Tk()

window.title('AI ASSISTANT')

window.geometry("793x750")
icon = os.path.join(sys.path[0], "logo.ico")
window.iconbitmap(icon)

start_button_img = PhotoImage(file= "START.png")
pause_button_img = PhotoImage(file= "PAUSE.png")
exit_button_img = PhotoImage(file= "EXIT.png")

#Welcome_Label = Label()

Start_button = Button(window, 
                      image = start_button_img,
#                        background = "#EC1515", 
#                        foreground = "#FAFAF8",
#                        activebackground = "WHITE", 
#                        activeforeground="#EC1515", 
#                        highlightthickness= 2, 
#                        highlightbackground= "#EC1515", 
#                        highlightcolor= "WHITE", 
                        cursor= "hand1",
                        width = 315, 
                        height = 69, 
                        border = 0, 
                        command = progress
#                        font = ('Arial', 16, 'bold') 
)
Start_button.place(x = 0, y = 1)
Start_button.pack()

Pause_button = Button(window, 
                      image = pause_button_img,
#                        background = "#EC1515", 
#                        foreground = "#FAFAF8",
#                        activebackground = "WHITE", 
#                        activeforeground="#EC1515", 
#                        highlightthickness= 2, 
#                        highlightbackground= "#EC1515", 
#                        highlightcolor= "WHITE", 
                        cursor= "hand1",
                        width = 315, 
                        height = 69, 
                        border = 0, 
                        command = pause
#                        font = ('Arial', 16, 'bold') 
)
Pause_button.place(x = 0, y = 1)
Pause_button.pack()

exit_button = Button(window, 
                      image = exit_button_img,
#                        background = "#EC1515", 
#                        foreground = "#FAFAF8",
#                        activebackground = "WHITE", 
#                        activeforeground="#EC1515", 
#                        highlightthickness= 2, 
#                        highlightbackground= "#EC1515", 
#                        highlightcolor= "WHITE", 
                        cursor= "hand1",
                        width = 315, 
                        height = 69, 
                        border = 0, 
                        command = exit
#                       font = ('Arial', 16, 'bold') 
)
exit_button.place(x = 0, y = 1)
exit_button.pack()

# Clock
def time():
    string = strftime("%H:%M:%S:%p")
    label.config(text =  string)
    label.after(1000,time)

label = Label(window, font = ("ds-digi",80), background = "black", foreground= "Red")
label.pack()
time()

window.mainloop()