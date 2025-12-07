from Exercicio12 import LinkedQueue

def encontrar_penultimo(lista):
    """
    Exercício 13: Encontra o penúltimo nó de uma lista encadeada simples.
    Assume que a lista tem pelo menos 2 elementos.
    """
    if lista.is_empty() or lista._head._next is None:
        return None # Lista vazia ou com 1 elemento não tem penúltimo
    
    atual = lista._head
    
    # Enquanto o "próximo" do "próximo" não for None, avança.
    # Quando o loop parar, 'atual' será o penúltimo.
    while atual._next._next is not None:
        atual = atual._next
        
    return atual._element

def testar_exercicio_13():
    print("--- [Exercício 13] Encontrar Penúltimo Nó ---")
    lista = LinkedQueue()
    lista.enqueue("A")
    lista.enqueue("B")
    lista.enqueue("C") # Penúltimo deve ser B
    lista.enqueue("D") # Último
    
    print(f"Lista completa (A->B->C->D)")
    penultimo = encontrar_penultimo(lista)
    print(f"Penúltimo elemento encontrado: {penultimo}") # Esperado: C

if __name__ == "__main__":
    testar_exercicio_13()