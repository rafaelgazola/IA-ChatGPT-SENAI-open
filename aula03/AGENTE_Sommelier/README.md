# 🍷 Néctar & Cura - Elisa (Sommelier Virtual)

> *"A garrafa certa para o momento perfeito"*

O **Néctar & Cura** é um projeto de e-commerce e consultoria de vinhos impulsionado por Inteligência Artificial. A proposta principal é ajudar o cliente a escolher o vinho ideal para qualquer ocasião e, ao mesmo tempo, sugerir o **adicional de queijo e acompanhamentos (add-ons)** perfeitos para enriquecer a degustação.

---

## 🔗 Links e Infraestrutura

- **Front-End Interativo:** Desenvolvido via **Lovable** (Tailwind CSS + Shadcn UI).
- **LINK LOVABLE:** `https://vinho-sommelier.lovable.app/`  (Para acessar o site desenvolvido)
- **API Back-End (Render):** `https://agente-vinhos-sommelier.onrender.com/vinhos` (Método `POST`)

---

## 🧰 Tecnologias Utilizadas

### **Back-End (Python API)**
- **Python 3.x:** Linguagem principal do servidor.
- **Flask:** Micro-framework web para criação da API RESTful e gerenciamento das rotas.
- **Flask-CORS (`flask_cors`):** Habilitação de Cross-Origin Resource Sharing para permitir a comunicação segura com o front-end.
- **Agno Framework (`agno`):** Framework para orquestração de agentes de IA, estruturação da persona e execução de prompts.
- **OpenAI API (`gpt-4o-mini`):** Modelo de linguagem responsável por gerar as recomendações e respostas da Elisa.
- **python-dotenv (`dotenv`):** Gerenciamento seguro de variáveis de ambiente (chaves de API).

### **Front-End (Interface)**
- **Lovable:** Plataforma de geração de interface e prototipagem rápida.
- **React:** Biblioteca para construção da interface de usuário baseada em componentes.
- **Tailwind CSS:** Framework CSS utilitário para estilização responsiva e tema customizado (tons Bordeaux e Ouro Velho).
- **Shadcn UI:** Coleção de componentes acessíveis e reutilizáveis (Input, Buttons, ScrollArea, Dialogs).

### **Hospedagem & Deploy**
- **Render:** Plataforma de nuvem responsável pela hospedagem contínua da API Flask em Python.
- **Git & GitHub:** Controle de versão do código fonte.

---

## 🛠️ Como o Back-End foi Desenvolvido

O servidor da aplicação foi escrito em **Python** utilizando **Flask** para expor a API REST e a biblioteca **Agno** para criar e gerenciar a persona do Agente de IA.

### Destaques do Código:
- **Framework Agno & OpenAI:** Instanciamos o `Agent` configurado com o modelo `gpt-4o-mini`, injetando a descrição da persona da *Elisa*, a tabela de preços dos vinhos (R$70 a R$280), os adicionais de queijos (R$30 a R$50) e as regras de harmonização.
- **CORS Habilitado:** Utilização do `flask_cors` para permitir requisições seguras vindas da interface web no Lovable.
- **Rotas:**
  - `GET /` : *Health check* para confirmar se a API está online (`"Mensagem": "Agente OnLine!!!! EM FUNCIONAMENTO"`).
  - `POST /vinhos` : Recebe a pergunta do usuário no JSON (`{"pergunta": "..."}`), executa o agente com `agente.run(pergunta)` e retorna a resposta formatada da Elisa no campo `mensagem`.

---

## 🧀 Matriz de Harmonização (Vinhos & Queijos Add-ons)

| Categoria do Vinho | Faixa de Preço | Tipo de Queijo Adicional | Preço Queijo | Acompanhamentos Sugeridos |
| :--- | :--- | :--- | :--- | :--- |
| **Entrada** (Leve / Refrescante) | R$ 70,00 | Queijos Suaves (Frescos, Gouda Jovem) | R$ 30,00 | Torradas, azeitonas, uvas |
| **Intermediário** (Médio Corpo) | R$ 140,00 | Queijos Cremosos (Brie, Camembert) | R$ 40,00 | Mel artesanal, geleia de pimenta, nozes |
| **Premium** (Encorpado / Reserva) | R$ 280,00 | Queijos Maturados e Intensos (Gorgonzola, Parmesão) | R$ 50,00 | Geleia de damasco, pães artesanais, castanhas |

---

## 🚀 Passo a Passo para Testar

### 1. Teste na Interface Web (Lovable)
1. Acesse o link da aplicação web gerada no **Lovable**.
2. Abra o widget de chat no canto inferior direito para interagir com a **Elisa - A Sommelier**.
3. Envie uma mensagem perguntando sobre sugestões (ex: *"Quero um vinho intermediário e um queijo cremoso"*).
4. O chat enviará o payload via `POST` para a API no Render e exibirá a recomendação de harmonização.

### 2. Teste Direto da API (cURL / Terminal)

Você pode testar a API enviando uma requisição `POST` com o campo `pergunta`:

```bash
curl -X POST [https://agente-vinhos-sommelier.onrender.com/vinhos](https://agente-vinhos-sommelier.onrender.com/vinhos) \
  -H "Content-Type: application/json" \
  -d '{"pergunta": "Recomende um vinho de entrada e o queijo ideal"}'
