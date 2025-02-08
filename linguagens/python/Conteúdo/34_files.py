''''
Modos de Abrir Arquivos em Python
> open(file, mode, encoding=None)
'''

#Ler um arquivo de texto:
with open("arquivo.txt", "r", encoding="utf-8") as file:
    conteudo = file.read()
    print(conteudo)

#Escrever em um arquivo (sobrescrevendo):
with open("arquivo.txt", "w", encoding="utf-8") as file:
    file.write("Este é o novo conteúdo do arquivo.")

#Adicionar conteúdo a um arquivo:
with open("arquivo.txt", "a", encoding="utf-8") as file:
    file.write("\nEsta linha foi adicionada ao final.")

#arquivos de img
with open("imagem.png", "rb") as file:
    dados = file.read()
    print(dados[:10])  




#Importação e Manipulação de Diferentes Formatos de Arquivo


# Arquivos CSV
import csv

with open("dados.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for linha in reader:
        print(linha)
#Escrita de CSV
with open("novo_dados.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Nome", "Idade", "Cidade"])  # Cabeçalho
    writer.writerow(["Maria", 30, "São Paulo"])


#Arquivos JSON
import json

with open("dados.json", "r", encoding="utf-8") as file:
    dados = json.load(file)
    print(dados)

# Escrita de JSON
dados = {"nome": "João", "idade": 25, "cidade": "Rio de Janeiro"}

with open("novo_dados.json", "w", encoding="utf-8") as file:
    json.dump(dados, file, indent=4)



# Arquivos Excel
'''
import pandas as pd
df = pd.read_excel("dados.xlsx")  # Lê a planilha
print(df.head())  # Mostra as primeiras linhas
'''
#Escrita de Excel
'''
df = pd.DataFrame({"Nome": ["Ana", "Lucas"], "Idade": [29, 34]})
df.to_excel("novo_dados.xlsx", index=False)
'''




'''
O modo de abertura define como o arquivo será acessado: se será apenas para leitura, escrita, ou ambas, além de outras opções.

Modo	             Descrição
'r'	Leitura (Read): Abre o arquivo apenas para leitura. O arquivo precisa existir, caso contrário, será gerado um erro.
'w'	Escrita (Write): Abre o arquivo para escrita. Se o arquivo já existir, seu conteúdo será apagado. Se não existir, ele será criado.
'a'	Adição (Append): Abre o arquivo para adicionar conteúdo ao final. Se o arquivo não existir, ele será criado.
'x'	Criação Exclusiva (Exclusive Creation): Abre o arquivo para escrita, mas falha se o arquivo já existir.
'b'	Modo Binário (Binary): Adiciona ao modo de abertura o suporte para trabalhar com arquivos binários (não codificados em texto).
't'	Modo Texto (Text): É o padrão, usado para trabalhar com arquivos de texto. Normalmente não é necessário explicitá-lo, pois é o comportamento padrão.

'''
