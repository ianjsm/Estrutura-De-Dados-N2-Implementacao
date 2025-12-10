from Exercicio01 import ArrayStack

def esvaziar_pilha_recursivo(S):
    if S.is_empty():
        return

    removido = S.pop()
    print(f"Removendo recursivamente: {removido}")
    
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

    print("Esvaziando...")
    esvaziar_pilha_recursivo(S)

    print(f"Pilha depois de esvaziar: {S._dados}")
    print("Tamanho final:", len(S)) 