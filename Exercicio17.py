from Exercicio12 import FilaEncadeada

def reverter(atual, anterior=None, lista=None):
    if atual is None:
        if lista: lista.cabeca = anterior
        return
    prox_orig = atual.proximo
    atual.proximo = anterior
    reverter(prox_orig, atual, lista)

def executar():
    print("Exercício 17")
    lista = FilaEncadeada()
    for x in input("Lista: ").split(): lista.inserir(x)
    
    reverter(lista.cabeca, None, lista)
    
    arr = []
    curr = lista.cabeca
    while curr:
        arr.append(curr.dado)
        curr = curr.proximo
    print(f"Invertida: {arr}")