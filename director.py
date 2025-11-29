# director.py
import ollama
import json

def get_shot_list(story_text):
    """
    Takes a full story and returns a 'shot_list' (a Python list of objects).
    """
    system_prompt = """
    You are a movie director. Read the following story and break it down
    into a list of distinct visual scenes.
    For EACH scene, you MUST provide:
    1. A short 'visual_prompt' for an AI image generator (Stable Diffusion).
    2. The exact 'narration_text' from the story for that scene.
    You MUST respond with ONLY a valid JSON array of objects.
    Do not add any text before or after the JSON.
    """
    
    print(" Calling the AI Director (Ollama)...")
    
    try:
        response = ollama.chat(
            model='phi3:mini',
            options={"num_gpu": 0},
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': story_text}
            ]
        )

        # Try to extract the text content from common response shapes
        raw = None
        if isinstance(response, dict):
            msg = response.get('message')
            if isinstance(msg, dict) and 'content' in msg:
                raw = msg['content']
            elif 'content' in response:
                raw = response['content']
            else:
                raw = str(response)
        else:
            # fallback to attribute access or str()
            try:
                raw = response.message.content
            except Exception:
                raw = str(response)

        if raw is None:
            raw = ''

        raw = str(raw).strip()
        print("Director raw response (first 500 chars):", raw[:500])

        # Remove common wrappers (code fences, leading text)
        if raw.startswith("```"):
            parts = raw.split("```")
            if len(parts) >= 2:
                # If response was like ```json\n[ ... ]\n```
                raw = parts[-1].strip()

        if raw.lower().startswith("here"):
            parts = raw.split("\n", 1)
            if len(parts) > 1:
                raw = parts[1].strip()

        if raw.startswith("```json"):
            raw = raw.replace("```json", "").strip()
            if raw.endswith("```"):
                raw = raw[:-3].strip()

        if not raw:
            print("Error in Director: Received empty content from AI.")
            return None

        # Attempt normal JSON parse first
        try:
            shot_list = json.loads(raw)
            print("Director finished. Shot list created.")
            return shot_list
        except json.JSONDecodeError:
            # Try to salvage a JSON array inside the text
            start = raw.find('[')
            end = raw.rfind(']')
            if start != -1 and end != -1 and end > start:
                candidate = raw[start:end+1]
                try:
                    shot_list = json.loads(candidate)
                    print("Director finished (extracted array). Shot list created.")
                    return shot_list
                except Exception as e2:
                    print(f"Error in Director: JSON decoding failed after extracting array. Error: {e2}")
                    print("Raw response was:", repr(raw))
                    return None
            else:
                print("Error in Director: JSON decoding failed and no JSON array found in response.")
                print("Raw response was:", repr(raw))
                return None

    except Exception as e:
        print(f"Error in Director: {e}")
        return None

# This part allows you to still run this file directly for testing
if __name__ == "__main__":
    test_story = "A knight walked. A dragon roared."
    shots = get_shot_list(test_story)
    if shots:
        print("\n--- TEST RUN SUCCESS ---")
        print(json.dumps(shots, indent=2))