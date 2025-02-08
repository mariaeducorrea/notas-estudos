# Guia de Comandos Git

## **Repositório**

#### **Inicializando um Repositório**
```bash
git init                                        # Inicializa um novo repositório
git add .                                       # Adiciona arquivos ao stage
git commit -m "Envian
do projeto"               # Grava alterações no repositório local
git branch -M main                              # Muda o nome da branch para "main"
git remote add origin [URL_DO_REPOSITÓRIO]     # Adiciona um repositório remoto
git push -u origin main                         # Envia as alterações para o repositório remoto
```
---
#### **Clonar um Repositório Existente**
```bash
# Clonar repositório remoto
git clone https://github.com/usuario/repositorio.git

# Clonar repositório e trocar branch inicial
git clone -b branch https://github.com/usuario/repositorio.git
```
---
#### **Verificar se projeto está vinculado a um repositório**
 ```bash
git remote -v
```
---
#### **Desvincular projeto de repositorio**
 ```bash
git remote remove origin
#ou
git remote rm origin
```
---
#### **Desvincular projeto de repositório local** 
```bash
cd cd C:\Users\Administrador\Desktop\projeto #Acessar projeto
ls -a   #Listar arquivos 
rm -rf .git #Excluit pasta .git  
```
---
#### **Vincular novo repositório ao projeto**
 ```bash
git remote add origin <url>
git remote -v
```
---
#### **Adicionar Arquivos:**
```bash
# Adicionar um arquivo específico
git add arquivo.txt
```
---
#### **Remover Arquivos:**
```bash
# Remover arquivo do repositório
git rm arquivo.txt

# Remover arquivo do repositório, mantendo no diretório local
git rm --cached arquivo.txt
```
---
#### **Mover arquivos**
```bash
git mv nome_doc.css nome_diretorio/nome_doc.css
```
---
#### **Adicionar um diretório**
 ```bash
git add nome-da-pasta/
```
#### **Ver Status repositorio**
```bash
git status
```
---
#### **Commit de alterações**
```bash
git status
git commit -a -m " " 
git push
# -a substitui "git add ." all = tudo
```
---
## **Push**
O comando git push é usado para enviar (ou "subir") suas alterações locais para um repositório remoto. Ele transfere commits que estão no seu repositório local para o repositório remoto, atualizando a branch correspondente no servidor.
```bash
#configurar para rastrear uma branch remota correspondente.
git push --set-upstream origin branch

#Quando branch local já está associada a uma branch remota.
git push

#Enviar alterações para uma branch específica no repositório remoto.
git push origin/main

#Quando você precisa sobrescrever alterações no repositório remoto((por exemplo, após usar git rebase ou reset)
#⚠️ Cuidado: Isso pode causar a perda de commits remotos que não estão no seu repositório local.
git push --force
```
---
## **Branch**
Branch no Git são como ramificações no histórico de commits do seu projeto. Eles permitem que você desenvolva diferentes funcionalidades, corrija bugs ou experimente novas ideias sem afetar o código principal do projeto. Cada branch é essencialmente um ponteiro para um commit específico no histórico.
 - Branch é a forma que o git separa as verões dos projetos.
 - Quando um projeto é criado ele inicia na branch main (master em projetos antigos).
 - Outros branches são criados para desenvolver novas funcionalidades, corrigir bugs ou testar ideias.
 - Após a finalização das alterações os branchs são unidos para ter o código-fonte final.
