from flask import Flask


# para executar: flask run
app = Flask(__name__)

@app.get("/")
def inicio():
    return {
        "mensagem": "Api de chamados em funcionamento"
    }

@app.get("/chamados")
def get_chamados():
    return [
        {
            "id": 1,
            "titulo": "Impressora com problema",
            "status": "aberto"
        },
        {
            "id": 2,
            "titulo": "Sem internet",
            "status": "em andamento"
        }
    ]

@app.get("/chamados/<int:chamado_id>")
def get_chamado_by_id(chamado_id):
    return {
        "id": chamado_id,
        "titulo": "Impressora com problema",
        "status": "aberto"
    }