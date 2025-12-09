from Exercicio01 import Pilha

def executar():
    print("Exercício 5")
    entrada = input("Digite a lista (separada por espaço): ").split()
    print(f"Original: {entrada}")
    
    p = Pilha()
    for item in entrada:
        p.empilhar(item)
        
    lista_invertida = []
    while not p.vazia():
        lista_invertida.append(p.desempilhar())
        
    print(f"Invertida: {lista_invertida}")