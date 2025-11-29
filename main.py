# main.py
import os
import json

# Import the functions from your other scripts
try:
    from director import get_shot_list
    from narrator import generate_audio_for_scene
except ImportError as e:
    print(f"Error: Could not import functions. {e}")
    print("Make sure 'director.py' and 'narrator.py' are in the same folder.")
    exit()

# --- 1. Define Your Inputs ---

# !!! CHANGE THESE !!!
YOUR_VOICE_SAMPLE = "my_voice.wav" # Change this to your .wav file

YOUR_STORY = """
A young knight named Alistair, armored in shining silver, 
walked nervously through the Whispering Woods. The trees were 
so dense, they blocked out the sun, creating an eerie twilight. 
Suddenly, he heard a snap of a twig. He drew his sword, 
its steel gleaming faintly. "Who's there?" he called out. 
From the shadows, a pair of glowing red eyes appeared, 
and a low growl echoed. A massive black wolf emerged, 
baring its fangs. Alistair stood his ground, heart pounding.
"""

# --- 2. Run the Director ---
shot_list = get_shot_list(YOUR_STORY)

if not shot_list:
    print("Halting: Director failed to create a shot list.")
    exit()

# Save the shot list so we can see it
with open('master_shot_list.json', 'w') as f:
    json.dump(shot_list, f, indent=2)
print("Master shot list saved to 'master_shot_list.json'")

# --- 3. Run the Narrator (in a loop) ---
print("\n--- Starting Audio Generation Loop ---")

# Create a folder to hold all our assets
output_folder = "project_assets"
os.makedirs(output_folder, exist_ok=True)

successful_scenes = 0
for i, scene in enumerate(shot_list):
    scene_number = f"{i+1:02d}" # Formats as "01", "02", etc.

    scene_text = scene.get('narration_text', '')
    if not scene_text:
        print(f"SKIPPING Scene {scene_number}: No 'narration_text' found.")
        continue

    output_filename = os.path.join(output_folder, f"scene_{scene_number}_audio.wav")

    success = generate_audio_for_scene(
        scene_text=scene_text,
        voice_sample_file=YOUR_VOICE_SAMPLE,
        output_filename=output_filename
    )

    if success:
        successful_scenes += 1

print(f"\n--- Audio Generation Complete ---")
print(f"Successfully generated {successful_scenes} audio files in the '{output_folder}' folder.")