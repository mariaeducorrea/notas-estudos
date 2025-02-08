#PYENV

#O pyenv é uma ferramenta popular para gerenciar diferentes versões do Python em sistemas.
#Ele permite que você instale e use várias versões do Python em uma única máquina, o que é 
#útil para desenvolvedores que precisam testar ou trabalhar em projetos que dependem de versões específicas do Python
#Documentação: https://github.com/pyenv-win/pyenv-win

# Instalação
https://github.com/pyenv-win/pyenv-win > Quick start > Install pyenv-win in PowerShell. > Rodar comando Invoke 
#vai ocorre erro > rodar comando abaixo
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser #depois desse rodar novamente o Invoke

#Variaveis de ambiente para pyenv
PYENV - C:\Users\Administrador\.pyenv\pyenv-win
PYENV_ROOT - C:\Users\Administrador\.pyenv\pyenv-win
PYENV_HOME - C:\Users\Administrador\.pyenv\pyenv-win


# Verificar Versões Instaladas
pyenv versions

# Definir a Versão Global
pyenv global 3.9.7

# Definir a Versão Local (no diretório do projeto)
pyenv local 3.9.7

