from Exercicio01 import ArrayStack

def esvaziar_pilha_recursivo(S):
    """
    Exercício 4: Remove todos os elementos de uma pilha recursivamente.
    
    Lógica Recursiva:
    1. Caso Base: Se a pilha estiver vazia, paramos (return).
    2. Passo Recursivo: Removemos um item e chamamos a função de novo 
       para lidar com o restante da pilha.
    """
    # 1. Caso Base: Condição de parada
    if S.is_empty():
        return

    # 2. Passo Recursivo: Remove o topo e chama a função novamente
    removido = S.pop()
    print(f"Removendo recursivamente: {removido}") # Print apenas para visualizar
    
    esvaziar_pilha_recursivo(S)

if __name__ == "__main__":
    S = ArrayStack()
    S.push(10)
    S.push(20)
    S.push(30)
    S.push(40)
    S.push(50)

    print(f"Pilha antes de esvaziar: {S._dados}")
    print("Tamanho inicial:", len(S))

    print("\n--- Iniciando Esvaziamento Recursivo ---")
    esvaziar_pilha_recursivo(S)

    print(f"\nPilha depois de esvaziar: {S._dados}")
    print("Tamanho final:", len(S)) # Deve ser 0
    
    # Teste extra: Garantir que não quebra se a pilha já estiver vazia
    print("\nTentando esvaziar pilha já vazia (não deve dar erro):")
    esvaziar_pilha_recursivo(S)
    print("Sucesso.")