```bash
#Criar branch
git branch <nome>

#Criar e mudar para nova branch
#1. Acesse a branch que deseja fazer uma copia
#2. Execute:
#Isso irá criar um branch clone da branch atual.
git checkout -b "nome_clone_branch"
#ou
#Se estiver usando uma versão recente do Git
git switch -c <nome-do-branch>

#Listar branch
git branch

#Listar branch remotas
git branch -r

#Sair e Acessar outra branch
git checkout <nome_branch>

#Deletar branch
git branch -d <nome_branch>
#Se a branch não foi mesclada use -D

#Deletar branches remotas
git push origin --delete nome-da-branch

#Mandar branch para repositorio
#git push --set-upstream origin <nome-da-branch>: Este comando é usado para configurar a branch local para seguir a branch remota. Isso significa que, ao usar esse comando, o Git associará sua branch local à branch remota no repositório, facilitando o uso de comandos como git push e git pull no futuro, sem precisar especificar o nome do repositório e branch.
git push --set-upstream origin <nome_branch>
#git push origin <nome-da-branch>: Apenas envia sua branch para o repositório remoto. Se a branch já estiver configurada, você pode usar este comando sem problemas.
git push origin <nome-da-branch>

#Detalhes de branch
git show

#Exibir diferenças de branch atual como o remoto
git diff <arquivo><arquivo_b>


```
---
## **Pull**
- O comando git pull é usado para atualizar o repositório local com as alterações feitas no repositório remoto. Ele é, essencialmente, uma combinação de dois comandos: git fetch e git merge.
    - `git fetch`: Obtém as atualizações do repositório remoto para o local, mas não aplica as mudanças ao seu diretório de trabalho.
    - `git merge`: Mescla as atualizações obtidas no diretório de trabalho local.
- O git pull executa essas duas etapas automaticamente.
```bash
git pull
```
---
## **Restore**
- O comando git restore é usado para desfazer alterações em arquivos na área de trabalho ou na staging area (índice). Ele é especialmente útil para reverter alterações feitas antes de serem confirmadas com um commit.
- Use quando você quiser desfazer alterações em um arquivo, retornando-o ao estado do commit mais recente.
```bash
git restore caminho/diretorio/arquivo.md #especifico
git restore .  #descartar todas as alterações
```
---
## **Reset**
Este comando redefine o branch atual para corresponder exatamente ao estado do branch remoto.
- Sincroniza o branch local com o branch remoto especificado (ex.: origin/main).
- Apaga todas as alterações locais (tanto rastreadas quanto não rastreadas) que não foram commitadas.
- Reescreve o histórico local para alinhar com o branch remoto.
- *Use git reset --hard origin/<branch> quando precisa descartar todas as alterações locais e alinhar completamente o branch local com o remoto.*
```bash
git reset --hard origin/main
```
---
## **Rebase**
O comando git rebase é uma ferramenta poderosa no Git usada para reorganizar o histórico de commits. Ele move ou reaplica commits de uma branch em cima de outra, criando um histórico mais linear e fácil de entender. 
Por exemplo quando quiser atualizar sua branch com os commits mais recentes de outra branch sem fazer um merge:
```bash
git git rebase <branch>
```

---
## **Merge**
O comando git merge é usado para combinar o histórico de dois branches diferentes em um único branch no Git. Ele é uma parte essencial do fluxo de trabalho de controle de versão, permitindo que alterações feitas em diferentes branches sejam unificadas.
```bash
git merge <nome_branch> 
```

---
## **Stach**
Serve para salvar temporariamente mudanças feitas em seu repositório local, sem precisar comprometer (fazer commit) ou descartar essas alterações. Ele é ideal para situações em que você precisa trocar de ramo (branch), atualizar o repositório ou fazer outras alterações sem perder o trabalho em progresso.

```bash
#Salvar no stash
git stash

#Listar stash
git stash list

#Recuperar stash
git stash apply <número_stash>

#Ver alterações stash
git stash show -p <numero_stash>

#Remover stash especifica
git stash drop <numero_stash>

#Removendo todas as stash
git stash clear
```

---
## **Tags**
As tags no Git são usadas para marcar pontos específicos na história do repositório, geralmente para destacar versões importantes ou estáveis de um projeto, como lançamentos ou milestones. Elas funcionam como "marcadores" que você pode referenciar facilmente.

