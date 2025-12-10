from Exercicio12 import LinkedQueue

def separar_listas(original):
    positivos = LinkedQueue()
    negativos = LinkedQueue()
    
    atual = original._head
    while atual is not None:
        valor = atual._element
        
        if valor >= 0:
            positivos.enqueue(valor)
        else:
            negativos.enqueue(valor)
            
        atual = atual._next
        
    return positivos, negativos

def imprimir(lista):
    res = []
    curr = lista._head
    while curr:
        res.append(str(curr._element))
        curr = curr._next
    return "[" + ", ".join(res) + "]"

def testar_exercicio_18():
    lista = LinkedQueue()
    lista.enqueue(10)
    lista.enqueue(-5)
    lista.enqueue(3)
    lista.enqueue(-1)
    lista.enqueue(0)
    
    print(f"Original: {imprimir(lista)}")
    
    pos, neg = separar_listas(lista)
    
    print(f"Positivos: {imprimir(pos)}") 
    print(f"Negativos: {imprimir(neg)}") 

if __name__ == "__main__":
    testar_exercicio_18()