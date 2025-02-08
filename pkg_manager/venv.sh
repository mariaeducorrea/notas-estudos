#VENV

#A pasta .venv (ou simplesmente venv) é um diretório que contém um ambiente virtual Python.
#Ambientes virtuais são uma maneira de isolar dependências de projetos Python, permitindo 
#que você tenha diferentes versões de pacotes instalados para diferentes projetos sem conflitos.

# Criar um Ambiente Virtual
#acessar diretório do projeto e executar:
python -m venv .venv

# Ativar o Ambiente Virtual
source .venv\Scripts\activate
# OBS: Após ativar, você verá o nome do ambiente virtual prefixado no prompt do terminal, indicando que ele está ativo.

# Enquanto o ambiente virtual está ativo, você pode instalar pacotes usando
pip install nome_do_pacote

# Desativar o Ambiente Virtual
deactivate

#excluir ambiente virtual
rm -rf .venv
