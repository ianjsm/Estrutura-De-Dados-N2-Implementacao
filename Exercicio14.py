from Exercicio12 import LinkedQueue

def concatenar_listas(L, M):
    if L.is_empty():
        L._head = M._head
    elif not M.is_empty():
        atual = L._head
        while atual._next is not None:
            atual = atual._next
        
        atual._next = M._head
    
    L._size += M._size
    
    M._head = None
    M._size = 0

def imprimir_lista(lista):
    atual = lista._head
    elementos = []
    while atual is not None:
        elementos.append(str(atual._element))
        atual = atual._next
    return " -> ".join(elementos)

def testar_exercicio_14():
    L = LinkedQueue()
    L.enqueue(1)
    L.enqueue(2)
    
    M = LinkedQueue()
    M.enqueue(3)
    M.enqueue(4)
    
    print(f"Lista L: {imprimir_lista(L)}")
    print(f"Lista M: {imprimir_lista(M)}")
    
    concatenar_listas(L, M)
    print(f"L concatenada: {imprimir_lista(L)}") 

if __name__ == "__main__":
    testar_exercicio_14()