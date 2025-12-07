from Exercicio12 import LinkedQueue

def contar_nos_recursivo(no):
    """
    Exercício 15: Algoritmo recursivo para contar nós.
    Argumento: um Nó (não a lista inteira).
    """
    # Caso Base: Se chegamos ao fim (None), soma 0
    if no is None:
        return 0
    
    # Passo Recursivo: 1 (eu mesmo) + contagem do restante
    return 1 + contar_nos_recursivo(no._next)

def testar_exercicio_15():
    print("--- [Exercício 15] Contagem Recursiva ---")
    lista = LinkedQueue()
    lista.enqueue("X")
    lista.enqueue("Y")
    lista.enqueue("Z")
    
    # Chamamos passando o HEAD da lista
    qtd = contar_nos_recursivo(lista._head)
    print(f"Elementos na lista: {qtd}") # Esperado: 3

if __name__ == "__main__":
    testar_exercicio_15()