from flask import Flask, request, redirect, render_template
import random
import string
app = Flask(__name__)

urls = {}

def generate_key(length = 6):
    """
    Gera uma key em formato de string e a retorna
    
    :param length: Tamanho da key
    :return: key
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def shorten(url):
    """
    Recebe uma URL e gera uma chave única para ela.
    
    :param url: URL original a ser encurtada
    :return: URL Encurtada
    """
    key = generate_key()
    while key in urls:
        key = generate_key()

    urls[key] = url
    
    return f"http://127.0.0.1:5000/{key}"

@app.route('/<key>')
def redirect_url(key):
    """
    Recebe uma key, redirecionando a pessoa para o site ligado àquela key.

    Se a key não existir, um erro será exibido.
    
    :param key: key da URL
    :return: Redirect ao site da key
    """

    if key not in urls:
        return 'URL not found', 404
    return redirect(urls[key])

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Função para renderizar o html e o processo de retornar a URL encurtada ao HTML.

    Se o método for post e uma URL válida for enviada, 
    retorna a URL encurtada para a exibição no HTML
    """
    url_encurtada = None

    if request.method == "POST":
        url_original = request.form.get('url')
        
        if not url_original:
            return render_template('index.html', url_encurtada=url_encurtada)
        
        url_encurtada = shorten(url_original)
        

    return render_template('index.html', url_encurtada=url_encurtada)

if __name__ == "__main__":
    app.run(debug=True)