import tkinter as tk

from PIL import Image, ImageTk

# Source: https://www.geeksforgeeks.org/python/how-to-resize-image-in-python-tkinter/
class ImageView:
    MIN=1 # For testing only.
    MAX=8 # For testing only.

    def __init__(self, window):
        self.current_img = 1

        self.imageview = tk.Label(window, bg='gray')
        self.load_image()
        self.imageview.pack(expand=True, fill=tk.BOTH)

    def load_image(self):
        file = "%d.jpg" % (self.current_img)
        #print(file)
        img = Image.open(file)
        width, height = img.size
        fit = img.resize( size=
            (int(width/2),
            int(height/2))
        )
        self.img = ImageTk.PhotoImage(fit)
        self.imageview.config(image = self.img)

    def next(self):
        if self.current_img < ImageView.MAX:
            self.current_img += 1

    def prev(self):
        if self.current_img > ImageView.MIN:
            self.current_img -= 1