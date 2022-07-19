import tkinter as tk
from PIL import Image

root = tk.Tk()
file="img\\00380c484c72dc2bfeab1e1e10e2ff7e.gif"

info = Image.open(file)

frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None

im2 = im[count]

count += 1
if count == frames:
        count = 0
        anim = root.after(50,count)


gif_label = tk.Label(root,image=anim)

gif_label.configure(image=im2)
gif_label.pack()


root.mainloop()