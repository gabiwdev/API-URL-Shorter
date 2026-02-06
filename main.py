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
    urls[key] = original_url
    return jsonify( {
    "short_url": f"http://localhost:5000/{key}"
} )

@app.route('/<key>')
def redirect_url(key):
    if key not in urls:
        return 'URL not found', 404
    return redirect(urls[key])



if __name__ == "__main__":
    app.run(debug=True)