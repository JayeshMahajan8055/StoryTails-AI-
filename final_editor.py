import ffmpeg
import os
import json

ASSET_FOLDER = "project_assets"
FINAL_MOVIE_FILE = "FINAL_STORY_MOVIE.mp4"

# --- 1. Load the Master Shot List ---
try:
    with open('master_shot_list.json', 'r') as f:
        shot_list = json.load(f)
except FileNotFoundError:
    print("Error: 'master_shot_list.json' not found.")
    print("This file is needed to know the correct scene order.")
    exit()

print(f"Loaded {len(shot_list)} scenes. Starting final edit...")

# --- STAGE 1: Combine Audio & Video for Each Scene ---

temp_scene_files = [] # This will hold the paths to our temp videos
temp_folder = "temp_scenes"
os.makedirs(temp_folder, exist_ok=True)

print(f"\n--- STAGE 1: Merging audio and video for {len(shot_list)} scenes ---")

for i in range(len(shot_list)):
    scene_number = f"{i+1:02d}"

    video_file = os.path.join(ASSET_FOLDER, f"scene_{scene_number}_video.mp4")
    audio_file = os.path.join(ASSET_FOLDER, f"scene_{scene_number}_audio.wav")
    temp_output_file = os.path.join(temp_folder, f"temp_scene_{scene_number}.mp4")

    # Check if both files exist
    if not os.path.exists(video_file) or not os.path.exists(audio_file):
        print(f"Warning: Missing files for Scene {scene_number}. Skipping.")
        continue

    print(f"Combining Scene {scene_number}...")
    try:
        # Load the streams
        video_stream = ffmpeg.input(video_file)
        audio_stream = ffmpeg.input(audio_file)

        # Combine them
        ffmpeg.output(
            video_stream, 
            audio_stream, 
            temp_output_file, 
            vcodec='copy',  # Copy video codec (fast)
            acodec='aac',   # Re-encode audio to standard AAC
            shortest=None   # Use the shortest input (should be the video)
        ).run(overwrite_output=True, quiet=True)

        temp_scene_files.append(temp_output_file)

    except Exception as e:
        print(f"Error combining Scene {scene_number}: {e}")

print(f" Stage 1 Complete. {len(temp_scene_files)} scenes prepared.")

# --- STAGE 2: Concatenate All Scenes into Final Movie ---

if not temp_scene_files:
    print("Error: No temporary scenes were created. Cannot build final movie.")
    exit()

print("\n--- STAGE 2: Stitching all scenes into the final movie ---")

try:
    # Create a text file for ffmpeg listing all the temp files to join
    list_file_path = os.path.join(temp_folder, "concat_list.txt")
    with open(list_file_path, 'w') as f:
        for file_path in temp_scene_files:
            f.write(f"file '{os.path.abspath(file_path)}'\n")

    # Use ffmpeg's 'concat' demuxer
    (
        ffmpeg
        .input(list_file_path, format='concat', safe=0)
        .output(FINAL_MOVIE_FILE, c='copy')
        .run(overwrite_output=True, quiet=True)
    )

    print("\n---  PROJECT COMPLETE!  ---")
    print(f"Your final movie has been created: {FINAL_MOVIE_FILE}")

except Exception as e:
    print(f"Error during final concatenation: {e}")

