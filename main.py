#%%
## Exercício — API de Cadastro de Produtos
## Crie uma API com FastAPI que gerencie produtos de uma loja. 
## Os produtos ficam salvos em uma lista em memória (sem banco de dados por enquanto).


#%%
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


#%%
app = FastAPI(
    title='API de Cadastro de Produtos',
    description='API para gerenciar produtos de uma loja',
    version='1.0.0'
)

class produto(BaseModel):
    nome: str
    preco: float
    quantidade: int

produtos=[]


@app.get ('/')
def root():
    return {'API de Cadastro de Produtos': 'Bem-vindo!'}

@app.get('/produtos')
def listar_produtos():
    return produtos

@app.get('/produtos/{id}')
def obter_produto(id:int):
    try: 
        # Tenta retornar o produto se o ID existir
        return produtos[id]
    except Exception:
        # Captura qualquer erro (como o ID não existir) e avisa o usuário
        raise HTTPException(status_code=404, detail=f"O id {id} não existe na lista de produtos")
        

@app.post('/produtos')
def adicionar_produto(produto:produto):
    produtos.append(produto.model_dump())
    return {'Adicionado': produto}

@app.delete('/produtos/{id}')
def excluir_produto(id:int):
    try:
        # Tenta excluir o produto se o ID existir
        produtos.pop(id)
        return {'Deletado': id}
    except Exception:
        # Captura qualquer erro (como o ID não existir) e avisa o usuário
        raise HTTPException(status_code=404, detail=f"O id {id} não existe na lista de produtos")

# %%
