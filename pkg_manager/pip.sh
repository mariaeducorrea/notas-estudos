#PIP

#O pip é o gerenciador de pacotes padrão para Python.
#Ele permite que você instale, atualize e gerencie bibliotecas e pacotes de terceiros que são utilizados em seus projetos Python.

# Versao pip
pip --version

# Instalar um Pacote
pip install nome_do_pacote

# Atualizar um Pacote
pip install --upgrade nome_do_pacote

# Desinstalar um Pacote
pip uninstall nome_do_pacote

# Listar Pacotes Instalados
pip list

# Gerar um arquivo de requisitos
pip freeze > requirements.txt

# Reproduzir um ambiente
pip install -r requirements.txt

# Desinstalar todas as bibliotecas do pip
pip freeze | grep -v "^-e" | xargs pip uninstall -y
#ou 
for /F "delims=" %i in ('pip freeze') do pip uninstall -y %i


# Mostrar Informações sobre um Pacote
pip show nome_do_pacote
