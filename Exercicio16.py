from Exercicio12 import CircularQueue

def contar_circular(lista):
    if lista.is_empty():
        return 0

    primeiro_no = lista._tail._next
    atual = first_node = primeiro_no
    contador = 0
    
    while True:
        contador += 1
        atual = atual._next

        if atual is primeiro_no:
            break
            
    return contador

def testar_exercicio_16():
    circ = CircularQueue()
    circ.enqueue(10)
    circ.enqueue(20)
    circ.enqueue(30)
    circ.enqueue(40)
    
    print(f"Contagem detectada: {contar_circular(circ)}")

if __name__ == "__main__":
    testar_exercicio_16()