import whisper
import sounddevice as sd
import numpy as np
import tempfile
import os
import wave


# Charger Whisper
model = whisper.load_model("small")

def record_audio(filename, duration=5, fs=44100):
    print("Parle maintenant...")
    # Enregistrement audio
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Attendre la fin de l'enregistrement
    wave_file = wave.open(filename, 'wb')
    wave_file.setnchannels(1)
    wave_file.setsampwidth(2)  # 16 bits
    wave_file.setframerate(fs)
    wave_file.writeframes(audio_data.tobytes())
    wave_file.close()
    print("Enregistrement terminé.")

def speech_to_text(filename):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
        record_audio(temp_file.name, duration=5)
        print("Transcription en cours...")
        result = model.transcribe(temp_file.name)
        os.remove(temp_file.name)  # Supprimer le fichier temporaire
        return result['text']