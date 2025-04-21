FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    ninja-build \
    git \
    wget \
    curl \
    libopenblas-dev \
    liblapack-dev \
    libsndfile1 \
    portaudio19-dev \
    python3-dev \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, wheel
RUN pip install --upgrade pip setuptools wheel

# Optional: create and use a virtualenv (good practice)
WORKDIR /app

# Copy all project files into the container
COPY . /app
COPY requirements.txt .

RUN pip install -r requirements.txt

# Lancer l'assistant virtuel
CMD ["python", "app/main.py"]