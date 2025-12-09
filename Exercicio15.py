from Exercicio12 import FilaEncadeada

def contar(no):
    if no is None: return 0
    return 1 + contar(no.proximo)

def executar():
    print("Exercício 15")
    lista = FilaEncadeada()
    for x in input("Lista: ").split(): lista.inserir(x)
    print(f"Tamanho: {contar(lista.cabeca)}")