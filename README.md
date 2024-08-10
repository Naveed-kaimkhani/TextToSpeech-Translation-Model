# TextToSpeech-Translation-Model
A Flask-based API for translating English text to Urdu and converting the translated text into speech using MBart and gTTS. This API enables seamless translation and real-time audio output.

## Features
Text Translation: Translates English text to Urdu using MBart.
Speech Synthesis: Converts translated Urdu text into speech using gTTS.
REST API: Simple API endpoints for translation and speech synthesis.

## Prerequisites
Python 3.6+

## Install required Python packages:

bash
Copy code
pip install Flask transformers gtts torch
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/TextToSpeech-Translation-Model.git
cd TextToSpeech-Translation-API
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask application:

bash
Copy code
python app.py
The API will be accessible at http://0.0.0.0:5000/.

## Usage
Translation and Speech Synthesis
Endpoint: /translate

## Method: POST

Request Body:

json
Copy code
{
  "text": "Your text here"
}
Response: Returns an MP3 file of the translated speech.

Example Request
bash
Copy code
curl -X POST http://0.0.0.0:5000/translate -H "Content-Type: application/json" -d '{"text":"Hello, World!"}' --output translated_speech.mp3
Hello World
Endpoint: /hello
Method: GET
Response: Hello, World!
License
This project is licensed under the MIT License.

## Contributing
Feel free to submit issues or pull requests for improvements and new features.
