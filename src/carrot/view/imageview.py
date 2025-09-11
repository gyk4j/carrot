import tkinter as tk

from PIL import Image, ImageTk, ImageFile

from ..resource import ClassLoader

# Source: https://www.geeksforgeeks.org/python/how-to-resize-image-in-python-tkinter/
class ImageView:
    MIN=1 # For testing only.
    MAX=8 # For testing only.

    def __init__(self, window):
        self._current_img = 1
        self._img_id = -1

        # Set initial size to 640x480.
        self._imageview = tk.Canvas(
            window, 
            bg='gray', 
            width= 640, 
            height= 480, 
            relief=tk.SUNKEN,
            borderwidth = 1,
        )
        self._imageview.pack(expand=True, fill=tk.BOTH)
        self._imageview.update()
        self.load_image()
        print("%d x %d" % (self._imageview.winfo_width(), self._imageview.winfo_height()))

        self._imageview.bind("<Configure>", self.on_configure)

    @property
    def imageview(self) -> tk.Canvas:
        return self._imageview

    @property
    def img_original(self) -> Image.Image:
        return self._img_original

    @property
    def img_resized(self) -> tk.Image:
        return self._img_resized

    @property
    def img(self) -> Image.Image:
        return self._img

    def load_image(self):
        cl = ClassLoader()
        file = cl.get_resource("%d.jpg" % (self._current_img))
        #print(file)
        self._img_original : Image.Image = Image.open(file)
        self.fit_image()

    def fit_image(self):
        i_width, i_height = self._img_original.size
        self.c_width = self._imageview.winfo_width()
        self.c_height = self._imageview.winfo_height()

        print("Image Width     : %d pixels" % (i_width))
        print("Image Height    : %d pixels" % (i_height))
        print("Canvas Width    : %d pixels" % (self.c_width))
        print("Canvas Height   : %d pixels" % (self.c_height))

        aspect_ratio_h = self.c_width / i_width
        aspect_ratio_v = self.c_height / i_height
        print("Aspect ratio (w): %f" % (aspect_ratio_h))
        print("Aspect ratio (h): %f" % (aspect_ratio_v))

        # Do not stretch a small image i.e. aspect ratio > 1 and use 1 as a fallback.
        # Otherwise, shrink a larger image proportionately to fit the canvas i.e. aspect ratio < 1.
        aspect_ratio = min( 1, aspect_ratio_h, aspect_ratio_v )

        resized_width = int(i_width * aspect_ratio)
        resized_height = int(i_height * aspect_ratio)

        self._img_resized : Image.Image = self._img_original.resize(
            size = ( resized_width, resized_height )
        )
        self._img = ImageTk.PhotoImage(self._img_resized)
        
        if self._img_id != -1:
            self._imageview.delete( self._img_id )

        x = (self.c_width - resized_width) // 2
        y = (self.c_height - resized_height) // 2
        self._img_id = self._imageview.create_image(x, y, anchor=tk.NW, image = self._img)
            
    def on_configure(self, event):
        print(event)
        width_latest = event.width
        height_latest = event.height

        # Assume no change, just repeated duplicate event.
        dirty: bool = False

        # Update only if there is any change.
        if width_latest != self.c_width:
            self.c_width = width_latest
            dirty = True

        # Update only if there is any change.
        if height_latest != self.c_height:
            self.c_height = height_latest
            dirty = True

        # Only print if size is changed.
        if dirty:
            print("%d x %d" % (self.c_width, self.c_height))
            self.fit_image()

    def next(self):
        if self._current_img < ImageView.MAX:
            self._current_img += 1
        self.load_image()

    def prev(self):
        if self._current_img > ImageView.MIN:
            self._current_img -= 1
        self.load_image()