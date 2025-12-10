from Exercicio12 import LinkedDeque

class DoublyLinkedListReversivel(LinkedDeque):
    def reverse(self):
        if self.is_empty():
            return

        atual = self._header
        
        while atual is not None:
            temp = atual._next
            atual._next = atual._prev
            atual._prev = temp

            atual = atual._prev

        self._header, self._trailer = self._trailer, self._header

def imprimir_reversivel(lista):
    elementos = []
    atual = lista._header._next
    while atual is not None and atual is not lista._trailer:
        elementos.append(str(atual._element))
        atual = atual._next
    return " <-> ".join(elementos)

def testar_exercicio_20():
    lista = DoublyLinkedListReversivel()
    lista.insert_last(1)
    lista.insert_last(2)
    lista.insert_last(3)
    lista.insert_last(4)
    
    print(f"Original: {imprimir_reversivel(lista)}")
    
    lista.reverse()
    
    print(f"Invertida: {imprimir_reversivel(lista)}") 

    lista.insert_last(99)
    print(f"Depois de inserir 99 no fim: {imprimir_reversivel(lista)}") 

if __name__ == "__main__":
    testar_exercicio_20()