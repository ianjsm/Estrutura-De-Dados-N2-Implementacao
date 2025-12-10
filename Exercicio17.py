from Exercicio12 import LinkedQueue

def reverter_recursivo(atual, anterior=None, lista_obj=None):
    if atual is None:
        if lista_obj is not None:
            lista_obj._head = anterior
        return

    proximo_original = atual._next
    
    atual._next = anterior
    
    reverter_recursivo(proximo_original, atual, lista_obj)

def imprimir_lista(lista):
    nos = []
    curr = lista._head
    while curr:
        nos.append(str(curr._element))
        curr = curr._next
    return " -> ".join(nos)

def testar_exercicio_17():
    lista = LinkedQueue()
    lista.enqueue(1)
    lista.enqueue(2)
    lista.enqueue(3)
    
    print(f"Original: {imprimir_lista(lista)}")
    
    reverter_recursivo(lista._head, None, lista)
    
    print(f"Revertida: {imprimir_lista(lista)}")

if __name__ == "__main__":
    testar_exercicio_17()