from flask import Flask, request, jsonify, send_file
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from gtts import gTTS
import os
import torch

app = Flask(__name__)


# Initialize the tokenizer and model
model_name = "facebook/mbart-large-50-many-to-many-mmt"
tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)
tokenizer.src_lang = "en_XX"
target_lang = "ur_PK"

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text')

    # Tokenize and translate
    encoded_input = tokenizer(text, return_tensors="pt")
    generated_tokens = model.generate(encoded_input['input_ids'], forced_bos_token_id=tokenizer.lang_code_to_id[target_lang])
    translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]

    # Convert translated text to speech
    tts = gTTS(translated_text, lang='ur')
    audio_file = "translated_speech.mp3"
    tts.save(audio_file)

    return send_file(audio_file, as_attachment=True)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
