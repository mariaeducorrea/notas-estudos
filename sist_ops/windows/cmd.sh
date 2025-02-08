
#Listar programas instalados
winget list


#verifica e repara arquivos do sistema corrompidos ou ausentes.
C:\WINDOWS\system32>sfc /scannow

# Desligar imediatamente
shutdown /s /f /r /t 0 

# Reiniciar o pc
shutdown /r 

# Faze logoff
shutdown /l

# Forçar fechamentos apps
shutdown /f

# Definir tempo em segundos antes de desligaar ou reinicializar
shutdown /r /t 0
shutdown /s /t 0

# verificar e corrigir erros no disco rígido ou em uma unidade de armazenamento, verificando a integridade do sistema de arquivos e tentando reparar setores defeituosos ou problemas de alocação de arquivos.
C:\WINDOWS\system32>chkdsk C: /f /r
#/f: Corrige erros encontrados no disco.
#/r: Localiza setores defeituosos e recupera informações legíveis.

# formatar um disco ou unidade de armazenamento. Ao executar esse comando, todos os dados no disco serão apagados permanentemente. Portanto, é importante ter cuidado ao utilizá-lo e garantir que você esteja formatando a unidade correta
C:\WINDOWS\system32>format C: /FS:FAT32

# Copiar um arquivo para outro diretório:
xcopy C:\origem\arquivo.txt D:\destino

#  Copiar um diretório e todo o seu conteúdo para outro local:
xcopy C:\origem D:\destino /s /e
#/s: Copia diretórios e subdiretórios, mas não os vazios.
#/e: Copia diretórios e subdiretórios, incluindo os vazios.

# Exibir atributos de um arquivo:
attrib arquivo.txt

#Definir o atributo "somente leitura" em um arquivo:
attrib +R arquivo.txt

# Definir o atributo "oculto" em um arquivo:=
attrib +H arquivo.txt

# Remover todos os atributos de um arquivo:
attrib -R -A -S -H arquivo.txt

# é utilizado para associar uma extensão de arquivo a um programa específico.
assoc    

#é usado para acessar o Editor de Registro do Windows
regedit 

#abre o Gerenciador de Tarefas do Windows. 
taskmgr

#exibe a versão do Windows instalado no computador.
ver

# Exibir o conteúdo de arquivos de texto diretamente no prompt de comando
type C:\caminho\para\arquivo.txt

# Exibindo informações sobre a criptografia de arquivos e pastas:
cipher /c
 
 # Criptografando arquivos e pastas:
cipher /

# Descriptografando arquivos e pastas:
cipher /d

#Listar todos os drivers instalados:
driverquery

#Listar informações detalhadas sobre os drivers:
driverquery /v

#Listar informações em formato de lista:
driverquery /fo list

#Exportar informações para um arquivo CSV:
driverquery /fo csv > drivers.csv

#xibe informações de ajuda sobre comandos específicos do CMD.
help

# Informações do processador
wmic cpu get name
 
# wmic cpu get name Informações do processador
wmic cpu get name
#ou 
wmic cpu get name,Manufacturer,NumberOfCores,
NumberOflogicalProcessors,MaxClockSpeed
#name = nome/modelo processador
#Manufacturer = fabricante do processador
#NumberOfCores = n° de núcleos físicos do processador
#NumberOfLogicalProcessors = n° processadores lógicos
#MaxClockSpeed = velocidade máxima do clock do processador em MHZ

#`systeminfo:`  informações do sistema operacional
systeminfo

# Criar txt com informações e mandar para diretório especifico
C:\Users\Administrador\info.txt

#`cd:` (Change Directory) é usado para navegar entre diretórios no sitema de arquivos.
# Diretório especifico 
cd "C:\Program Files\postgresql\13\bin"

# Voltar um diretório 
cd..

# Diretório raiz
cd\

# Diretório do usuário
cd %USERPROFILE%

# Unidade diferente 
cd /d D:

# Visualizar o diretório atual 
cd

# Outros  dir
dir /A --Lista #todos os arquivos, incluindo arquivos ocultos.
dir /B --Lista #apenas os nomes dos arquivos/diretórios, sem detalhes.
dir /S --Lista #os arquivos de forma recursiva, incluindo subdiretórios.
dir /W --Lista #os arquivos em várias colunas.
dir /O --Ordena #a lista de arquivos. Por exemplo, /ON ordena por nome.

# Criar novo diretório 
mkdir teste_mkdi

# Novo diretório com espaçamento
mkdir  "novo diretório"

# Multiplos diretórios 
mkdir  pasta1 pasta2 

# Copiar arquivos
copy C:\Arquivo.txt D:\Destino

#ipconfig: exibe informações sobre a configuração de rede do seu computador.
ipconfig

#`ping:` Verificar conectividade entre o seu computador e um endereço IP
# Verificação curta
ping google.com
# Verificação longa -> ctrl _ c para encerrar ping
# recomendado deixar de um a dois minutos
ping -t google.com

#tasklist: listar todos os processos em execução do sistema, com informações sobre cada processo. 
tasklist

#taskkill: encerrar ou finalizar processos em execução no sistema.
taskkill /PID 17500

#netstat:  exibe estatísticas detalhadas sobre conexões de rede, tabelas, roteamento e informações sobre as interfaces de rede do sistema.
netstat
# Outros
netstat -n --exibe #endereços e portas em formato numérico
netstat -b --exibe #o nome do executável envolvido na criação de cada conexão ou escuta
netstat -o --exibe #o PID de cada conexão

r