import tkinter as tk
import cv2
from PIL import Image, ImageTk

# ✅ OpenCV VideoCapture
cap = cv2.VideoCapture(0)

# ✅ Tkinter GUI Window
root = tk.Tk()
root.title("Live Camera Feed")

# ✅ Label to Display Video Frames
label = tk.Label(root)
label.pack()

# ✅ Flag to control loop
running = True

# ✅ Function to update video frames
def show_frame():
    if not running:
        return  # Stop updating if running is False
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(image=Image.fromarray(frame))
        label.imgtk = img
        label.configure(image=img)
    root.after(10, show_frame)

# ✅ Function to handle window close
def on_closing():
    global running
    running = False
    cap.release()          # Release webcam
    root.destroy()         # Destroy window

# ✅ Handle close button
root.protocol("WM_DELETE_WINDOW", on_closing)

# ✅ Start video loop
show_frame()

# ✅ Start GUI loop
root.mainloop()

