from Exercicio12 import FilaEncadeada

def executar():
    print("Exercício 18")
    lista = FilaEncadeada()
    entrada = input("Números (ex: 10 -5 3): ").split()
    for x in entrada: lista.inserir(int(x))
    
    pos = FilaEncadeada()
    neg = FilaEncadeada()
    
    curr = lista.cabeca
    while curr:
        if curr.dado >= 0: pos.inserir(curr.dado)
        else: neg.inserir(curr.dado)
        curr = curr.proximo
        
    def listar(l):
        res = []
        c = l.cabeca
        while c:
            res.append(str(c.dado))
            c = c.proximo
        return res
        
    print(f"Positivos: {listar(pos)}")
    print(f"Negativos: {listar(neg)}")