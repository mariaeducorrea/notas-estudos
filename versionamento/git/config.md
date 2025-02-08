# **Instalação e configurações git**


## **Instalação**

#### **Windows**
1. Baixe o instalador no site oficial: https://git-scm.com/.
2. Execute o instalador:
	- Durante a instalação, escolha o editor padrão do Git (recomendo o VS Code ou o Vim).
	- Selecione Git Bash como terminal preferido.
3. Verifique a instalação:
	```bash
	git --version
	``` 

#### **Linux**
1. Atualize os repositórios:
	```bash
	sudo apt update    # Para distribuições baseadas em Debian/Ubuntu
	sudo yum update    # Para distribuições baseadas em Red Hat
	```
2. Instale o Git
	```bash
	sudo apt install git  # Debian/Ubuntu
	sudo yum install git  # Red Hat/CentOS/Fedora
	```
3. Verifique a instalação:
	```bash
	git --version
	```

---

## **Configurações**

### **Usuário**
1. Abra o terminal (ou Git Bash):
	```bash
	git config --global user.name "Seu Nome"
	git config --global user.email "seuemail@example.com"
	```
2. Verifique se as configurações foram aplicadas:
	```bash
	git config --global --list
	```

### **SSH**
1. Verificar se já existe uma chave SSH
	```bash
	ls -al ~/.ssh
	```
	- -t ed25519: Especifica o tipo de chave a ser criada. ed25519 é mais recente e recomendado por ser mais seguro e rápido.
	- -C "your_email@example.com": Associa a chave ao seu e-mail (substitua pelo e-mail da sua conta GitHub).

	- Passo a Passo:
		1. Quando solicitado, pressione Enter três vezes para aceitar os padrões:
			- Local para salvar a chave (padrão é ~/.ssh/id_ed25519).
			- Passphrase (opcional, mas recomendado para mais segurança).
		2. A chave será gerada.


2. Criar uma nova chave SSH
	```bash
	ssh-keygen -t ed25519 -C "your_email@example.com"
	```
3. Copiar o conteúdo da chave pública
	```bash
	cat "C:\Users\Administrador\.ssh\id_ed25519.pub"
	```
---


### **Cores do Git**

#### **AZUL: Modified (Modificado)**
- Representa arquivos que foram modificados no diretório de trabalho, mas ainda não estão prontos para commit.
- **Ação necessária:** Adicionar ao índice (staged) usando `git add`.

#### **VERDE: Staged**
- Representa arquivos que foram adicionados ao índice (staged) e estão prontos para serem comitados.
- **Ação necessária:** Realizar o commit usando `git commit`.

#### **LARANJA/AMARELO: Merge Conflict (Conflitos de Merge)**
- Representa arquivos que estão no índice (staged) e possuem conflitos de merge que precisam ser resolvidos antes do commit.
- **Ação necessária:** Resolver os conflitos manualmente e marcar o arquivo como resolvido com `git add`.

#### **VERMELHO: Untracked (Não Rastreado)**
- Arquivos no diretório de trabalho que não estão sendo rastreados pelo Git.
- **Ação necessária:** Adicionar ao rastreamento com `git add` ou ignorar adicionando ao `.gitignore`.

#### **CINZA: Ignored (Ignorado)**
- Arquivos que estão listados no arquivo `.gitignore` e, portanto, não aparecem no rastreamento do Git.
- **Ação necessária:** Nenhuma. Esses arquivos são intencionalmente ignorados.

#### **ROXO: Renamed (Renomeados)**
- Arquivos que foram renomeados ou movidos.
- **Ação necessária:** O Git já detectou a mudança. Pode ser necessário adicionar o arquivo renomeado ao índice com `git add`.

#### **BRANCO (ou padrão do terminal): Clean (Limpo)**
- Representa que o arquivo não sofreu alterações em relação ao último commit.
- **Ação necessária:** Nenhuma. O arquivo está sincronizado com o repositório.