```bash
#Criar tags
git tag -a <nome-tag> -m <mensagem>

#Listar tag
git tag

#Ver tag
git show <nome-tag>

#Checkout em uma Tag
#Observação: Isso cria um estado detached HEAD. Você não está em um branch e alterações futuras não serão associadas a nenhum ramo.
git checkout <nome-tag>

#Enviar tag especifica para o repositorio
git push origin <nome-tag>

#Enviar todas as tags
git push origin --tags

#Remover tag localmete
git tag -d <nome-tag>

#Remover uma tag do repositório remoto
git push origin --delete <nome-tag>

```
---
## **Fetch** 
O comando git fetch é usado para atualizar seu repositório local com as alterações mais recentes de um repositório remoto. Ele baixa novos objetos e referências, como branches ou tags, mas não mescla automaticamente essas mudanças com seu branch atual.
```bash
git fetch -a 
```
---
## **Log**
```bash
# Histórico completo
git log

# Histórico resumido
git log --oneline

# Histórico com gráfico visual
git log --graph --oneline --all
```


---
## **Shortlog**
O comando shortlog no Git resume o histórico de commits de forma mais concisa, agrupando os commits por autor, facilitando a visualização de quem fez mais contribuições no repositório.
```bash
#Ver commits 
git shortlog

#Agrupar por autor
git shortlog -s -n

```
---
## **Reflog**
O comando reflog é utilizado para mostrar o histórico das referências do Git, ou seja, o registro de todas as mudanças que ocorreram no seu HEAD (a posição atual do repositório). Isso inclui commits que foram excluídos ou reescritos, permitindo recuperar commits que você possa ter perdido, como em situações de git reset ou git rebase.
```bash
git reflog
```
---
## **Clean**
O comando git clean é usado para remover arquivos e diretórios não rastreados do repositório de trabalho. É útil para limpar a área de trabalho, especialmente quando há arquivos temporários ou gerados que você deseja excluir.
```bash
#Visualizar o que será excluido
git clean -n

#Excluir
git clean

#Para remover efetivamente os arquivos, use a opção -f (force)
git clean -f

#Remover diretórios não rastreados:
git clean -fd

#Excluir apenas arquivos ignorados (.gitignore)
git clean -f -X

#-n	Simula o comando e mostra o que seria removido, sem excluir nada.
#-f	Necessário para forçar a remoção de arquivos (force).
#-d	Inclui diretórios na remoção.
#-X	Remove apenas arquivos ignorados pelo .gitignore.
#-x	Remove todos os arquivos não rastreados, ignorando o .gitignore.

```
---
## **gc - garbage collection**
O comando git gc (garbage collection) é usado para otimizar o repositório Git, limpando e reorganizando objetos para melhorar o desempenho. Ele é útil para manter o repositório eficiente, especialmente após uma longa sequência de operações que criam objetos desnecessários, como commits descartados, branches deletados ou merges.
- Ele identifica arquivos que não são mais necessários e os exclui.
```bash
git gc
```
---
## **fsck - file system check**
O comando git fsck (file system check) é usado para verificar a integridade do repositório Git. Ele analisa o banco de dados de objetos do Git para identificar problemas, como objetos corrompidos, referências perdidas ou inconsistências. Esse comando é especialmente útil para depuração e manutenção de repositórios.
```bash
git fsck
```
---
## **Submodule**
É usado para adicionar um repositório como submódulo dentro de um repositório Git existente. Submódulos permitem que você inclua outro repositório Git dentro do seu projeto, mantendo-o como uma entidade separada, mas vinculada.

 ```bash
#Verificar lista de submodules
git submodule 

#Adicionar submodule 
git submodule add <URL-do-repositorio>

#Enviar alterações do submodule para repositorio
git push --recurse-submodules=on-demand
 ```
---
## **Backup do Repositório**
Criar um arquivo compactado (formato ZIP) com o conteúdo da versão atual do repositório Git. 
```bash
git archive --format=zip --output=backup.zip HEAD
```







