# Task Manager

Aplicação web educacional desenvolvida em **Flask** para gerenciar tarefas (*Create, Read, Update, Delete*) com implementação de **testes automatizados** usando **Pytest**..  
O projeto foi criado como parte dos estudos de **APIs REST**, **métodos HTTP**, **Postman** e **Swagger Editor**, aplicando conceitos aprendidos durante as aulas.  

Além do código, este repositório inclui **anotações teóricas detalhadas** que explicam os fundamentos utilizados no desenvolvimento.

---

##  Tecnologias utilizadas
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Pytest](https://docs.pytest.org/)
- [Requests](https://docs.python-requests.org/)
- API REST
- Postman
- Swagger Editor

---

##  Conceitos estudados e aplicados
- **Flask**: microframework para desenvolvimento web em Python.
- **API** e **API REST**: comunicação cliente-servidor via HTTP.
- **API RESTful**: implementação fiel aos princípios do REST.
- **Métodos HTTP**: GET, POST, PUT, PATCH, DELETE.
- **Stateless** e **Cache** no contexto de APIs.
- **Endpoints**: URLs específicas para manipulação de recursos.
- **Códigos de resposta HTTP** (1xx, 2xx, 3xx, 4xx, 5xx).
- **Pytest**: framework para testes automatizados.
- **Biblioteca Requests**: utilizada para consumir endpoints durante os testes.

As anotações completas estão no arquivo [`ANOTACOES.py`](./ANOTACOES.py).

---

## ⚙️ Funcionalidades
- **Criar tarefa** (`POST /tasks`)
- **Listar todas as tarefas** (`GET /tasks`)
- **Obter tarefa por ID** (`GET /tasks/<id>`)
- **Atualizar tarefa** (`PUT /tasks/<id>`)
- **Deletar tarefa** (`DELETE /tasks/<id>`)

---

##  Testes automatizados
O projeto conta com testes automatizados criados com **Pytest** que validam:
1. Criação de tarefa
2. Listagem de tarefas
3. Obtenção de tarefa específica
4. Atualização de tarefa
5. Exclusão de tarefa

Para rodar os testes, é necessário:
1. Ter o servidor Flask rodando (`python app.py`)
2. Executar:
   ```bash
   pytest -v
    ```
##  Como executar o projeto

1. **Clonar o repositório**
   ```bash
   git clone https://github.com/seu-usuario/task-manager.git
   cd task-manager
    ```
2. Criar e ativar ambiente virtual

    ```bash
    python -m venv venv
    source venv/bin/activate  # Mac/Linux
    venv\Scripts\activate     # Windows
    ```
3. Instalar dependências

    ```bash
    pip install flask pytest requests
    ```
4. Executar o servidor
    ```bash
    python app.py
    ```

5. Testar os endpoints

Usar Postman ou Swagger Editor.

Base URL: http://127.0.0.1:5000

## Estrutura de pastas
        .
        ├── app.py           # Arquivo principal da aplicação Flask
        ├── models/          # Modelos de dados
        ├── ANOTACOES.md     # Anotações teóricas do projeto
        └── README.md

