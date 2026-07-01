# Minha Solução — Banco

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