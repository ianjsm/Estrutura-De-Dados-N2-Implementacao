from Exercicio01 import ArrayStack  # Importando a pilha que criamos

def exercicio_2():
    """
    Executa a série de operações pedida no Exercício 2.
    """
    S = ArrayStack() # "S" é o nome padrão para Pilha (Stack)
    
    print("Iniciando operações na Pilha S...")

    # Operações conforme o enunciado:
    # push(5), push(3), pop(), push(2), push(8), pop(), pop(), 
    # push(9), push(1), pop(), push(7), push(6), pop(), pop(), 
    # push(4), pop(), pop()
    
    operacoes = [
        ("push", 5), ("push", 3), ("pop", None), 
        ("push", 2), ("push", 8), ("pop", None), ("pop", None),
        ("push", 9), ("push", 1), ("pop", None),
        ("push", 7), ("push", 6), ("pop", None), ("pop", None),
        ("push", 4), ("pop", None), ("pop", None)
    ]

    for acao, valor in operacoes:
        if acao == "push":
            S.push(valor)
            print(f"push({valor}) -> Pilha: {S._dados}")
        elif acao == "pop":
            removido = S.pop()
            print(f"pop()    -> Removeu: {removido} | Pilha: {S._dados}")

    print("\nEstado final da pilha:", S._dados)
    print("Tamanho final:", len(S))

if __name__ == "__main__":
    exercicio_2()