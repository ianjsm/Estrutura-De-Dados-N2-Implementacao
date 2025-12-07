from Exercicio12 import LinkedDeque

class DoublyLinkedListReversivel(LinkedDeque):
    """
    Exercício 20: Estende a LinkedDeque para adicionar o método reverse.
    """
    
    def reverse(self):
        """Inverte a ordem da lista trocando referências prev/next."""
        if self.is_empty():
            return

        # Começamos pelo header
        atual = self._header
        
        while atual is not None:
            # TROCA (SWAP): O next vira prev, e o prev vira next
            temp = atual._next
            atual._next = atual._prev
            atual._prev = temp
            
            # Avança para o próximo nó.
            # ATENÇÃO: Como trocamos os ponteiros, o "próximo" nó original
            # agora está guardado no atributo '_prev' do nó atual.
            atual = atual._prev

        # No final, o header antigo agora funciona como trailer (e vice-versa).
        # Precisamos trocar as referências da classe para manter a consistência.
        self._header, self._trailer = self._trailer, self._header

def imprimir_reversivel(lista):
    elementos = []
    # Navega usando next para provar que os links estão certos
    atual = lista._header._next
    while atual is not None and atual is not lista._trailer:
        elementos.append(str(atual._element))
        atual = atual._next
    return " <-> ".join(elementos)

def testar_exercicio_20():
    print("--- [Exercício 20] Reverse In-Place ---")
    lista = DoublyLinkedListReversivel()
    lista.insert_last(1)
    lista.insert_last(2)
    lista.insert_last(3)
    lista.insert_last(4)
    
    print(f"Original: {imprimir_reversivel(lista)}")
    
    lista.reverse()
    
    print(f"Invertida: {imprimir_reversivel(lista)}") # Esperado: 4 <-> 3 <-> 2 <-> 1
    
    # Teste extra: Inserir após reverter para garantir que header/trailer estão certos
    lista.insert_last(99)
    print(f"Após inserir 99 no fim: {imprimir_reversivel(lista)}") 
    # Esperado: 4 <-> 3 <-> 2 <-> 1 <-> 99

if __name__ == "__main__":
    testar_exercicio_20()