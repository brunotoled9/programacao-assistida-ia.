"""Módulo para verificação de números primos."""

import math
from typing import Iterator


def encontrar_primos_ate(limite: int) -> list[int]:
    """Retorna todos os números primos até o limite especificado."""
    if limite < 2:
        return []
    
    sieve = [True] * (limite + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(limite**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limite + 1, i):
                sieve[j] = False
    
    return [i for i, e_primo in enumerate(sieve) if e_primo]


def e_primo(n: int) -> bool:
    """
    Verifica se um número é primo.
    
    Args:
        n: Número inteiro a ser verificado.
        
    Returns:
        True se o número for primo, False caso contrário.
        
    Raises:
        TypeError: Se o argumento não for um inteiro.
    """
    if not isinstance(n, int):
        raise TypeError(f"Esperado inteiro, recebido {type(n).__name__}")
    
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


def iterador_primos(inicio: int = 2, limite: int | None = None) -> Iterator[int]:
    """
    Generator que yields números primos indefinidamente ou até o limite.
    
    Args:
        inicio: Número inicial da busca (padrão: 2).
        limite: Limite máximo (opcional).
        
    Yields:
        Números primos em sequência.
    """
    n = max(2, inicio)
    
    while limite is None or n <= limite:
        if e_primo(n):
            yield n
        n += 1


# Testes
if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 17, 18, 19, 20, 97, 100, 101]
    
    print("=== Teste da função e_primo ===")
    for num in numeros:
        resultado = "✓ Primo" if e_primo(num) else "✗ Não primo"
        print(f"{num:3d} → {resultado}")
    
    print("\n=== Números primos até 50 ===")
    print(encontrar_primos_ate(50))
    
    print("\n=== Iterador de primos (10 primeiros) ===")
    primos = list(iterador_primos(limite=30))
    print(primos)