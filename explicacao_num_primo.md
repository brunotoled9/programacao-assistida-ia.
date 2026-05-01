# Números Primos

## O que é um Número Primo?

Um **número primo** é um número natural maior que 1 que possui apenas dois divisores positivos: 1 e ele mesmo.

## Exemplos de Números Primos

- 2 (divisores: 1, 2)
- 3 (divisores: 1, 3)
- 5 (divisores: 1, 5)
- 7 (divisores: 1, 7)
- 11 (divisores: 1, 11)
- 13 (divisores: 1, 13)

## Números Não Primos (Compostos)

Números que têm mais de dois divisores são chamados de **números compostos**.

- 4 (divisores: 1, 2, 4) → Composto
- 6 (divisores: 1, 2, 3, 6) → Composto
- 9 (divisores: 1, 3, 9) → Composto

## Propriedades Importantes

1. **2 é o único número primo par** — todos os outros primos são ímpares.
2. **O número 1 não é primo** — ele tem apenas um divisor.
3. **Infinitos primos** — Euclides provou que existe um número infinito de primos.

## Como Verificar se um Número é Primo?

Para verificar se um número `n` é primo, basta testar a divisibilidade por todos os números ímpares menores que `√n`.

### Exemplo em Python (Otimizado)

```python
import math

def e_primo(n: int) -> bool:
    """Verifica se um número é primo."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limite = int(math.isqrt(n))
    for i in range(3, limite + 1, 2):
        if n % i == 0:
            return False
    return True
```

### Otimizações Aplicadas

| Técnica | Benefício |
|---------|-----------|
| Verificar `n == 2` primeiro | Caso especial tratado rapidamente |
| Verificar `n % 2 == 0` | Elimina todos os pares com uma verificação |
| Usar `math.isqrt(n)` | Raiz quadrada inteira (mais rápida que `n**0.5`) |
| Iterar apenas ímpares | Reduz iterações pela metade |

### Funções Complementares

```python
# Encontrar todos os primos até um limite (Crivo de Eratóstenes)
def encontrar_primos_ate(limite: int) -> list[int]:
    sieve = [True] * (limite + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limite**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limite + 1, i):
                sieve[j] = False
    return [i for i, e in enumerate(sieve) if e]

# Generator lazy de primos
def iterador_primos(inicio: int = 2, limite: int = None) -> Iterator[int]:
    n = max(2, inicio)
    while limite is None or n <= limite:
        if e_primo(n):
            yield n
        n += 1
```

## Aplicações

Números primos são fundamentais em:
- **Criptografia** (RSA, criptografia de chave pública)
- **Geradores de números aleatórios**
- **Teoria dos números**