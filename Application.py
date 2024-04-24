import tkinter as tk
from tkinter import filedialog
import pyaudio
import wave
import librosa
import numpy as np
import keras
from PIL import Image, ImageTk

# Constants for audio recording
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "C:/Users/2/Documents/Speech Emotion Recognition Project/Final Speech Emotion Recognition Project/recorded_audio.wav"

# Load the pre-trained model
model_path = 'C:/Users/2/Documents/Speech Emotion Recognition Project/Final Speech Emotion Recognition Project/model/Speech Emotion Recognition.h5'
loaded_model = keras.models.load_model(model_path)

def record_audio():
    # Record audio from microphone
    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return WAVE_OUTPUT_FILENAME

def analyze_audio():
    option = audio_option.get()
    if option == 'Record':
        audio_file = record_audio()
    elif option == 'Select File':
        audio_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])

    if audio_file:
        data, sampling_rate = librosa.load(audio_file)
        mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=40).T, axis=0)
        x = np.expand_dims(mfccs, axis=0)
        x = np.expand_dims(x, axis=2)
        predictions = loaded_model.predict_classes(x)
        result_label.config(text="Recognized Emotion: " + convert_class_to_emotion(predictions[0]), font=("Helvetica", 18, "bold"))

def convert_class_to_emotion(pred):
    label_conversion = {0: 'neutral',
                        1: 'calm',
                        2: 'happy',
                        3: 'sad',
                        4: 'angry',
                        5: 'fearful',
                        6: 'disgust',
                        7: 'surprised'}
    return label_conversion[pred]

# Create main window
root = tk.Tk()
root.title("Speech Emotion Recognition")
root.geometry("800x600")

# Set background color
root.configure(bg="#007ACC")

# Load logo
logo_image = Image.open("C:/Users/2/Documents/Speech Emotion Recognition Project/Final Speech Emotion Recognition Project/logo.png")
logo_image = logo_image.resize((800, 400), Image.ANTIALIAS)
logo_photo = ImageTk.PhotoImage(logo_image)

# Title Label with Logo
title_frame = tk.Frame(root, bg="#007ACC")
title_frame.pack(pady=10)
logo_label = tk.Label(title_frame, image=logo_photo, bg="#007ACC")
logo_label.grid(row=0, column=0, padx=5)
title_label = tk.Label(title_frame, text="Speech Emotion Recognition", font=("Helvetica", 28, "bold"), fg="white", bg="#007ACC")
title_label.grid(row=0, column=1)

# Instructions Label
instructions_text = "Instructions:\n\n1. Click 'Record' to record your voice.\n2. Click 'Select File' to choose an audio file.\n3. Click 'Analyze Audio' to analyze the recorded or selected audio."
instructions_label = tk.Label(root, text=instructions_text, font=("Helvetica", 16), fg="white", bg="#007ACC", justify=tk.LEFT)
instructions_label.pack()

# Add radio buttons for audio options
audio_option = tk.StringVar(value="Record")  # Initially set to 'Record'

record_button = tk.Radiobutton(root, text="Record", variable=audio_option, value="Record", font=("Helvetica", 20), bg="#007ACC", fg="white", activebackground="#FF5733", activeforeground="white", selectcolor="#FF5733", height=1, width=10, indicatoron=False)
record_button.pack(pady=5)

select_button = tk.Radiobutton(root, text="Select File", variable=audio_option, value="Select File", font=("Helvetica", 20), bg="#007ACC", fg="white", activebackground="#FF5733", activeforeground="white", selectcolor="#FF5733", height=1, width=10, indicatoron=False)
select_button.pack(pady=5)

# Text Display Area
result_label = tk.Label(root, text="", font=("Helvetica", 32, "bold"), fg="white", bg="#007ACC")
result_label.pack(pady=10)

# Analysis Button
analyze_button = tk.Button(root, text="Analyze Audio", command=analyze_audio, font=("Helvetica", 20), bg="#FFC300", fg="black", relief=tk.FLAT)
analyze_button.pack(pady=5)

# Run the application
root.mainloop()
