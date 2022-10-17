from tkinter import Label, Tk 
import time

window = Tk()
window.title("Digital Clock")
window.geometry("620x200")
window.resizable(1,1)

text_font = ("Boulder", 70, 'bold')
background = "#000000"
foreground = "#FFFFFF"
width = 50

label = Label(window, font = text_font, bg= background, fg = foreground, bd = width)
label.grid(row=0, column = 1)

def digital_clock():
    time_live = time.strftime("%I:%M:%S %p")
    label.config(text=time_live)
    label.after(200, digital_clock)

digital_clock()
window.mainloop()
