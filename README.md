<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    Moodify: AI-Powered Emotion-Based Music
</head>
<body>
    <h1>Project Overview</h1>
    <p>This project is an AI-based music player that uses facial expressions to detect the user's emotions and plays music accordingly. It leverages machine learning techniques and OpenCV for facial expression recognition.
      The Emotion-Based Music Player uses a pre-trained model to classify emotions such as happy, sad, angry, and neutral. Based on the detected emotion, the app suggests and plays music that aligns with the mood. The following guide walks through setting up the environment, running the project, and understanding the code..</p>
    <h2>Prerequisites</h2>
    <p>Before running the project, ensure you have the following installed:</p>
    <ul>
        <li><strong>Anaconda:</strong> For managing packages and environments</li>
        <li><strong>Git:</strong> For cloning the repository</li>
    </ul>
    <h2>Setup and Implementation</h2>
    <h3>1. Clone the Repository</h3>
    <p>Open your terminal or command prompt and run the following command to clone the repository:</p>
    <pre><code>git clone -repository_url- </code></pre>
    <p>Navigate to the project directory:</p>
    <pre><code>cd <repository_directory></code></pre>
    <h3>2. Create a Conda Environment</h3>
    <p>Create a virtual environment using Conda:</p>
    <pre><code>conda create --name env_name python=3.x</code></pre>
    <p>Activate the environment:</p>
    <pre><code>conda activate env_name</code></pre>
    <h3>3. Install Dependencies</h3>
    <p>Since the <code>requirements.txt</code> file is not available, install the required packages manually. Use the following command to install packages as needed:</p>
    <pre><code>pip install package_name</code></pre>
    <p>Here are some common libraries you might need:</p>
    <ul>
        <li><code>numpy</code></li>
        <li><code>opencv-python</code></li>
        <li><code>pydub</code></li>
        <li><code>speechrecognition</code></li>
        <li><code>flask</code></li>
    </ul>
    <h3>4. Using the Project</h3>
    <p>The project includes databases that contain the songs. You can run the scripts in the <code>src</code> directory:</p>
    <pre><code>cd src</code></pre>
    <ul>
        <li>For video processing, run:</li>
        <pre><code>python video.py</code></pre>
        <p>When prompted, provide the name of the database (e.g., <strong>happy</strong>) you wish to use.</p>    
        <li>For voice processing, run:</li>
        <pre><code>python voice.py</code></pre>
        <p>Again, provide the name of the database when prompted.</p>
        <li>For text processing, run:</li>
        <pre><code>python text.py</code></pre>
        <p>Follow the prompts as necessary.</p>
    </ul>
    <h2>Outputs</h2>
    <p>The outputs of the project will include playing songs based on the selected database and modality.</p>
    <h2>Acknowledgements</h2>
    <p>Author: Gajulapalli Naga Vyshnavi<br>
    Contact: <a href="mailto:nvyshnavi36@gmail.com">nvyshnavi@gmail.com </a><br>
    For any inquiries, feel free to reach out via the contact information provided.</p>
</body>
</html>
