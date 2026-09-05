# Agente Hotel (Persistência)

## Comandos
- Use o Python do ambiente local; `python` não está disponível no PATH: `.venv\Scripts\python.exe`.
- Instale as dependências com `.venv\Scripts\python.exe -m pip install -r requirements.txt`.
- Inicie o servidor com `.venv\Scripts\python.exe app.py` e acesse `http://localhost:8000/`.
- Não use a porta padrão 5000: `app.py` escuta em `0.0.0.0:8000` com debug habilitado.
- Não há testes, linter, typecheck ou CI configurados; valide mudanças iniciando o servidor e exercitando o fluxo afetado.

## Estrutura e contratos
- O backend inteiro está em `app.py`; o front-end é um único arquivo em `static/index.html` servido pela rota `GET /`.
- `app.py` carrega as variáveis `SUPABASE_URL` e `SUPABASE_KEY` do ambiente via `load_dotenv()` e usa a tabela Supabase `reservas`.
- `POST /perguntar` recebe `{"pergunta": ...}` e retorna `{"mensagem": ...}`; `POST /agente` usa o mesmo payload, mas retorna `{"resposta": ...}` e é a rota usada pelo chat do front-end.
- `POST /reserva` e `POST /reservas` inserem o JSON recebido em `reservas`; `GET /reservas` retorna a lista de registros.
- O formulário envia e a tela renderiza os campos `nome`, `quarto`, `checkin` e `checkout`.

## Cuidados
- Preserve as rotas e as chaves JSON acima: `static/index.html` depende desse contrato.
- Preserve a `description` do agente em `app.py`, pois ela contém os preços e serviços usados nas respostas.
- Não exponha valores de credenciais nem altere arquivos de ambiente ao investigar ou modificar o projeto.
