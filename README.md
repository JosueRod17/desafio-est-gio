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
```

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
