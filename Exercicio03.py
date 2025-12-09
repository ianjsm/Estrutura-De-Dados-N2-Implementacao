from Exercicio01 import Pilha

def transferir(origem, destino):
    while not origem.vazia():
        destino.empilhar(origem.desempilhar())

def executar():
    print("Exercício 3")
    S = Pilha()
    T = Pilha()
    
    entrada = input("Digite elementos para a pilha S (separados por espaço): ")
    for item in entrada.split():
        S.empilhar(item)
    
    print(f"S original: {S._dados}")
    print(f"T original: {T._dados}")
    
    transferir(S, T)
    
    print(f"S final: {S._dados}")
    print(f"T final: {T._dados}")