from Exercicio12 import DequeEncadeado

def inverter_deque(d):
    curr = d.cabeca
    while curr:
        temp = curr.proximo
        curr.proximo = curr.anterior
        curr.anterior = temp
        curr = curr.anterior 
    d.cabeca, d.cauda = d.cauda, d.cabeca

def executar():
    print("Exercício 20")
    d = DequeEncadeado()
    for x in input("Lista: ").split(): d.inserir_final(x)
    
    inverter_deque(d)
    
    res = []
    curr = d.cabeca.proximo
    while curr is not d.cauda:
        res.append(curr.dado)
        curr = curr.proximo
    print(f"Invertida: {res}")