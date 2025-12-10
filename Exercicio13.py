from Exercicio12 import LinkedQueue

def encontrar_penultimo(lista):
    if lista.is_empty() or lista._head._next is None:
        return None
    
    atual = lista._head
    
    while atual._next._next is not None:
        atual = atual._next
        
    return atual._element

def testar_exercicio_13():
    lista = LinkedQueue()
    lista.enqueue("A")
    lista.enqueue("B")
    lista.enqueue("C") 
    lista.enqueue("D") 
    
    print(f"Lista completa (A->B->C->D)")
    penultimo = encontrar_penultimo(lista)
    print(f"Penultimo elemento encontrado: {penultimo}") 

if __name__ == "__main__":
    testar_exercicio_13()