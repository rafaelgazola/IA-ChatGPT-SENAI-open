from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Criando um objeto Flask
app = Flask(__name__)
CORS(app)

# Base de dados em memória (lista de produtos de um e-commerce)
produtos = [
    {"id": 1, "nome": "Celular", "valor": 2000.00, "categoria": "Eletr\u00f4nicos", "estoque": 10},
    {"id": 2, "nome": "Esponja", "valor": 15.00, "categoria": "Limpeza", "estoque": 50},
    {"id": 3, "nome": "Notebook", "valor": 4500.00, "categoria": "Eletr\u00f4nicos", "estoque": 5},
]

# Contador de IDs para evitar duplicidade
proximo_id = max([p["id"] for p in produtos], default=0) + 1


# Tela inicial: serve o frontend (HTML/CSS/JS)
@app.route("/")
def index():
    return render_template("index.html")


# READ - Lista todos os produtos (GET)
@app.route("/listar", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)


# READ - Lista um produto específico por ID (GET)
@app.route("/listar/<int:id>", methods=["GET"])
def listar_produto_especifico(id):
    for produto in produtos:
        if produto["id"] == id:
            return jsonify(produto)
    return jsonify({"mensagem": "Produto não encontrado!"}), 404


# CREATE - Cria um novo produto (POST)
@app.route("/criar", methods=["POST"])
def criar_produto():
    global proximo_id
    dados = request.get_json(force=True, silent=True) or {}

    if not dados.get("nome") or dados.get("valor") is None:
        return jsonify({"mensagem": "Campos 'nome' e 'valor' são obrigatórios!"}), 400

    novo_produto = {
        "id": proximo_id,
        "nome": dados.get("nome"),
        "valor": dados.get("valor"),
        "categoria": dados.get("categoria", "Sem categoria"),
        "estoque": dados.get("estoque", 0),
    }
    produtos.append(novo_produto)
    proximo_id += 1
    return jsonify(novo_produto), 201


# UPDATE - Atualiza um produto existente por ID (PUT)
@app.route("/atualizar/<int:id>", methods=["PUT"])
def atualizar_produto(id):
    dados = request.get_json(force=True, silent=True) or {}
    for produto in produtos:
        if produto["id"] == id:
            produto["nome"] = dados.get("nome", produto["nome"])
            produto["valor"] = dados.get("valor", produto["valor"])
            produto["categoria"] = dados.get("categoria", produto["categoria"])
            produto["estoque"] = dados.get("estoque", produto["estoque"])
            return jsonify(produto)
    return jsonify({"mensagem": "Produto não encontrado!"}), 404


# UPDATE parcial - PATCH (método HTTP extra)
@app.route("/atualizar/<int:id>", methods=["PATCH"])
def atualizar_produto_parcial(id):
    dados = request.get_json(force=True, silent=True) or {}
    for produto in produtos:
        if produto["id"] == id:
            for chave, valor in dados.items():
                if chave in produto:
                    produto[chave] = valor
            return jsonify(produto)
    return jsonify({"mensagem": "Produto não encontrado!"}), 404


# DELETE - Remove um produto por ID (DELETE)
@app.route("/apagar/<int:id>", methods=["DELETE"])
def apagar_produto(id):
    for produto in produtos:
        if produto["id"] == id:
            produtos.remove(produto)
            return jsonify({"mensagem": "Produto removido com sucesso!"})
    return jsonify({"mensagem": "Produto não encontrado!"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
