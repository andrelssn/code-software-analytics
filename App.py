from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Fazer a requisição para a API
    response_racao = requests.get(url_racao)
    response_suplementos = requests.get(url_suplementos)
    dados_racao = response_racao.json()
    dados_suplementos = response_suplementos.json()

    # Extrair os dados necessários da resposta da API
    dias_da_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    quantidade_racao = [dados_racao[dia] for dia in dias_da_semana]
    quantidade_suplementos = [dados_suplementos[dia] for dia in dias_da_semana]

    # Passar os dados para o template
    return render_template('index.html', dias_da_semana=dias_da_semana, quantidade_racao=quantidade_racao, quantidade_suplementos=quantidade_suplementos)

if __name__ == '__main__':
    app.run(debug=True)

# APLICAÇÃO SEM CONEXÃO COM O BANCO DE DADOS