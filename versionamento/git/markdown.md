# Arquivo README.md.
O Git Markdown (MD) é amplamente utilizado para documentar projetos, como nos arquivos README.md. Ele possui uma sintaxe simples e versátil para formatar texto. 

---

## 1. **Títulos**
Use `#` para criar títulos de diferentes níveis:

```markdown
# Título Nível 1
## Título Nível 2
### Título Nível 3
#### Título Nível 4
##### Título Nível 5
###### Título Nível 6
```
### Exemplo:

# Título Nível 1
## Título Nível 2
### Título Nível 3

---
## 2. **Texto Estilizado**
- **Negrito:** Use `**texto**` ou `__texto__`.
- *Itálico:* Use `*texto*` ou `_texto_`.
- ***Negrito e Itálico:*** Use `***texto***`.
- ~~Riscado:~~ Use `~~texto~~`.

### Exemplo:

**Negrito**
*Itálico*
***Negrito e Itálico***
~~Riscado~~

---

## 3. **Listas**

### Lista Ordenada:

```markdown
1. Item 1
2. Item 2
   1. Subitem 2.1
   2. Subitem 2.2
3. Item 3
```

### Exemplo:
1. Item 1
2. Item 2
   1. Subitem 2.1
   2. Subitem 2.2
3. Item 3

### Lista Não Ordenada:

```markdown
- Item 1
- Item 2
  - Subitem 2.1
  - Subitem 2.2
- Item 3
```

### Exemplo:
- Item 1
- Item 2
  - Subitem 2.1
  - Subitem 2.2
- Item 3

---


## 4. **Links**

### Links Simples:

```markdown
[Texto do Link](https://exemplo.com)
```

[Visite o Google](https://www.google.com)

### Links com Títulos:

```markdown
[Texto do Link](https://exemplo.com "Título do Link")
```

[Visite o Google](https://www.google.com "Acesse o Google")

---

## 5. **Imagens**

### Inserir Imagens:

```markdown
![Texto Alternativo](https://via.placeholder.com/150 "Título da Imagem")
```

![Exemplo de Imagem](https://via.placeholder.com/150 "Imagem de Placeholder")

---

## 6. **Códigos**

### Código Inline:

```markdown
`codigo_inline`
```

Exemplo: `print("Hello World")`

### Bloco de Código:

```markdown
\`\`\`linguagem
// Código aqui
\`\`\`
```

#### Exemplo com Python:

```python
print("Olá, Markdown!")
```

---

## 7. **Blocos de Citação**

```markdown
> Este é um bloco de citação.
> Pode ter várias linhas.
```

> Este é um bloco de citação.
> Pode ter várias linhas.

---

## 8. **Tabelas**

```markdown
| Coluna 1 | Coluna 2 | Coluna 3 |
|----------|----------|----------|
| Valor A  | Valor B  | Valor C  |
| Valor D  | Valor E  | Valor F  |
```

| Coluna 1 | Coluna 2 | Coluna 3 |
|----------|----------|----------|
| Valor A  | Valor B  | Valor C  |
| Valor D  | Valor E  | Valor F  |

---

## 9. **Gráficos com Markdown (Mermaid)**
Para gráficos, use a sintaxe do **Mermaid**:

```markdown
\`\`\`mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
\`\`\`
```

#### Exemplo Renderizado:
```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

---

## 10. **Linha Horizontal**

Use `---`, `***` ou `___` para criar uma linha horizontal.

---

## 11. **Links Internos**

Crie links para seções do mesmo documento:

```markdown
[Ir para Títulos](#títulos)
```

[Ir para Títulos](#títulos)

---





