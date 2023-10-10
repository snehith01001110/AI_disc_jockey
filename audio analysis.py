import librosa
import numpy as np

def analyze_tempo(audio, sr):
    onset_env = librosa.onset.onset_strength(y=audio, sr=sr)
    tempo, _ = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)
    return tempo

def analyze_pitch(audio, sr):
    pitches, magnitudes = librosa.core.piptrack(y=audio, sr=sr)
    pitch = []
    for t in range(pitches.shape[1]):
        index = magnitudes[:, t].argmax()
        pitch.append(pitches[index, t])
    pitch = np.array(pitch)
    pitch = pitch[pitch > 0]  # remove zero entries
    mean_pitch = np.mean(pitch)
    return mean_pitch

def analyze_volume(audio):
    return librosa.feature.rms(y=audio)[0]

def analyze_audio(audio, sr):
    tempo = analyze_tempo(audio, sr)
    pitch = analyze_pitch(audio, sr)
    volume = analyze_volume(audio)
    return {'tempo': tempo, 'pitch': pitch, 'volume': np.mean(volume)}

if __name__ == "__main__":
    # For testing purposes, you can read an audio file using the previous component
    # and then pass the audio data and sample rate to this component.
    # For example:
    audio, sr = librosa.load("/Users/snehithnayak/Desktop/AI_DJ/for_all_the_dogs/01-drake-virginia_beach-proper.flac", sr=None)
    analysis = analyze_audio(audio, sr)
    print(analysis)
    pass
