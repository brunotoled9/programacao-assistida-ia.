# Debug: Erro de Tipo em JavaScript

## 1. Identificação do Erro

### Código Original (Com Erro)

```javascript
let x = "10"
let y = 5

console.log(x + y)
// Saída: "105" (string concatenada, não soma!)
```

### Código Corrigido

```javascript
let x = "10"
let y = 5

// Conversão explícita para número antes da soma
console.log(Number(x) + y)        // 15

// Alternativa: usando parseInt
console.log(parseInt(x, 10) + y) // 15

// Alternativa: usando operador unário +
console.log(+x + y)              // 15
```

---

## 2. Explicação da Causa

### O Problema

O erro ocorre devido à **coerção de tipos** do JavaScript e ao comportamento do operador `+`:

| Variável | Tipo | Valor |
|-----------|------|-------|
| `x` | String | `"10"` |
| `y` | Number | `5` |

### Por que acontece?

1. **Operador `+` com strings**: Quando um dos operandos é uma string, o JavaScript realiza **concatenação** em vez de adição aritmética.

2. **Precedência de tipos**: O JavaScript converte o número `5` para string `"5"` e concatena com `"10"`, resultando em `"105"`.

3. **Tipagem dinâmica**: JavaScript é fracamente tipado, fazendo conversões implícitas que podem gerar resultados inesperados.

### Fluxo de Execução

```
x = "10" (string)
y = 5    (number)

x + y
   ↓
"10" + 5
   ↓
"10" + "5"  (coerção implícita)
   ↓
"105"       (concatenação!)
```

---

## 3. Proposta de Correção

### Solução 1: Number()

```javascript
console.log(Number(x) + y)
```

**Vantagens:**
- Conversão explícita e clara
- Funciona para decimais também

**Desvantagens:**
- Retorna `NaN` para strings inválidas

---

### Solução 2: parseInt()

```javascript
console.log(parseInt(x, 10) + y)
```

**Vantagens:**
- Permite especificar base (decimal, binário, etc.)
- Mais flexível para parsing

**Desvantagens:**
- Trunca decimais (`"10.5"` → `10`)

---

### Solução 3: Operador Unário `+`

```javascript
console.log(+x + y)
```

**Vantagens:**
- Sintaxe concisa
- Boa performance

**Desvantagens:**
- Menos legível para iniciantes

---

## Recomendação

Para o caso específico, a solução mais idiomática em JavaScript moderno é usar o **operador unário `+`**:

```javascript
let x = "10"
let y = 5

console.log(+x + y)  // 15
```

Porém, para código mais legível em equipe, prefira `Number()` ou `parseInt()` com comentário explicativo.