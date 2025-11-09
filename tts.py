# tts.py — Convert news summaries into audio files

from gtts import gTTS
import os
import uuid

def text_to_speech(text, lang="en"):
    """Convert text to speech and save as mp3 file"""
    if not text:
        return None
    
    filename = f"audio_{uuid.uuid4().hex}.mp3"
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    return filename

if __name__ == "__main__":
    file = text_to_speech("Hello! This is your AI news assistant.")
    print(f"Saved audio to {file}")
