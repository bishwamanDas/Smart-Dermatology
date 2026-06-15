from tkinter import *
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np
import os
import sys

BACKGROUND = '#FFFFFF'
RED = '#000000'
fonts = ("Arial", 15, "bold")

image_label = None
disease_label = None
selected_image_path = None

window = Tk()
window.title('Smart Dermatology')
window.minsize(width=500, height=700)
window.config(padx=10, pady=10, bg=BACKGROUND)

title_label = Label(window, text="SMART DERMATOLOGY", font=("Arial", 16, "bold"), bg=BACKGROUND, fg=RED)
title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="n")



disease_tips = {
    'actinic keratosis': [
        'Use sunscreen with SPF 30+.',
        'Avoid sun exposure during peak hours.',
        'Consult a dermatologist for cryotherapy.'
    ],
    'basal cell carcinoma': [
        'Consult a dermatologist immediately.',
        'Consider Mohs surgery for removal.',
        'Protect skin with hats and clothing.'
    ],
    'dermatofibroma': [
        'Monitor for changes in size or color.',
        'Avoid trauma to the area.',
        'See a doctor if it becomes painful.'
    ],
    'melanoma': [
        'Seek immediate medical evaluation.',
        'Monitor for ABCDE signs (asymmetry, border, color, diameter, evolving).',
        'Avoid tanning beds and UV exposure.'
    ],
    'nevus': [
        'Watch for asymmetry or color changes.',
        'Photograph moles to track changes.',
        'Biopsy if changes are suspicious.'
    ],
    'pigmented benign keratosis': [
        'No treatment needed if asymptomatic.',
        'Consider removal for cosmetic reasons.',
        'Avoid picking or scratching the area.'
    ],
    'seborrheic keratosis': [
        'Remove if irritated or itchy.',
        'Use gentle skin care products.',
        'Consult a doctor for removal options.'
    ],
    'squamous cell carcinoma': [
        'Seek early treatment from a doctor.',
        'May require surgical removal.',
        'Use sun protection to prevent recurrence.'
    ],
    'vascular lesion': [
        'Consider laser therapy for treatment.',
        'Consult a dermatologist or specialist.',
        'Avoid trauma to the affected area.'
    ]
}

# Load the ML model
try:
    model = tf.keras.models.load_model('model.h5')
except Exception as e:
    messagebox.showerror(title="Model Error", message=f"Error loading model: {str(e)}")
    model = None

disease_classes = ['actinic keratosis', 'basal cell carcinoma', 'dermatofibroma',
                   'melanoma', 'nevus', 'pigmented benign keratosis',
                   'seborrheic keratosis', 'squamous cell carcinoma', 'vascular lesion']

def diagnose():
    global disease_label, selected_image_path
    if not selected_image_path:
        messagebox.showerror(title="Error", message="Please select an image file first.")
        return

    if model is None:
        messagebox.showerror(title="Model Error", message="Machine learning model not loaded.")
        return

    # Remove previous disease label if exists
    if disease_label is not None:
        disease_label.destroy()

    try:
        # Load and resize the image to 180x180
        img = Image.open(selected_image_path)
        img = img.resize((180, 180), Image.Resampling.LANCZOS)

        # Convert to NumPy array and normalize
        img_array = np.array(img) 
        if len(img_array.shape) == 2:  
            img_array = np.stack([img_array] * 3, axis=-1)
        elif img_array.shape[-1] == 4:  
            img_array = img_array[..., :3]

        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)  # Shape: (1, 180, 180, 3)

        # Predict using the model
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions)
        predicted_disease = disease_classes[predicted_class]

        # Display the predicted disease
        disease_label = Label(treatment_frame, text="The disease: " + predicted_disease, font=("Arial", 12), bg=BACKGROUND, fg=RED)
        disease_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        
        #Tips 
        tips_list = disease_tips.get(predicted_disease, ["No tips available for this disease."])
        numbered_tips = "\n".join(f"{i+1}) {tip}" for i, tip in enumerate(tips_list))
        tips_content.config(text=numbered_tips)

    except Exception as e:
        messagebox.showerror(title="Prediction Error", message=f"Error during prediction: {str(e)}")




def select_file():
    global image_label, selected_image_path
    selected_file = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=(
            ("Image Files", "*.png;*.jpg;*.jpeg"),  # Allow multiple image file extensions
            ("PNG Files", "*.png"),
            ("JPEG Files", "*.jpg;*.jpeg"),
        )
    )
    if selected_file:
        selected_image_path = selected_file
        file_path_entry.config(state='normal')
        file_path_entry.delete(0, END)
        file_path_entry.insert(0, selected_file)
        file_path_entry.config(state='readonly')  

        if image_label is not None:
            image_label.destroy()
        try:
            img = Image.open(selected_file)
            img = img.resize((200, 200), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)

            # Display image in the treatment section
            image_label = Label(treatment_frame, image=photo, bg=BACKGROUND)
            image_label.image = photo  # Keep a reference to avoid garbage collection
            image_label.grid(row=1, column=0, padx=10, pady=10)

        except Exception as e:
            messagebox.showerror(title="Image Error", message=f"Error loading image: {str(e)}")
    else:
        messagebox.showerror(title="Error", message="No file selected.")

# Diagnosis Section
diagnosis_frame = Frame(window, bg=BACKGROUND, highlightbackground=RED, highlightthickness=2)
diagnosis_frame.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

# Diagnosis Label
diagnosis_label = Label(diagnosis_frame, text="Diagnosis", font=fonts, bg=BACKGROUND, fg=RED)
diagnosis_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

# File selection
file_path_entry = Entry(diagnosis_frame, font=("Arial", 10), bg="white", fg="black", width=40)
file_path_entry.insert(0, "No file selected")  # Set initial text
file_path_entry.config(state='readonly')  # Make it read-only
file_path_entry.grid(row=1, column=0, padx=5, pady=5, sticky="w")

choose_button = Button(diagnosis_frame, text="Choose", font=("Arial", 10, "bold"), bg=RED, fg="white", command=select_file)
choose_button.grid(row=1, column=1, padx=2, pady=2,sticky="w")

# Diagnose Button
diagnose_button = Button(diagnosis_frame, text="Diagnose", font=("Arial", 10, "bold"), bg=RED, fg="white", command=diagnose)
diagnose_button.grid(row=2, column=0, columnspan=2, padx=2, pady=2, sticky="ew")

# Treatment Section
treatment_frame = Frame(window, bg=BACKGROUND, highlightbackground=RED, highlightthickness=2)
treatment_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

# Treatment Label
treatment_label = Label(treatment_frame, text="Treatment", font=fonts, bg=BACKGROUND, fg=RED)
treatment_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

# Disease Label (initially empty)
disease_label_text = Label(treatment_frame, text="The disease:", font=("Arial", 12), bg=BACKGROUND)
disease_label_text.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Tips Section
tips_label = Label(treatment_frame, text="Tips:", font=("Arial", 12, "bold"), bg=BACKGROUND)
tips_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

tips_content = Label(treatment_frame, text="Select an image and diagnose to see tips.", font=("Arial", 10),
                     bg=BACKGROUND, justify=LEFT)
tips_content.grid(row=4, column=0, padx=10, pady=5, sticky="w")

window.grid_rowconfigure(0, weight=0)
window.grid_rowconfigure(1, weight=0)
window.grid_rowconfigure(2, weight=1)

window.grid_columnconfigure(0, weight=1)

diagnosis_frame.grid_columnconfigure(0, weight=1)
diagnosis_frame.grid_columnconfigure(1, weight=1)

treatment_frame.grid_columnconfigure(0, weight=1)

window.mainloop()
