import tkinter as tk
from tkinter import PhotoImage
import subprocess

def on_hover(event):
    x, y = event.x, event.y
    if 125 <= x <= 365:
        if 469 <= y <= 522:
            left_canvas.itemconfig(left_image_item, image=img5)
        elif 369 <= y <= 422:
            left_canvas.itemconfig(left_image_item, image=img4)
        elif 269 <= y <= 322:
            left_canvas.itemconfig(left_image_item, image=img3)
        elif 169 <= y <= 222:
            left_canvas.itemconfig(left_image_item, image=img2)
    else:
        left_canvas.itemconfig(left_image_item, image=img1)

def on_click(event):
    x, y = event.x, event.y
    if 125 <= x <= 365:
        if 169 <= y <= 222:
            right_canvas.itemconfig(right_image_item, image=img6)
        elif 269 <= y <= 322:
            right_canvas.itemconfig(right_image_item, image=img7)  
        elif 369 <= y <= 422:
            right_canvas.itemconfig(right_image_item, image=img8)  
        elif 469 <= y <= 522:
            right_canvas.itemconfig(right_image_item, image=img9)  

def right_click_link(event):
    x, y = event.x, event.y
    if 120 <= x <= 310 and 269 <= y <= 322:
        right_canvas.itemconfig(right_image_item, image=img10)
        subprocess.Popen(['python', 'KendrickPIN.py'])

root = tk.Tk()
root.title("Messenger")

# Load images
img1 = PhotoImage(file="Chat/Desktop - 1.png")
img2 = PhotoImage(file="Chat/Desktop - 2.png")
img3 = PhotoImage(file="Chat/Desktop - 3.png")
img4 = PhotoImage(file="Chat/Desktop - 4.png")
img5 = PhotoImage(file="Chat/Desktop - 5.png")
img6 = PhotoImage(file="Chat/Desktop - 6.png")
img7 = PhotoImage(file="Chat/Desktop - 7.png")
img8 = PhotoImage(file="Chat/Desktop - 8.png")
img9 = PhotoImage(file="Chat/Desktop - 9.png")
img10 = PhotoImage(file="Chat/Desktop - 10.png")

# Create a left frame
left_frame = tk.Frame(root, width=414.34, height=720)
left_frame.pack(side="left")

# Create a right frame
right_frame = tk.Frame(root, width=865.76, height=720)
right_frame.pack(side="right")

# Create left canvas and display initial image (img1)
left_canvas = tk.Canvas(left_frame, width=414.34, height=720)
left_canvas.pack()
left_image_item = left_canvas.create_image(640, 720 / 2, image=img1)

# Create right canvas and display initial image (img1)
right_canvas = tk.Canvas(right_frame, width=865.76, height=720)
right_canvas.pack()
right_image_item = right_canvas.create_image(220, 720 / 2, image=img1)

# Bind events
left_canvas.bind("<Motion>", on_hover)
left_canvas.bind("<Button-1>", on_click)
right_canvas.bind("<Button-1>", right_click_link)

root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))
root.mainloop()
