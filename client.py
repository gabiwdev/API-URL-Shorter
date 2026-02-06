import requests

url_longa = "cole-url-aqui"

response = requests.post(
    "http://127.0.0.1:5000/shorten", json={"url": url_longa}
)

print(response.json())