from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "57a891c9d85793050a25d247f4451ef7"  # Substitua pela sua chave de API

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/clima', methods=['POST'])
def obter_clima():
    cidade = request.form['cidade']
    
    # Monta a URL de requisição da API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric"
    
    # Faz a requisição para a API
    resposta = requests.get(url)
    dados_clima = resposta.json()

    # Verifica se a cidade foi encontrada
    if resposta.status_code == 200:
        temperatura = dados_clima['main']['temp']
        descricao = dados_clima['weather'][0]['description']
        umidade = dados_clima['main']['humidity']

        return render_template('index.html', cidade=cidade, temperatura=temperatura, descricao=descricao, umidade=umidade)
    else:
        return render_template('index.html', erro="Cidade não encontrada.")

if __name__ == '__main__':
    app.run(debug=True)
