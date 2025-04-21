# Mira Project

Mira is an intelligent virtual assistant designed to provide seamless interaction through speech recognition, natural language processing, and text-to-speech synthesis. This project leverages state-of-the-art AI models to enable real-time communication with users.

## Features
- **Speech-to-Text (STT):** Converts spoken language into text using advanced speech recognition models.
- **Natural Language Processing (NLP):** Processes user input and generates intelligent responses using AI-powered models like Mistral or Llama.
- **Text-to-Speech (TTS):** Converts AI-generated responses into natural-sounding speech using Coqui TTS.
- **Graphical User Interface (GUI):** A user-friendly interface built with Tkinter for easy interaction.
- **Dockerized Environment:** Fully containerized for easy deployment and reproducibility.

## Technologies Used
- **Python:** Core programming language for the project.
- **Coqui TTS:** For text-to-speech synthesis.
- **Llama/Mistral Models:** For natural language understanding and response generation.
- **Tkinter:** For building the graphical user interface.
- **Docker:** For containerization and deployment.

## Installation and Usage

### Prerequisites
- Docker and Docker Compose installed on your system.
- Need to download **mistral-7b-instruct-v0.2.Q4_K_M.gguf** file from https://huggingface.co
```bash
git clone https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF
```
Then copy it to models directory

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/username/mira-project.git
   cd mira-project
   ```

2. Build the Docker image:
   ```bash
   docker-compose build
   ```

3. Start the application:
   ```bash
   docker-compose up
   ```

4. Interact with the assistant through the GUI.

## Project Structure
```
Mira-Project/
├── app/
│   ├── main.py          # Main application script
│   ├── stt.py           # Speech-to-text functionality
│   ├── chatbot.py       # AI response generation
│   ├── tts_helper.py    # Text-to-speech functionality
├── models/              # Directory for AI models
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose configuration
├── requirements.txt     # Python dependencies
├── LICENSE              # License file
└── README.md            # Project documentation
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.
