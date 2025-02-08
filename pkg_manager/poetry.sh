#POETRY

#Poetry é uma ferramenta de gerenciamento de dependências e empacotamento para projetos Python.
#visa simplificar a criação e o gerenciamento de ambientes virtuais, bem como a definição e instalação de dependências, tudo em uma única ferramenta
# Documentação: https://python-poetry.org/docs/

# Instalar
pipx install poetry

# Desinstalar poetry 
python -m poetry self uninstall

# Criar um Novo Projeto
poetry new nome_do_projeto
cd nome_do_projeto #entra no diretorio
code . #abrir diretorio no vscode

# Adicionar Dependência
poetry add nome_do_pacote

# Remover Dependência
poetry remove nome_do_pacote

# Listar Dependências
poetry show

# Remover um Projeto
poetry remove nome_do_projeto

# configurar o Poetry de forma que ele crie ambientes virtuais dentro do diretório do projeto
poetry config virtualenvs.in-project true

# Verificando a Configuração
poetry config --list

#criar ambiente .venv com poetry 
poetry shell