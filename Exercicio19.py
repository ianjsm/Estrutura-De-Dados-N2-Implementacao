from Exercicio12 import LinkedDeque

def remover_duplicatas(lista):
    vistos = set()

    atual = lista._header._next
    
    while atual is not lista._trailer:
        elemento = atual._element
        proximo_no = atual._next 
        
        if elemento in vistos:
            lista._delete_node(atual)
        else:
            vistos.add(elemento)
            
        atual = proximo_no

def imprimir_deque(deque):
    elementos = []
    atual = deque._header._next
    while atual is not deque._trailer:
        elementos.append(str(atual._element))
        atual = atual._next
    return " <-> ".join(elementos)

def testar_exercicio_19():
    lista = LinkedDeque()
    
    lista.insert_last("A")
    lista.insert_last("B")
    lista.insert_last("A") 
    lista.insert_last("C")
    lista.insert_last("B") 
    lista.insert_last("D")
    
    print(f"Original:  {imprimir_deque(lista)}")
    
    remover_duplicatas(lista)
    
    print(f"Sem dup:  {imprimir_deque(lista)}")

if __name__ == "__main__":
    testar_exercicio_19()