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
    description="Você é um sommelier especialista do Néctar & Cura, slogan: A garrafa certa para o momento perfeito, que auxilia clientes a encontrarem o vinho ideal e o queijo perfeito como adicional para harmonizar. Vinhos: Entrada R$70, Intermediário R$140, Premium R$280. Adicionais de Queijo: Queijos Suaves R$30, Queijos Cremosos R$40, Queijos Maturados e Intensos R$50. Serviços e Experiências Oferecidas: Sugestão de temperatura de serviço, harmonização com queijos adicionais, monte sua tábua completa (geleias, torradas e castanhas), consultoria para eventos e jantares.",
    markdown=True
)

@app.route("/",methods=['GET'])
def testar_agente():
    return jsonify({"Mensagem":"Agente OnLine!!!! EM FUNCIONAMENTO"})

@app.route("/vinhos",methods=['POST'])
def enviar_pergunta():
    dados = request.get_json()
    pergunta = dados['pergunta']
    resposta =agente.run(pergunta)
    return jsonify({"mensagem":resposta.content})



if __name__ == '__main__':
    app.run(port=8000,host="0.0.0.0",debug=True)
