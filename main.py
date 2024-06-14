from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"id_cliente": 1,"ordem compra": "0001", "qtd_vendas": 1, "SKU":"TM5"},
    2: {"id_cliente": 2,"ordem compra": "0003", "qtd_vendas": 2, "SKU":"TM5"},
    3: {"id_cliente": 3,"ordem compra": "0004", "qtd_vendas": 1, "SKU":"TM3"},
    4: {"id_cliente": 4,"ordem compra": "0006", "qtd_vendas": 5, "SKU":"TM72"}
}

@app.get("/")
def home():
    return {"Vendas": len(vendas)}

@app.get("/vendas/{id_venda}") #{variavel}
def get_venda(id_venda: int):
    return vendas[id_venda]

@app.post("/")
def post():
    return "hello world"