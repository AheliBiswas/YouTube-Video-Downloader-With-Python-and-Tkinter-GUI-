import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
from pytube import YouTube
import shutil


def download_path():
    path = filedialog.askdirectory()  # directory showing up and select a folder
    show_path.config(text=path)  # loading directory in the label


try:
    def download_video():
        get_link = entry.get()  # getting video link from the entry
        get_path = show_path.cget("text")  # getting path link from the label
        root.title("Downloading.......")
        mp4_video = YouTube(get_link).streams.get_highest_resolution().download()  # downloading the YouTube video
        shutil.move(mp4_video, get_path)  # moving to the desired path
        messagebox.showinfo("Youtube Video Downloader", "Download Completed")
        root.title("Youtube Video Downloader")
except:
    messagebox.showerror("Youtube Video Downloader", "Something Went Wrong")

root = tk.Tk()
root.resizable(False, False)
root.geometry('666x333+375+170')
app_logo = ImageTk.PhotoImage(Image.open('app_logo.png'))
root.iconphoto(False, app_logo)
root.title("Youtube Video Downloader")

# --------------------------------- Head Line -------------------------------------------
img = ImageTk.PhotoImage(Image.open('youtube.png').resize((122, 47)))
logo = tk.Label(root, image=img)
logo.place(x=134, y=40)

label = tk.Label(root, text="Video Downloder!!!!", fg="#101010", font=('Arial', 22, 'bold'))
label.place(x=270, y=45)

# --------------------------------- Entry Label and Entry Box -------------------------------------------
label_1 = tk.Label(root, text="Enter your link here :", font=('Arial', 12, 'bold'))
label_1.place(x=168, y=115)

entry = tk.Entry(root, bg="#D9D9D9", font=('Arial', 11), bd=2)
entry.place(width=330, height=38, x=168, y=147)

# --------------------------------- Path Label -------------------------------------------
path_label = tk.Label(root, text="Path: ", font=('Arial', 11))
path_label.place(x=168, y=204)

show_path = tk.Label(root, text="_________", font=('Arial', 11))
show_path.place(x=215, y=204)

# --------------------------------- Path Button -------------------------------------------
yellow_img = ImageTk.PhotoImage(Image.open('yellow_btn.png').resize((100, 48)))
path_btn = tk.Button(root, image=yellow_img, text="Select path", borderwidth=0, cursor="hand2", font=('Arial', 11)
                     , command=download_path)
path_btn.place(x=185, y=244)

# --------------------------------- Download Button -------------------------------------------
green_img = ImageTk.PhotoImage(Image.open('green_btn.png').resize((100, 48)))
download_btn = tk.Button(root, image=green_img, text="Download", borderwidth=0, cursor="hand2", font=('Arial', 11),
                         command=download_video)
download_btn.place(x=381, y=244)

root.mainloop()
