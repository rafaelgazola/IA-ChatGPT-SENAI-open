from agno.models.openai import OpenAIChat
from agno.agent import Agent
from dotenv import load_dotenv
from flask import Flask,jsonify,request
from flask_cors import CORS 


# Lendo a chave da API
load_dotenv()

#
app = Flask(__name__)
CORS(app)

# Criando o Agente
agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um agente prestativo do Hotel Travesseiro Nervoso, slogan: Aqui, até a Insonia Dorme, que auxilia hóspedes a encontrarem o quarto Ideal. Quartos : Standard R$400, Quartos: Deluxe R$600, Quartos: Luxo R$1600. Serviços Oferecidos no Hotel: Café da Manhã, academia, restaurante, piscina, serviço de quarto, estacionamento",
    markdown=True
)

@app.route("/",methods=['GET'])
def testar_agente():
    return jsonify({"Mensagem":"Agente OnLine!!!!"})

@app.route("/perguntar",methods=['POST'])
def enviar_pergunta():
    dados = request.get_json()
    pergunta = dados['pergunta']
    resposta =agente.run(pergunta)
    return jsonify({"mensagem":resposta.content})



if __name__ == '__main__':
    app.run(port=8000,host="0.0.0.0",debug=True)