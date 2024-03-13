from tkinter import *
from uuid import uuid4
from tkinter import Toplevel, Label
from PIL import Image, ImageTk
from tkVideoPlayer import TkinterVideo

windows = Tk()
windows.title("Video and Picture on tkinter")

def picture():
    window = Toplevel(windows)
    window.title("Picture")
    window.geometry("500x500")
    window.resizable(False, False)
    window.config(bg="black")
    image = Image.open("logo.png")
    photo = ImageTk.PhotoImage(image)
    label = Label(window, image=photo)
    label.image = photo
    label.pack()


def video():
    window = Toplevel(windows)
    window.title("Video")
    window.geometry("720x360")
    window.resizable(False, False)
    window.config(bg="black")
    videoplayer = TkinterVideo(master=window, scaled=True)
    videoplayer.load(r"Adobe_infintive.mp4")
    videoplayer.pack(fill="both", expand=True)
    videoplayer.play()

def info():
    window = Toplevel(windows)
    window.title("Info")
    window.geometry("500x500")
    window.resizable(False, False)
    window.config(bg="black")
    label = Label(window, text="Bu dasturda tkinterda videoni va rasmlarni ko'rish mumkin", font=("Arial", 20), bg="black", fg="white")
    label.pack()
windows.geometry("600x400")
windows.config(bg="blue")  # Set background color of the window
text1 = Label(windows, text="Videoni ko'rish uchun bosing", font=("Arial", 20), bg="blue", fg="white")  # Set background and foreground color of the label
text1.pack()
click1 = Button(windows, text="Video", font=("Arial", 20), command=video, bg="green", fg="white")  # Set background and foreground color of the button
click1.pack()
text2 = Label(windows, text="Rasmni ko'rish uchun bosing", font=("Arial", 20), bg="blue", fg="white")  # Set background and foreground color of the label
text2.pack()
click2 = Button(windows, text="Picture", font=("Arial", 20), command=picture, bg="green", fg="white")  # Set background and foreground color of the button
click2.pack()
windows.mainloop()