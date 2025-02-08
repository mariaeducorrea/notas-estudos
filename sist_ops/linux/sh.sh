#************** Comandos gerais sistema 

# Verificar espaço em disco
df -h



#************** Manipulação de pacotes e instalações

# instalar pacotes
    sudo apt install nome_programa

# atualizar pacotes
    sudo apt update  # Atualiza a lista de pacotes disponíveis e as versões que estão disponíveis para o sistema.
    sudo apt upgrade # Instala as versões mais recentes dos pacotes que já estão instalados no seu sistema.

# remove pacotes
    sudo apt remove nome_programa

# remove pacotes mais arquivos
    sudo apt purge nome_programa

# buscar por pacote
    apt search editor(ou outra palavra relacionada ao pacotes)

# listar pacotes instalado
    apt list --installed

# ver informacoes de um pacote
    apt show nome_pacote

# limpar pacotes desnecessarios 
    sudo apt autoremove

# pacotes que dependem de um pacote
    apt rdepends nome_pacote

# atualizar sistema e remover pacotes nao necessarios
    sudo apt dist-upgrade

# limpar pacotes baixado do cache (libera espaço em disco)
    sudo apt clean



#**************Comandos para Serviços

# Iniciar um Serviço
    sudo systemctl start nome_do_serviço

# Parar um Serviço
    sudo systemctl stop nome_do_serviço

# Reiniciar um Serviço
    sudo systemctl restart nome_do_serviço

# Desativar um Serviço
    sudo systemctl disable nome_do_serviço

# Habilitar um Serviço
    sudo systemctl enable nome_do_serviço

# Verificar o Status de um Serviço
    sudo systemctl status nome_do_serviço



#************** Configurações de usuários

# adicionar usuario
    sudo adduser nome_usuario 

# entrar em outro usuario
    sudo su nome_usuario




#************** Instalações de Pacotes

# Editor de arquivos
    sudo apt -y install vim

# Pacote que oferece autocompletar avançado para o shell bash
    sudo apt -y install bash-completion

# ferramenta para criptografia e assinatura digital de dados e comunicações
    sudo apt -y install gnupg2

# Um utilitário de linha de comando usado para baixar arquivos da web. Ele suporta HTTP, HTTPS e FTP, o que o torna útil para baixar arquivos diretamente de um terminal.
    sudo apt -y install wget


