# narrator.py
import os
from TTS.api import TTS

# --- Initialize the Model ONCE ---
# This is slow, so we do it when the file is first imported
print("Loading Coqui XTTS model... (This will download the model the first time)...")
try:
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True).to("cpu")
    print(" Narrator Model Loaded.")
except Exception as e:
    print(f"Failed to load TTS model: {e}")
    tts = None

def generate_audio_for_scene(scene_text, voice_sample_file, output_filename):
    """
    Takes scene text and generates a .wav file with the cloned voice.
    """
    if tts is None:
        print("Error: TTS model is not loaded. Cannot generate audio.")
        return False
        
    if not os.path.exists(voice_sample_file):
        print(f"Error: The speaker file was not found: {voice_sample_file}")
        return False

    print(f" Narrating: '{scene_text[:30]}...' -> {output_filename}")
    
    try:
        tts.tts_to_file(
            text=scene_text,
            speaker_wav=voice_sample_file,
            language="en",
            file_path=output_filename
        )
        return True
    except Exception as e:
        print(f"An error occurred during TTS generation: {e}")
        return False

# This part allows you to still run this file directly for testing
if __name__ == "__main__":
    if tts:
        print("\n--- TEST RUN STARTING ---")
        generate_audio_for_scene(
            scene_text="This is a test of the narrator function.",
            voice_sample_file="my_voice.wav", # CHANGE this if your file is named differently
            output_filename="test_audio.wav"
        )
        print("--- TEST RUN COMPLETE ---")