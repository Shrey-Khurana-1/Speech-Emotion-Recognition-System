#Original and placeholder GUI Deisgn before finishing complete implementation 

import tkinter as tk

def analyze_audio():
    # Placeholder function to simulate analysis
    # Replace with actual speech emotion recognition code
    recognized_emotion = "Happy"  # Replace this with actual result
    result_label.config(text="Recognized Emotion: " + recognized_emotion)

# Create main window
root = tk.Tk()
root.title("Speech Emotion Recognition System")
root.geometry("400x300")

# Set background color
root.configure(bg="#007ACC")

# Load logo
logo_image = tk.PhotoImage(file="C:/Users/2/Documents/Speech Emotion Recognition Project/Final Speech Emotion Recognition Project/logo.png") 
logo_image = logo_image.subsample(2, 2)

# Title Label with Logo
title_frame = tk.Frame(root, bg="#007ACC")
title_frame.pack(pady=10)
logo_label = tk.Label(title_frame, image=logo_image, bg="#007ACC")
logo_label.grid(row=0, column=0, padx=5)
title_label = tk.Label(title_frame, text="Speech Emotion Recognition System", font=("Helvetica", 28, "bold"), fg="white", bg="#007ACC")
title_label.grid(row=0, column=1)

# Instructions Label
instructions_text = "Instructions:\n\n1. Click 'Record' to record your voice.\n2. Click 'Select File' to choose an audio file.\n3. Click 'Analyze Audio' to analyze the recorded or selected audio."
instructions_label = tk.Label(root, text=instructions_text, font=("Helvetica", 12), fg="white", bg="#007ACC", justify=tk.LEFT)
instructions_label.pack()

# Button for Audio Input
record_button = tk.Button(root, text="Record", command=analyze_audio, font=("Helvetica", 12), bg="#FF5733", fg="white", relief=tk.FLAT)
record_button.pack(pady=5)
select_button = tk.Button(root, text="Select File", command=analyze_audio, font=("Helvetica", 12), bg="#FF5733", fg="white", relief=tk.FLAT)
select_button.pack(pady=5)

# Text Display Area
result_label = tk.Label(root, text="", font=("Helvetica", 14, "italic"), fg="white", bg="#007ACC")
result_label.pack(pady=10)

# Analysis Button
analyze_button = tk.Button(root, text="Analyze Audio", command=analyze_audio, font=("Helvetica", 14), bg="#FFC300", fg="black", relief=tk.FLAT)
analyze_button.pack(pady=5)

# Run the application
root.mainloop()
