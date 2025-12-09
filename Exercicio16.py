from Exercicio12 import FilaCircular

def contar_circular(lista):
    if lista.vazia(): return 0
    inicio = lista.cauda.proximo
    atual = inicio
    cont = 0
    while True:
        cont += 1
        atual = atual.proximo
        if atual is inicio: break
    return cont

def executar():
    print("Exercício 16")
    fc = FilaCircular()
    for x in input("Lista Circular: ").split(): fc.inserir(x)
    print(f"Tamanho: {contar_circular(fc)}")