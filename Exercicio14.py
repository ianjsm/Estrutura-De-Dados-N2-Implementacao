from Exercicio12 import LinkedQueue

def concatenar_listas(L, M):
    """
    Exercício 14: Concatena lista M ao final de L.
    """
    if L.is_empty():
        L._head = M._head
    elif not M.is_empty():
        # Vamos encontrar o último nó de L navegando (jeito clássico)
        # Nota: Se usássemos L._tail seria instantâneo, mas vamos treinar navegação.
        atual = L._head
        while atual._next is not None:
            atual = atual._next
        
        # O último de L aponta para o primeiro de M
        atual._next = M._head
    
    # Atualiza o tamanho (opcional, mas bom para consistência)
    L._size += M._size
    
    # "Esvazia" M para evitar efeitos colaterais (opcional)
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
    print("--- [Exercício 14] Concatenar Listas ---")
    L = LinkedQueue()
    L.enqueue(1)
    L.enqueue(2)
    
    M = LinkedQueue()
    M.enqueue(3)
    M.enqueue(4)
    
    print(f"Lista L: {imprimir_lista(L)}")
    print(f"Lista M: {imprimir_lista(M)}")
    
    concatenar_listas(L, M)
    print(f"L concatenada: {imprimir_lista(L)}") # Esperado: 1->2->3->4

if __name__ == "__main__":
    testar_exercicio_14()