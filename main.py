from flask import Flask, request, jsonify, redirect, render_template
import random
import string
app = Flask(__name__)

urls = {}

def generate_key(length = 6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def shorten(url):
   
    key = generate_key()
    while key in urls:
        key = generate_key()

    urls[key] = url
    
    return f"http://127.0.0.1:5000/{key}"

@app.route('/<key>')
def redirect_url(key):
    if key not in urls:
        return 'URL not found', 404
    return redirect(urls[key])

@app.route('/', methods=['GET', 'POST'])
def home():
    url_encurtada = None

    if request.method == "POST":
        url_original = request.form.get('url')
        url_encurtada = shorten(url_original)
        if not url_original:
            return render_template('index.html', url_encurtada=url_encurtada)

    return render_template('index.html', url_encurtada=url_encurtada)



if __name__ == "__main__":
    app.run(debug=True)