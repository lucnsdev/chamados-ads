from flask import Flask
from flask import request

'''
Para executar: 
source .venv/bin/activate
uv run flask run
'''

app = Flask(__name__)

chamados = [
    {
        "id": 0,
        "titulo": "Sem internet",
        "descrição": "O computador não está conectando",
        "solicitante": "Pedro",
        "prioridade": "media"
    }
]
proximo_id = 1


@app.get("/")
def inicio():
    return {"mensagem": "Api de chamados em funcionamento"}


@app.get("/chamados")
def get_chamados():
    global chamados
    return chamados


@app.get("/chamados/<int:chamado_id>")
def get_chamado_by_id(chamado_id):
    global chamados
    for chamado in chamados:
        if chamado["id"] == chamado_id:
            return chamado
    return {"mensagem": "Chamado não encontrado"}, 404


@app.post("/chamados")
def criar_chamado():
    global chamados
    global proximo_id
    chamado = request.get_json()
    chamados.append(chamado)
    chamado["id"] = proximo_id
    proximo_id += 1
    return {"message": "Chamado criado", "chamado": chamado}, 200
    