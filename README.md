Emotion-Based Music Player Using Python and Machine Learning
Introduction
This project uses machine learning techniques to detect emotions through video (facial expression), voice, or text inputs. Based on the detected emotion, the system plays music from a predefined database of songs categorized by different emotions such as happy, sad, angry, etc.

Features
Facial Expression Detection: Analyzes video feed and plays songs based on facial emotion.
Voice Emotion Detection: Analyzes voice input to detect emotion and select music.
Text Emotion Detection: Analyzes written text to understand the emotion and play corresponding music.
Project Structure
bash
Copy code
EMP_project/
├── Database/                 # Contains folders with songs for different emotions
│   ├── angry/
│   ├── happy/
│   ├── neutral/
│   ├── sad/
│   └── surprised/
├── src/                      # Contains the main scripts for emotion detection
│   ├── video.py              # Script for video-based emotion detection
│   ├── voice.py              # Script for voice-based emotion detection
│   └── text.py               # Script for text-based emotion detection
├── haarcascade_frontalface_default.xml  # Pre-trained model for face detection
├── trained_emoclassifier.xml  # Pre-trained emotion classification model
├── README.md                 # This file
├── requirements.txt          # Required Python packages
└── Update_Model.py           # Script to update the emotion classifier
Requirements
Before you start, make sure you have the following installed:

Python 3.11 (or a compatible version)
pip: Python package installer
Install Dependencies
To install all the required Python packages, run:

bash
Copy code
pip install -r requirements.txt
How to Use the Project
Step 1: Set Up the Song Database
Add Songs: Inside the Database folder, there are subfolders for different emotions (happy, sad, angry, etc.). Each folder should contain songs that reflect that emotion.
You can modify or add songs to these subfolders as per your preference.
Step 2: Video-Based Emotion Detection
To detect emotion through facial expressions and play music:

Open a terminal or command prompt.
Navigate to the src folder:
bash
Copy code
cd src
Run the video-based emotion detection script:
bash
Copy code
python video.py
Enter the song database when prompted. For example, if you want to use songs from the happy folder, type happy.
Step 3: Voice-Based Emotion Detection
To detect emotion through voice input and play music:

Open a terminal or command prompt.
Navigate to the src folder:
bash
Copy code
cd src
Run the voice-based emotion detection script:
bash
Copy code
python voice.py
Enter the song database when prompted. For example, type sad to use the sad folder.
Step 4: Text-Based Emotion Detection
To detect emotion through written text and play music:

Open a terminal or command prompt.
Navigate to the src folder:
bash
Copy code
cd src
Run the text-based emotion detection script:
bash
Copy code
python text.py
Enter the song database when prompted.
Example Commands
Here's how to run the project for video-based emotion detection:

bash
Copy code
cd src
python video.py
# Enter the song database name when prompted (e.g., happy)
Updating the Emotion Model
If you need to update the emotion classification model:

Open the Update_Model.py script and follow the instructions inside to retrain the model with new data.
Run the script to update the model:
bash
Copy code
python Update_Model.py
Notes
The emotion detection uses pre-trained models for face detection and emotion classification.
You can add or replace songs in the Database folders to change the music played for each emotion.
For optimal performance, ensure that your Python environment has all the required dependencies installed.
Acknowledgments
OpenCV: Used for video-based face and emotion detection.
Machine Learning Models: Pre-trained models used for emotion classification.


