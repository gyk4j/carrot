import tkinter as tk

def close_window(): 
  root.destroy()

root = tk.Tk()

# place a frame
frame = tk.Frame(root)
frame.pack()

# place a label on the root window
message = tk.Label(frame, text="Hello, World!")
message.pack()

button = tk.Button (frame, text = "Good-bye.", command = close_window)
button.pack()

# keep the window displaying
root.mainloop()
