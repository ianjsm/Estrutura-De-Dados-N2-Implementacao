from Exercicio01 import ArrayDeque

def testar_exercicio_07():
    """
    Executa a série de operações de deque pedida no Exercício 7.
    Operações:
    add_first(4), add_last(8), add_last(9), add_first(5), back(), 
    delete_first(), delete_last(), add_last(7), first(), last(), 
    add_last(6), delete_first(), delete_first().
    """
    D = ArrayDeque()
    print("--- [Exercício 07] Teste de Mesa (Deque) ---")

    # Passo 1: add_first(4)
    D.add_first(4)
    print(f"add_first(4)  -> {D._dados}")

    # Passo 2: add_last(8)
    D.add_last(8)
    print(f"add_last(8)   -> {D._dados}")

    # Passo 3: add_last(9)
    D.add_last(9)
    print(f"add_last(9)   -> {D._dados}")

    # Passo 4: add_first(5)
    D.add_first(5)
    print(f"add_first(5)  -> {D._dados}")

    # Passo 5: back() (Geralmente é um 'peek' no último elemento)
    print(f"back()        -> Olhando o último: {D.last()}")

    # Passo 6: delete_first()
    removido = D.delete_first()
    print(f"delete_first()-> Saiu: {removido} | Deque: {D._dados}")

    # Passo 7: delete_last()
    removido = D.delete_last()
    print(f"delete_last() -> Saiu: {removido} | Deque: {D._dados}")

    # Passo 8: add_last(7)
    D.add_last(7)
    print(f"add_last(7)   -> {D._dados}")

    # Passo 9: first()
    print(f"first()       -> Olhando o primeiro: {D.first()}")

    # Passo 10: last()
    print(f"last()        -> Olhando o último: {D.last()}")

    # Passo 11: add_last(6)
    D.add_last(6)
    print(f"add_last(6)   -> {D._dados}")

    # Passo 12: delete_first()
    removido = D.delete_first()
    print(f"delete_first()-> Saiu: {removido} | Deque: {D._dados}")

    # Passo 13: delete_first()
    removido = D.delete_first()
    print(f"delete_first()-> Saiu: {removido} | Deque: {D._dados}")

    print(f"\nEstado Final do Deque: {D._dados}")

if __name__ == "__main__":
    testar_exercicio_07()