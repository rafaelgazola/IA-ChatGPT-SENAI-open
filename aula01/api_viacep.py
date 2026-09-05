import requests
 
url = "https://viacep.com.br/ws/01001000/json/"

dados = requests.get(url)
endereco = dados.json()
logradouro = "praça"

endereco = {
    'cep': '01001-000',
    'logradouro': 'Praça da Sé', 
    'complemento': 'lado ímpar', 
    'unidade': '',
    'bairro': 'Sé',
    'localidade': 'São Paulo',
    'uf': 'SP', 
    'estado': 'São Paulo', 
    'regiao': 'Sudeste', 
    'ibge': '3550308', 
    'gia': '1004', 
    'ddd': '11', 
    'siafi': '7107'
}

print(f"""Seu CEP é: {endereco['cep']} 
Sua Rua é: {endereco['logradouro']}
Seu Bairro é: {endereco['bairro']}
Sua Cidade é: {endereco['localidade']}
Seu estado é: {endereco['uf']}
""")
