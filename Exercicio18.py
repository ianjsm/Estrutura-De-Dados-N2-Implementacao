from Exercicio12 import LinkedQueue

def separar_listas(original):
    """
    Exercício 18: Cria duas listas (Positivos e Negativos) a partir da original.
    """
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
    print("--- [Exercício 18] Separar Positivos/Negativos ---")
    lista = LinkedQueue()
    # Adicionando mix de números: 10, -5, 3, -1, 0
    lista.enqueue(10)
    lista.enqueue(-5)
    lista.enqueue(3)
    lista.enqueue(-1)
    lista.enqueue(0)
    
    print(f"Original: {imprimir(lista)}")
    
    pos, neg = separar_listas(lista)
    
    print(f"Positivos: {imprimir(pos)}") # Esperado: [10, 3, 0]
    print(f"Negativos: {imprimir(neg)}") # Esperado: [-5, -1]

if __name__ == "__main__":
    testar_exercicio_18()