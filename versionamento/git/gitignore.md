# .gitignore
O arquivo .gitignore é usado em projetos que utilizam o Git para controle de versão, com o objetivo de especificar arquivos ou diretórios que devem ser ignorados pelo Git. Isso significa que os itens listados no .gitignore não serão rastreados ou incluídos no repositório, mesmo que estejam na pasta do projeto.
 
---
### Por que usar o .gitignore?
Manter o repositório limpo: Evita o versionamento de arquivos desnecessários, como logs, cache ou dependências compiladas.
Privacidade e segurança: Impede o envio de informações sensíveis, como chaves de API, credenciais ou configurações locais.
Evitar conflitos: Reduz a chance de conflitos em arquivos gerados automaticamente ou específicos de um ambiente.
   

### Como criar um .gitignore?
1. Crie um arquivo chamado .gitignore na raiz do seu repositório.
2. Adicione os padrões ou caminhos dos arquivos/diretórios que deseja ignorar.
Exemplos:
```bash
# Ignorar arquivos de log
*.log

# Ignorar arquivos gerados pelo sistema operacional
.DS_Store
Thumbs.db

# Ignorar arquivos de configuração local
.env

# Ignorar arquivos na pasta raiz
/secrets.json

# Ignorar todos os arquivos .txt, exceto README.txt
*.txt
!README.txt

# Ignorar tudo na pasta "build", mas não o subdiretório "build/libs"
build/*
!build/libs/
```



