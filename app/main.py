import tkinter as tk
from tkinter import scrolledtext
from stt import speech_to_text
from chatbot import get_ai_response
from tts_helper import speak

def send_message():
    user_text = user_input.get()
    if not user_text.strip():
        return

    chat_log.insert(tk.END, f"Vous: {user_text}\n")
    user_input.delete(0, tk.END)

    if "stop" in user_text.lower():
        chat_log.insert(tk.END, "Arrêt du programme.\n")
        root.quit()
        return

    response = get_ai_response(user_text)
    chat_log.insert(tk.END, f"IA: {response}\n")
    speak(response)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Assistant Intelligent")

# Zone de texte pour afficher la conversation
chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='normal', height=20, width=50)
chat_log.pack(padx=10, pady=10)

# Champ de saisie pour l'utilisateur
user_input = tk.Entry(root, width=40)
user_input.pack(padx=10, pady=5)

# Bouton pour envoyer le message
send_button = tk.Button(root, text="Envoyer", command=send_message)
send_button.pack(pady=5)

# Lancer la boucle principale de l'interface
root.mainloop()