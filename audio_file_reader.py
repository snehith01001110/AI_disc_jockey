import os
import librosa
from tkinter import filedialog
from tkinter import Tk

def read_audio_files_from_folder(folder_path):
    audio_data = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.flac'):
            file_path = os.path.join(folder_path, filename)
            audio, sr = librosa.load(file_path, sr=None)
            audio_data[filename] = {'audio': audio, 'sample_rate': sr}
    return audio_data

def select_folder_and_read_files():
    root = Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory()
    if folder_path:
        return read_audio_files_from_folder(folder_path)
    else:
        return None

if __name__ == "__main__":
    audio_data = select_folder_and_read_files()
    if audio_data:
        for filename, data in audio_data.items():
            print(f"Read {filename} with sample rate {data['sample_rate']}")
