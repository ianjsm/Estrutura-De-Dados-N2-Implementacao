from Exercicio12 import CircularQueue

def contar_circular(lista):
    """
    Exercício 16: Conta nós em uma lista circularmente encadeada.
    """
    if lista.is_empty():
        return 0
    
    # Na nossa implementação CircularQueue, temos apenas _tail.
    # O head é tail.next
    primeiro_no = lista._tail._next
    atual = first_node = primeiro_no
    contador = 0
    
    while True:
        contador += 1
        atual = atual._next
        
        # Se voltamos ao início, terminamos o ciclo
        if atual is primeiro_no:
            break
            
    return contador

def testar_exercicio_16():
    print("--- [Exercício 16] Contar Lista Circular ---")
    circ = CircularQueue()
    circ.enqueue(10)
    circ.enqueue(20)
    circ.enqueue(30)
    circ.enqueue(40)
    
    print(f"Contagem detectada: {contar_circular(circ)}") # Esperado: 4

if __name__ == "__main__":
    testar_exercicio_16()