import tkinter as tk
import tkinter.filedialog as fd
import pyvips

root = tk.Tk()

def thumbnail():
  input = fd.askopenfilename(title="Select Picture", filetypes=[("JPEG images", ('*.jpg')), ("All files", "*.*")]) 
  thumb = pyvips.Image.thumbnail(input, 128, height=128)
  thumb.write_to_file('tn-test.jpg')
  
def close_window(): 
  root.destroy()

def main():
  # place a frame
  frame = tk.Frame(root)
  frame.pack()

  # place a label on the root window
  message = tk.Label(frame, text=pyvips.API_mode)
  message.pack()

  btn_thumbnail = tk.Button (frame, text = "Thumbnail", command = thumbnail)
  btn_thumbnail.pack()

  button = tk.Button (frame, text = "Good-bye.", command = close_window)
  button.pack()

  # keep the window displaying
  root.mainloop()

if __name__ == "__main__":
  main()
  