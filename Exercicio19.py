from Exercicio12 import DequeEncadeado

def executar():
    print("Exercício 19")
    lista = DequeEncadeado()
    for x in input("Lista (ex: A B A C): ").split(): lista.inserir_final(x)
    
    vistos = set()
    atual = lista.cabeca.proximo
    
    while atual is not lista.cauda:
        prox = atual.proximo
        if atual.dado in vistos:
            lista._remover_no(atual)
        else:
            vistos.add(atual.dado)
        atual = prox
        
    res = []
    curr = lista.cabeca.proximo
    while curr is not lista.cauda:
        res.append(curr.dado)
        curr = curr.proximo
    print(f"Únicos: {res}")