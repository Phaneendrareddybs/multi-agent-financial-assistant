# agents/voice_agent.py

import whisper
from gtts import gTTS
import os
import uuid

def speech_to_text(audio_file_path):
    """
    Convert audio to text using Whisper STT.
    The model is loaded inside the function to avoid global torch crashes.
    """
    model = whisper.load_model("base")
    result = model.transcribe(audio_file_path)
    return result["text"]

def text_to_speech(text, output_path=None):
    """
    Convert text to speech using gTTS and save as an MP3 file.
    Returns the path to the generated file.
    """
    if output_path is None:
        output_path = f"tts_{uuid.uuid4().hex[:6]}.mp3"
    
    tts = gTTS(text)
    tts.save(output_path)

    # Optional playback (safe for Windows)
    try:
        os.system(f"start {output_path}")  # Windows
        # os.system(f"afplay {output_path}")  # macOS
        # os.system(f"mpg321 {output_path}")  # Linux
    except Exception as e:
        print(f"Error playing audio: {e}")

    return output_path
