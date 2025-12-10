from Exercicio12 import LinkedQueue

def contar_nos_recursivo(no):
    if no is None:
        return 0
    
    return 1 + contar_nos_recursivo(no._next)

def testar_exercicio_15():
    lista = LinkedQueue()
    lista.enqueue("X")
    lista.enqueue("Y")
    lista.enqueue("Z")
    
    qtd = contar_nos_recursivo(lista._head)
    print(f"Elementos na lista: {qtd}") 

if __name__ == "__main__":
    testar_exercicio_15()