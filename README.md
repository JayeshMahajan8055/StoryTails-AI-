🎬 StoryTails – AI Text-to-Video Story Generator

Transform written stories into AI-generated animated videos with scene extraction, visual generation, and synchronized narration.

StoryTails is an advanced multimodal AI system that converts text into full animated sequences using LLM-driven scene extraction, diffusion-based visual generation, and neural text-to-speech models—all combined using FFmpeg.

🚀 Key Features

✔ Converts text stories into animated videos
✔ Llama 3 for intelligent scene breakdown & narrative understanding
✔ SDXL and Stable Video Diffusion for high-quality visual scene generation
✔ Coqui XTTS for TTS narration (multilingual support)
✔ FFmpeg-based audio–video synchronization
✔ Streamlit UI for interaction, progress tracking, and video preview
✔ Maintains visual consistency of characters across frames
✔ Optimized prompt designs for coherent storytelling

🧠 AI Pipeline Overview
flowchart LR
    A[Story Text Input] --> B[Scene Extraction (Llama 3)]
    B --> C[Image/Video Generation (SDXL/Stable VD)]
    B --> D[Speech Synthesis (Coqui XTTS)]
    C --> E[Video Assembly (FFmpeg)]
    D --> E
    E --> F[Final Video Output]

🛠️ Tech Stack
Component	Technology
Scene Extraction	Llama 3
Image/Video Generation	SDXL, Stable Video Diffusion
Voice Generation	Coqui XTTS
Synchronization	FFmpeg
Interface	Streamlit
Language	Python
📂 Project Structure
StoryTails/
├── main.py                  # Streamlit interface or pipeline starter
├── director.py              # Scene extraction & script logic
├── narrator.py              # Speech synthesis (XTTS)
├── final_editor.py          # FFmpeg-based video composition
├── project_be.py            # Backend flow management
├── temp_scenes/             # Intermediate scene data
├── output/                  # Final generated videos (ignored via .gitignore)
├── .gitignore
└── README.md

📦 Installation
git clone https://github.com/JayeshMahajan8055/StoryTails-AI-.git
cd StoryTails-AI-
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # Mac/Linux
pip install -r requirements.txt

🔐 Environment Setup

Create a .env file:

OPENAI_API_KEY=your_openai_key
COQUI_API_KEY=your_coqui_key


Ensure these keys are active and not committed to Git.

▶️ Usage
Run with Streamlit UI
streamlit run main.py

Or run full pipeline manually:
python main.py


Then:

📝 Write your story → 📸 Scenes generated → 🎙 Narration added → 🎞 Final video rendered.

🧪 Example Story Input
Once upon a time in a futuristic city, a young girl named Aira discovered 
a glowing AI cube that spoke in an ancient language...


Output:
📌 LLM extracts scenes → 🎨 AI generates visuals → 🔊 XTTS voice narration is added → 🎬 Assembled into animated video.

🚨 Limitations

❗ High GPU demand (diffusion models)
❗ Frame coherence may vary depending on prompt quality
❗ TTS timing optimization still experimental
❗ Processing takes time for long stories

🧩 Future Improvements

🔹 Real-time preview of generated frames
🔹 Character memory & style locking
🔹 Support for interactive branching stories
🔹 Web deployment (HuggingFace, GPU Cloud)
🔹 Subtitle auto-generation

🤝 Contribution

Contributions are welcome!

Fork this repo

Create a new branch: feature/my-feature

Commit your enhancements

Open a Pull Request 🚀

📬 Contact

Jayesh Mahajan
AI/ML Engineer | Generative AI | Multimodal Systems
📍 Pune, India
🔗 GitHub: JayeshMahajan8055

💼 LinkedIn: Add your profile link here
📧 Email: Your email here

⭐ Support

If you like this project, please consider starring ⭐ this repo to support further development.

“Storytelling is humanity’s oldest art — StoryTails brings it to life with AI.” 🚀

🏁 End of README

Now:

✔ Commit and push this README.md
✔ Update GitHub description (you already have the perfect one)
✔ Add tags
