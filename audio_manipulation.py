import librosa
import numpy as np
import soundfile as sf
from scipy.signal import resample

def change_tempo(audio, sr, tempo_ratio):
    hop_length = 512
    stft = librosa.stft(audio, hop_length=hop_length)
    stft_stretch = librosa.core.phase_vocoder(stft, rate=tempo_ratio, hop_length=hop_length)
    audio = librosa.istft(stft_stretch, hop_length=hop_length)
    return audio

def change_pitch(audio, sr, n_steps):
    # Resampling to change pitch
    new_sr = sr * (2.0 ** (n_steps / 12.0))
    num_samples = int(audio.shape[0] * (new_sr / sr))
    audio = resample(audio, num_samples)
    return audio

def change_volume(audio, db_change):
    audio = audio * (10 ** (db_change / 20.0))
    return audio

def manipulate_audio(audio, sr, tempo_ratio=1.0, n_steps=0, db_change=0):
    audio = change_tempo(audio, sr, tempo_ratio)
    audio = change_pitch(audio, sr, n_steps)
    audio = change_volume(audio, db_change)
    return audio

def save_audio(audio, sr, path):
    sf.write(path, audio, sr)

if __name__ == "__main__":
    # For testing purposes, you can read an audio file using the first component
    # and then pass the audio data and sample rate to this component.
    # For example:
    audio, sr = librosa.load("/Users/snehithnayak/Desktop/AI_DJ/for_all_the_dogs/01-drake-virginia_beach-proper.flac", sr=None)
    manipulated_audio = manipulate_audio(audio, sr, tempo_ratio=1.2, n_steps=2, db_change=5)
    save_audio(manipulated_audio, sr, "/Users/snehithnayak/Desktop/AI_DJ/manipulated_audio.flac")
    pass
