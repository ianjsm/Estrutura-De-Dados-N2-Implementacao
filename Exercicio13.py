from Exercicio12 import FilaEncadeada

def encontrar_penultimo(lista):
    if lista.vazia() or lista.cabeca.proximo is None:
        return None
    atual = lista.cabeca
    while atual.proximo.proximo is not None:
        atual = atual.proximo
    return atual.dado

def executar():
    print("Exercício 13")
    lista = FilaEncadeada()
    inp = input("Digite elementos da lista: ").split()
    for x in inp: lista.inserir(x)
    
    res = encontrar_penultimo(lista)
    print(f"Penúltimo: {res}")