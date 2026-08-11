from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Instancia principal da aplicacao.
app = FastAPI()

# Endpoint responsavel por verificar se a aplicacao esta rodando corretamente.
@app.get("/")
def home():
    return {"message": "Bem-vindo ao nosso Acervo Digital."}

# Modelo de dados necessarios para criar um livro.
class Livro(BaseModel):
    titulo: str
    autor: str
    nacionalidade: str


# Lista temporária utilizada apenas para simular os dados da nossa aplicação.
@app.get("/livros")
def listar_livros():
    return livros

# Endpoint responsavel por criar um novo livro a partir das informacoes enviadas pelo cliente.
@app.post("/livros", status_code=201)
def criar_livro (livro: Livro):
    novo_livro = {"id": len(livros) + 1, "titulo": livro.titulo, "autor": livro.autor, "nacionalidade": livro.nacionalidade}
    livros.append(novo_livro)
    return novo_livro

# Dados temporários compartilhados entre endpoints.
livros = [
    {"id": 1, "titulo": "Python para APIs.", "autor": "Marine Silva", "genero": "Tecnologia"},
    {"id": 2, "titulo": "Codigo Limpo.", "autor": "Marine Silva","genero": "Desenvolvimento Web"}
]

# Endpoint responsavel por atualizar os livros ou substituir.
@app.put("/livros/{livros_id}")
def alterar_livros(livros_id: int, livro: Livro):
    for alterar_livro in livros:
        if alterar_livro ["id"] == livros_id:
            alterar_livro["titulo"] = livro.titulo
            alterar_livro["autor"] = livro.autor
            return alterar_livro
    raise HTTPException (status_code=404, detail="Livro não encontrado.")


# Endpoint responsavel por atualizar o respectivo campo desejado.
@app.patch("/livros{livros_id}")
def editar_livros(livros_id: int):
    return {"message": f"Livro com a id {livros_id} atualizado com sucesso."}

# Endpoint responsavel por consultar um livro pelo identificador informado na URL.
@app.get("/livros/{livro_id}")
def buscar_livro(livro_id: int):
    for livro in livros:
        if livro["id"] == livro_id:
            return livro
    raise HTTPException (status_code=404, detail="Livro não encontrado.")


# Endpoint responsavel por deletar um livro pelo identificador informado na URL.
@app.delete("/livros/{livro_id}")
def deletar_livro(livro_id: int):
    for indice, livro in enumerate(livros):
        if livro["id"] == livro_id:
            livros.pop(indice)
            return {"message": f"Livro com a id {livro_id} apagado com sucesso."}
    raise HTTPException (status_code=404, detail= "Livro não encontrado.")

# Endpoint responsavel por consultar o autor do livro pelo uso de identificador.
@app.get("/livros/{livro_id}/autor")
def buscar_autor(livro_id: int):
    for livro in livros:
        if livro["id"] == livro_id:
            return {"message": f"Autor do livro: {livro_id} e: {livro['autor']}"}

# Endpoint responsavel por criar um novo autor para o livro.
@app.post("/livros/{livro_id}/autor")
def criar_autor():
    novo_autor = {"autor": "Comitê Científico Internacional da UNESCO"}
    livros.append(novo_autor)
    return {"message": f"O autor {novo_autor} foi vinculado ao livro com sucesso."}

# Endpoint responsavel por alterar o autor do livro pelo uso de identificador.
@app.put("/livros/{livro_id}/autor")
def alterar_autor(livro_id: int):
    return {"message": f"O auor do livro com a id {livro_id} foi alterado com sucesso."}

# Endpoint responsavel por alterar um determinado campo do autor do livro pelo uso de identificador.
@app.patch("/livros/{livro_id}/autor")
def editar_autor(livro_id: int):
    return {"message": f"O autor do livro com a id {livro_id} foi alterado com sucesso."}

# Endpoint responsavel por deletar o autor do livro pelo uso de identificador.
@app.delete("/livros/{livro_id}/autor")
def deletar_autor(livro_id: int):
    return {"message": f"O autor do livro com a id {livro_id} foi deletado com sucesso. "}

# Adicionado novos endpoints para filmes, elenco e direção.
#Endpoint responsavel por listar os filmes.
@app.get("/filmes")
def listar_filmes():
    return [
        {"id": 11, "titulo": "Corra."},
        {"id": 12, "titulo": "Mulher Rei."},
        {"id": 13, "titulo": "Cidade de Deus."}
    ]

#Endpoint responsavel por listar o elenco.
@app.get("/eleco")
def listar_elenco():
    return [
        {"id": 11, "elenco": "Daniel Kaluuya, Allison Williams, Bradley Whitford"},
        {"id": 12, "elenco": "Viola Davis, Thuso Mbedu, John Boyega"},
        {"id": 13, "elenco": "Leandro Firmino, Alice Braga, Seu Jorge"}
    ]

# Endpoint responsavel por listar a direcao.
@app.get("/direcao")
def listar_direcao():
    return [
        {"id": 11, "direcao": "Gina Prince-Bythewood"},
        {"id": 12, "direcao": "Barry Jenkins"},
        {"id": 13, "direcao": "Fernando Meirelles"}
    ]