# BANCO AGILIZE

Projeto desenvolvido como solução para o desafio técnico do processo seletivo de **Estágio em Tecnologia da Agilize**.

## Sobre o projeto

O sistema simula operações bancárias entre contas correntes e poupança, respeitando as regras de negócio propostas no desafio.

A aplicação é dividida em duas partes:

* **Backend:** API desenvolvida com Python e FastAPI.
* **Frontend:** Interface web desenvolvida com HTML, CSS e JavaScript puro, consumindo a API.

## Tecnologias utilizadas

### Backend

* Python 3
* FastAPI
* Uvicorn
* Pydantic

### Frontend

* HTML5
* CSS3
* JavaScript

## Funcionalidades

* Listagem de contas
* Saque
* Transferência entre contas
* Atualização automática da tabela de contas
* Validação das regras de negócio

## Estrutura do projeto

```text
backend/
    app/
        dados.py
        esquemas.py
        main.py
        modelos.py
        rotas.py
        servicos.py

frontend/
    index.html
    style.css
    script.js
```

## ▶ Como executar

### Backend

Entre na pasta do backend:

```bash
cd backend
```

Instale as dependências:

```bash
py -m pip install -r requirements.txt
```

Execute a API:

```bash
py -m uvicorn app.main:app --reload
```

A documentação da API estará disponível em:

```text
http://127.0.0.1:8000/docs
```# Minha Solução — Banco

## Stack
- **Backend:** Python 3.14 + FastAPI
- **Frontend:** HTML5, CSS3 e JavaScript puro

## Pré-requisitos / dependências
**Backend** 

- **Windows**

Entre na pasta `backend`:

```bash
cd backend
```

Instale as dependências:

```bash
py -m pip install -r requirements.txt
```

- **Linux**

Entre na pasta `backend`:

```bash
cd backend
```

Instale as dependências:

```bash
python3 -m pip install -r requirements.txt
```

> **OBS:** Em distribuições Linux que utilizam a política PEP 668 (como Ubuntu 24.04+), caso ocorra o erro `externally-managed-environment`, utilize:

```bash
python3 -m pip install --break-system-packages -r requirements.txt
```

## Como executar

### Backend (API)

- **Windows**

Entre na pasta `backend`:

```bash
cd backend
```

Execute a API:

```bash
py -m uvicorn app.main:app --reload
```

- **Linux**

Entre na pasta `backend`:

```bash
cd backend
```

Execute a API:

```bash
python3 -m uvicorn app.main:app --reload
```

A API ficará disponível em:

```
http://127.0.0.1:8000
```

Documentação Swagger:

```
http://127.0.0.1:8000/docs
```

### Frontend

- **Windows**

Abra um terminal na pasta `frontend` e execute:

```bash
cd frontend
py -m http.server 5500
```

- **Linux**

Abra um terminal na pasta `frontend` e execute:

```bash
cd frontend
python3 -m http.server 5500
```

Depois acesse:

```
http://localhost:5500
```

OBS: Certifique-se de que o backend esteja em execução antes de abrir o frontend.

## Exemplo de uso
```
1. Execute o backend.

2. Execute o frontend.

3. Clique em "Atualizar Contas" para visualizar as contas disponíveis.

4. Para realizar um saque, informe o ID da conta e o valor desejado e clique em Sacar.

5. Para realizar uma transferência, informe a conta de origem, a conta de destino e o valor, depois clique em Transferir.

6. Após cada operação, a tabela de contas é atualizada automaticamente.
```

## Observações (opcional)
- A aplicação foi organizada em camadas (```dados```, ```modelos```, ```esquemas```, ```servicos``` e ```rotas```) para separar responsabilidades.

- As regras de negócio foram implementadas no backend.

- Além da operação obrigatória de saque, foi implementada a funcionalidade de transferência entre contas como diferencial.

- A interface web consome a API utilizando JavaScript puro (```fetch```).

### Frontend

Abra o arquivo:

```text
frontend/index.html
```

em seu navegador.

## Regras implementadas

* Conta corrente possui tarifa de R$ 1,00 por operação.
* Conta corrente pode utilizar cheque especial até R$ 500,00 negativos.
* Conta poupança não possui tarifa.
* Conta poupança não pode ficar com saldo negativo.

## Autor

Josué Rodrigues da Silva
