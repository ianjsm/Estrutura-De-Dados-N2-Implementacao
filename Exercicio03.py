from Exercicio01 import ArrayStack

def transfer(S, T):
    """
    Exercício 3: Transfere todos os elementos da pilha S para a pilha T.
    
    Lógica:
    Ao removermos (pop) de S, pegamos os elementos do topo para a base.
    Ao inserirmos (push) em T, esses elementos são empilhados na ordem inversa.
    O resultado é que o topo de S vai para o fundo dos novos itens em T,
    e o fundo de S vira o novo topo de T.
    """
    # Enquanto S não estiver vazia
    while not S.is_empty():
        # Remove do topo de S
        elemento = S.pop()
        # Adiciona no topo de T
        T.push(elemento)

if __name__ == "__main__":
    # Criando as pilhas S e T
    S = ArrayStack()
    T = ArrayStack()

    # Preenchendo S com: [Base] 10, 20, 30 [Topo]
    S.push(10)
    S.push(20)
    S.push(30)

    print(f"Estado inicial de S (topo é o último): {S._dados}")
    print(f"Estado inicial de T: {T._dados}")

    print("\n--- Transferindo S para T ---")
    transfer(S, T)

    print(f"Estado final de S (deve estar vazia): {S._dados}")
    # T deve ter recebido 30 primeiro, depois 20, depois 10.
    # Se T estava vazia, ficará: [30, 20, 10]
    print(f"Estado final de T (topo é o último): {T._dados}")
    
    # Verificação rápida: O topo de T deve ser 10 (que era a base de S)
    if not T.is_empty():
        print(f"Novo topo de T: {T.top()}")