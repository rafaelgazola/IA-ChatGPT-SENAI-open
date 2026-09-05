from flask import Flask,request,jsonify
from flask_cors import CORS 

#Criando um objeto Flask
app = Flask(__name__)
CORS(app)

#Criando uma base de produtos 
produtos = [
    {"id":1,
     "nome":"Celular",
     "valor":2000,
     "categoria":"Eletrônicos"
    },
    {
        "id":2,
        "nome":"Esponja",
        "valor":15,
        "categoria":"Limpeza" 
    }
]

#Lista todos os produtos
@app.route("/listar",methods=['GET'])
def lista_produtos():
    return jsonify(produtos)

#Lista produtos por ID
@app.route("/listar/<int:id>", methods=['GET'])
def lista_produtos_especificos(id):
    for produto in produtos:
        if produto['id'] == id:
            return jsonify(produto)
    return jsonify({"Mensagem":"Produto não encontrado!"}),404

#Criação de novos produtos
@app.route("/criar", methods=['POST'])
def criar_produto():
    produto_novo = request.get_json()
    produtos.append(produto_novo)
    return jsonify(produto_novo),201

#Rota para atualizar dados
@app.route("/atualizar/<int:id>", methods=['PUT'])
def atualizar_produto(id):
    produto_atualizado = request.get_json()
    for produto in produtos:
        if produto['id'] == id:
            produto['valor'] = produto_atualizado['valor']
            return jsonify(produto_atualizado)
    return jsonify({"Mensagem":"Produto não encontrado!"}),404

#Rota para apagar produtos
@app.route("/apagar/<int:id>", methods=['DELETE'])
def deletar_produto(id):
    for produto in produtos:
        if produto['id'] == id:
            produtos.remove(produto)
            return jsonify({"Mensagem":"Produto removido com sucesso!"})
    return jsonify({"Mensagem":"Produto não encontrado!"}),404

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000,debug=True)