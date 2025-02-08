# Guia Completo de Pull Request (PR)

A tradução literal de pull request seria "solicitação de pull" ou "solicitação de mesclagem", mas no contexto do desenvolvimento de software, uma tradução mais clara seria:

- "Solicitação para incorporar alterações" ou "Solicitação para integrar código".

Um **pull request (PR)** é uma solicitação para integrar alterações feitas em uma branch específica de um repositório Git a outra branch, geralmente a principal (como `main` ou `master`). 

O pull request é usado para:
- **Revisar** o código antes de integrá-lo.
- **Colaborar** com outros desenvolvedores.
- **Garantir qualidade** com verificações automatizadas (CI/CD).

---

## Como Funciona o Pull Request?

### **Criação da Branch de Trabalho**
- Antes de começar a implementar mudanças, crie uma branch específica para a tarefa:

```bash
git checkout -b feature/nome-da-tarefa
```
Isso evita conflitos e mantém o histórico de mudanças organizado.

###  **Implementação e Commits**
- Faça as alterações necessárias e salve o progresso com commits claros:

```bash
git add .
git commit -m "Descrição objetiva do que foi feito"
#ou só
git commit -a -m "Descrição objetiva do que foi feito"
```

Boas práticas para commits:
- Mensagens descritivas e objetivas.
- Dividir as alterações em pequenos commits, sempre que possível.

###  **Envio das Alterações para o Repositório Remoto**
- Envie a branch criada para o repositório remoto:

```bash
git push origin feature/nome-da-tarefa
```

###  **Criação do Pull Request (PR)**
- Acesse a interface da plataforma (como GitHub, GitLab ou Bitbucket).
- Clique em "New Pull Request".
- Escolha:
  - A branch principal como destino.
  - Sua branch de trabalho como origem.
- Preencha:
  - Um título descritivo.
  - Uma descrição detalhada das alterações.
  - Mencione problemas relacionados, se aplicável

###  **Revisão de Código**
- Outros desenvolvedores revisam o PR, deixando comentários ou sugerindo mudanças.
- Ajuste sua branch com base no feedback:

```bash
git add .
git commit -m "Ajusta funcionalidade conforme revisão"
git push origin feature/nome-da-tarefa
```

###  **Aprovação e Merge**
- Após aprovação:
  - Realize o merge diretamente na plataforma ou via terminal:

```bash
git checkout main
git merge feature/nome-da-tarefa
```

- Exclua a branch local e remota para manter o repositório limpo:

```bash
git branch -d feature/nome-da-tarefa
git push origin --delete feature/nome-da-tarefa
```
---

## Boas Práticas para Pull Requests

###  **Use Mensagens Claras**
- O título do PR deve ser descritivo (ex.: "Adiciona endpoint de autenticação").
- A descrição deve incluir:
  - O motivo das mudanças.
  - O que foi alterado.
  - Como testar.

###  **Divida o Trabalho em Commits Menores**
- Cada commit deve representar uma alteração lógica e coesa.

###  **Teste Antes de Abrir o PR**
- Garanta que o código está funcionando localmente e que passou nos testes.

###  **Respeite o Fluxo de Branches**
- Siga a estratégia de branching definida pelo time (ex.: Git Flow).
  - Exemplo de nomenclatura:
    - `feature/nome-da-funcionalidade`
    - `fix/corrige-bug-x`

###  **Faça Revisões Construtivas**
- Ao revisar um PR, forneça feedback claro e evite críticas vagas.

###  **Automatize Processos Repetitivos**
- Configure ferramentas de CI/CD para automatizar testes e verificações.

---

#### Aprenda mais:
[Como fazer um pull request.](https://www.youtube.com/watch?v=GgedJcK014s&list=PLylCwvNCtoanYEIC4OBMO2hfB-ihCSv9Y&index=6)


