import tkinter as tk

from PIL import Image, ImageTk

# Source: https://www.geeksforgeeks.org/python/how-to-resize-image-in-python-tkinter/
class ImageView:
    MIN=1 # For testing only.
    MAX=8 # For testing only.

    def __init__(self, window):
        self.current_img = 1
        self.img_id = -1

        # Set initial size to 640x480.
        self.imageview = tk.Canvas(window, bg='gray', width= 640, height= 480)
        self.imageview.pack(expand=True, fill=tk.BOTH)
        self.imageview.update()
        self.load_image()
        print("%d x %d" % (self.imageview.winfo_width(), self.imageview.winfo_height()))

    def load_image(self):
        file = "%d.jpg" % (self.current_img)
        #print(file)
        self.img_original = Image.open(file)
        self.fit_image()

    def fit_image(self):
        i_width, i_height = self.img_original.size
        c_width = self.imageview.winfo_width()
        c_height = self.imageview.winfo_height()

        print("Image Width     : %d pixels" % (i_width))
        print("Image Height    : %d pixels" % (i_height))
        print("Canvas Width    : %d pixels" % (c_width))
        print("Canvas Height   : %d pixels" % (c_height))

        aspect_ratio_h = c_width / i_width
        aspect_ratio_v = c_height / i_height
        print("Aspect ratio (w): %f" % (aspect_ratio_h))
        print("Aspect ratio (h): %f" % (aspect_ratio_v))
        aspect_ratio = min( aspect_ratio_h, aspect_ratio_v )

        resized_width = int(i_width * aspect_ratio)
        resized_height = int(i_height * aspect_ratio)

        self.img_resized = self.img_original.resize(
            size = ( resized_width, resized_height )
        )
        self.img = ImageTk.PhotoImage(self.img_resized)
        
        if self.img_id != -1:
            self.imageview.delete( id = self.img_id )

        x = (c_width - resized_width) // 2
        y = (c_height - resized_height) // 2
        self.img_id = self.imageview.create_image(x, y, anchor=tk.NW, image = self.img)
            

    def next(self):
        if self.current_img < ImageView.MAX:
            self.current_img += 1
        self.load_image()

    def prev(self):
        if self.current_img > ImageView.MIN:
            self.current_img -= 1
        self.load_image()