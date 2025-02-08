'''
Os dicionários (ou dict) em Python são uma estrutura de dados muito importante. Eles são coleções de pares chave-valor, onde cada chave é única. A manipulação de dicionários é essencial para trabalhar com dados organizados e de fácil acesso. 

'''

# criar dict
meu_dict = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print(meu_dict)

# acessando valores
meu_dict = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
nome = meu_dict["nome"]
idade = meu_dict["idade"]
print(nome)  # João
print(idade)  # 30

# get
meu_dict = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
cidade = meu_dict.get("cidade")
print(cidade)  # São Paulo

# adicionando e atualizando itens
meu_dict = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

meu_dict["estado"] = "SP"
print(meu_dict)

meu_dict["idade"] = 31
print(meu_dict)