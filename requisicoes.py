#%%
import requests

#%%
requisicao=requests.get('http://127.0.0.1:8000/produtos/1')
#%%
requisicao.json()
# %%

adicao=requests.post('http://127.0.0.1:8000/produtos/', 
                     json={
                         'nome': 'Produto 1', 
                         'preco': 10.0, 
                         'quantidade': 5})
# %%
adicao.json()
# %%
receber=requests.get('http://127.0.0.1:8000/produtos/0')
# %%
receber.json()
# %%
