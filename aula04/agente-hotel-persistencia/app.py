from agno.models.openai import OpenAIChat
from agno.agent import Agent
from dotenv import load_dotenv
from flask import Flask,jsonify,request,send_from_directory
from flask_cors import CORS 
from supabase import create_client
import os

# Lendo a chave da API
load_dotenv()

#Criar uma conexao com o banco de dados
supabase = create_client(os.getenv("SUPABASE_URL"),os.getenv("SUPABASE_KEY"))
app = Flask(__name__)
CORS(app)

# Criando o Agente
agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um agente prestativo do Hotel Travesseiro Nervoso, slogan: Aqui, até a Insonia Dorme, que auxilia hóspedes a encontrarem o quarto Ideal. Quartos : Standard R$400, Quartos: Deluxe R$600, Quartos: Luxo R$1000. Serviços Oferecidos no Hotel: Café da Manhã, academia, restaurante, piscina, serviço de quarto, estacionamento",
    markdown=False
)

@app.route("/",methods=['GET'])
def testar_agente():
    return app.send_static_file("index.html")

@app.route("/imagens/<path:nome_arquivo>",methods=['GET'])
def servir_imagem(nome_arquivo):
    return send_from_directory(os.path.join(app.root_path, "imagens"), nome_arquivo)

@app.route("/perguntar",methods=['POST'])
def enviar_pergunta():
    dados = request.get_json()
    pergunta = dados['pergunta']
    resposta =agente.run(pergunta)
    return jsonify({"mensagem":resposta.content})

#rota usada pelo chat do site (static/index.html)
@app.route("/agente",methods=['POST'])
def agente_responder():
    dados = request.get_json()
    pergunta = dados['pergunta']
    resposta = agente.run(pergunta)
    return jsonify({"resposta":resposta.content})


#para reservar a insrir dados no banco
@app.route("/reserva",methods=['POST'])
def criar_reserva():
    dados = request.get_json()
    supabase.table("reservas").insert(dados).execute()
    return jsonify({"mensagem":"Reserva feita com sucesso"})

#rota usada pelo formulário de reserva do site (static/index.html)
@app.route("/reservas",methods=['POST'])
def criar_reserva_site():
    dados = request.get_json()
    supabase.table("reservas").insert(dados).execute()
    return jsonify({"mensagem":"Reserva feita com sucesso"})

@app.route("/reservas",methods=['GET'])
def reservas_realizadas():
    resultado = supabase.table("reservas").select("*").execute()
    return jsonify (resultado.data)

if __name__ == '__main__':
    app.run(port=8000,host="0.0.0.0",debug=True)
