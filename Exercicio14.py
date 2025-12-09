from Exercicio12 import FilaEncadeada

def concatenar(L, M):
    if L.vazia():
        L.cabeca = M.cabeca
    elif not M.vazia():
        L.cauda.proximo = M.cabeca
        L.cauda = M.cauda
    L._tamanho += M._tamanho
    # Limpar M
    M.cabeca = M.cauda = None
    M._tamanho = 0

def executar():
    print("Exercício 14")
    L = FilaEncadeada()
    M = FilaEncadeada()
    
    for x in input("Lista L: ").split(): L.inserir(x)
    for x in input("Lista M: ").split(): M.inserir(x)
    
    concatenar(L, M)

    arr = []
    curr = L.cabeca
    while curr:
        arr.append(curr.dado)
        curr = curr.proximo
    print(f"Concatenada: {arr}")