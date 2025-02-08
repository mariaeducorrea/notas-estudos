# Guia Completo do GitHub

Este guia aborda todas as funcionalidades principais do GitHub, desde a criação de repositórios até pull requests, forks e integrações.

## **Criando um Repositório no GitHub**
Um repositório Git é um local onde todo o histórico de alterações de um projeto é armazenado e gerenciado. Ele serve como um sistema de controle de versão, permitindo que desenvolvedores acompanhem alterações no código-fonte, colaborem com outras pessoas e revertam mudanças, se necessário.

### Passos:
1. Acesse [GitHub](https://github.com) e faça login.
2. No menu principal, clique em `New` ou `+` > `New Repository`.
3. Preencha as informações necessárias:
   - **Repository Name:** Nome do repositório.
   - **Description:** (Opcional) Descrição do projeto.
   - **Visibility:** Escolha entre público ou privado.
   - **Initialize Repository:** Selecione opções como criar um arquivo README, .gitignore ou licença.
4. Clique em `Create Repository` para finalizar.




## **Forks e Clonagem**
Um fork é uma cópia de um repositório existente para o seu perfil, permitindo modificações sem afetar o original.

#### Como Fazer um Fork:
1. Navegue até o repositório desejado.
2. Clique no botão `Fork` no canto superior direito.
3. Escolha o destino (sua conta ou organização).

### Quando Usar:
- Para contribuir com projetos de terceiros.
- Para criar uma cópia independente de um projeto.



##  **Trabalhando com Pull Requests**
Pull Requests (PR) são solicitações para integrar alterações de uma branch (ou fork) em outra branch de um repositório.

#### Criando um Pull Request:
1. No GitHub, vá até o repositório e clique em `Pull Requests`.
2. Clique em `New Pull Request`.
3. Escolha a branch de origem e a branch de destino para comparar.
4. Revise as alterações e clique em `Create Pull Request`.
5. Preencha o título e a descrição, explicando as alterações.

#### Boas Práticas:
- Adicione uma descrição clara e detalhada.
- Inclua referências a issues.
- Certifique-se de que os testes estão passando.

#### Aprenda mais:
[Como fazer um pull request.](https://www.youtube.com/watch?v=GgedJcK014s&list=PLylCwvNCtoanYEIC4OBMO2hfB-ihCSv9Y&index=6)



## **Issues no GitHub**
As issues são usadas para rastrear tarefas, bugs e discussões relacionadas ao projeto.

#### Criando uma Issue:
1. No repositório, clique em `Issues` > `New Issue`.
2. Adicione um título descritivo.
3. Descreva o problema ou sugestão com detalhes.
4. Opcional: Adicione labels, assignees ou milestones.
5. Clique em `Submit New Issue`.


## **GitHub Actions**
GitHub Actions é uma ferramenta de CI/CD integrada ao GitHub, usada para automação de tarefas como testes, deploys e validações.

#### Configurando GitHub Actions:
1. No repositório, clique em `Actions`.
2. Escolha um template ou crie um workflow personalizado em `.github/workflows/`.
3. Use arquivos YAML para definir as etapas do workflow.


## **Integração com Times**

### Colaboração:
- **Contributors:** Adicione colaboradores ao repositório via `Settings` > `Collaborators`.
- **Reviewers:** Configure revisores em pull requests para garantir qualidade de código.

### Melhorias na Organização:
- **Projects:** Gerencie tarefas como em um kanban, disponível na aba `Projects`.
- **Milestones:** Agrupe issues e pull requests em objetivos maiores.



## **GitHub Pages**
GitHub Pages permite criar e hospedar sites estáticos diretamente de um repositório.

#### Como Configurar:
1. No repositório, vá em `Settings` > `Pages`.
2. Escolha a branch e o diretório para publicar.
3. Clique em `Save`.

#### Exemplos de Uso:
- Documentação de projetos.
- Portfólios.
- Sites de projetos open-source.

