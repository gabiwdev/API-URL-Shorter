from flask import Flask, request, jsonify, redirect
import random
import string
app = Flask(__name__)

urls = {}

def generate_key(length = 6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    original_url = data['url']
    
    key = generate_key()
    urls['key'] = original_url


@app.route('/')
def hello_word():
    return 'Hello, Word!'

@app.route('/HTML')
def troll():
    return 'Caiu mauzão'

if __name__ == "__main__":
    app.run(debug=True)