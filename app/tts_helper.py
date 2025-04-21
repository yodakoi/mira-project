import os
from TTS.api import TTS

# Charger le modèle vocal de coqui
tts_model = TTS(model_name="tts_models/en/ljspeech/glow-tts", progress_bar=False).to("cpu")

def speak(text):
    tts_model.tts_to_file(text=text, file_path="response.wav")
    os.system("aplay response.wav")  # Joue le fichier audio