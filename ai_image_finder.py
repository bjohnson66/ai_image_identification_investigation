import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES  # For drag-and-drop support
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageGrab
import numpy as np
import os


def analyze_image(img):
    """Analyze the image and return a confidence score based on averaging pixel values."""

    # Convert the image to RGB if it's not already
    img = img.convert("RGB")
    
    # Convert the image to a NumPy array
    img_array = np.array(img)
    
    # Calculate the average pixel value across all color channels
    avg_pixel_value = np.mean(img_array)
    
    # Scale average pixel value to percentage (0-100)
    avg_percentage = (avg_pixel_value / 255) * 100  
    print(f"Average Pixel Value: {avg_percentage:.2f}%")
    
    confidence = max(0, 100 - abs(avg_percentage - 50) * 2)

    # Confidence is high if the pixel value is within the grey range
    #50/50 diagonal coin split = 82.5
    #more false positives = 70
    #more false negatives = 90
    
    if confidence>=82.5:
        return f"Likely AI Generated Image (Confidence: {confidence:.2f}%)"
    else:
        return f"Likely Real Image (Confidence: {confidence:.2f}%)"



def load_image(img_path):
    """Load and display the image from the given file path, and analyze it."""
    try:
        img = Image.open(img_path)
        img.thumbnail((400, 400))
        img_tk = ImageTk.PhotoImage(img)
        img_label.config(image=img_tk)
        img_label.image = img_tk
        
        # Analyze the image after loading and display the result
        result = analyze_image(img)
        messagebox.showinfo("Analysis Result", result)
    except Exception as e:
        messagebox.showerror("Error", f"Unable to open image: {e}")

def upload_image():
    """Open file chooser to upload an image."""
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        load_image(file_path)

def handle_drag_and_drop(event):
    """Handle drag-and-drop image loading."""
    file_path = event.data.strip()
    if os.path.isfile(file_path) and file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        load_image(file_path)
    else:
        messagebox.showerror("Error", "Please drop a valid image file.")

def paste_image():
    """Handle image pasting from clipboard."""
    try:
        img = ImageGrab.grabclipboard()  # Grab the image from the clipboard
        if isinstance(img, Image.Image):
            img.thumbnail((400, 400))
            img_tk = ImageTk.PhotoImage(img)
            img_label.config(image=img_tk)
            img_label.image = img_tk
            
            # Analyze the pasted image and display the result
            result = analyze_image(img)
            messagebox.showinfo("Analysis Result", result)
        else:
            messagebox.showerror("Error", "No image found in clipboard.")
    except Exception as e:
        messagebox.showerror("Error", f"Unable to paste image: {e}")

# Set up the GUI window with drag-and-drop functionality
root = TkinterDnD.Tk()  # Use TkinterDnD for drag-and-drop
root.title("AI Image Detector")

# Drag-and-drop event handler
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', handle_drag_and_drop)

# Upload button for file chooser
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

# Paste button to paste from clipboard
paste_button = tk.Button(root, text="Paste Image", command=paste_image)
paste_button.pack(pady=10)

# Image display area
img_label = tk.Label(root)
img_label.pack(pady=20)

# Start the GUI
root.mainloop()

