import tkinter as tk
#from PIL import Image, ImageTk
import pyvips

root = tk.Tk()

# The built-in tk.PhotoImage does not support JPEG format. This would fail to read the JPEG file.
image = tk.PhotoImage(file="1.jpg")

# Most examples use Pillow for JPEG loading instead of libvips/pyvips
# image = ImageTk.PhotoImage(Image.open("1.jpg"))

# Trying pyvips JPEG loading, but tkinter Label can't use pyvips.Image
# Obviously, this doesn't work as well.
# image = pyvips.Image.new_from_file('1.jpg', access='sequential')

label = tk.Label(root, image = image)

label.pack()

root.mainloop()
