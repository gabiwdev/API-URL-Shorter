from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_word():
    return 'Hello, Word!'

@app.route('/HTML')
def troll():
    return 'Caiu mauzão'

if __name__ == "__main__":
    app.run(debug=True)