from Exercicio12 import LinkedQueue

def reverter_recursivo(atual, anterior=None, lista_obj=None):
    """
    Exercício 17: Reverte os ponteiros de uma lista encadeada recursivamente.
    
    Parâmetros:
    - atual: Nó que estamos processando
    - anterior: Nó que processamos antes (será o novo 'next')
    - lista_obj: Referência ao objeto lista principal (para atualizar o head no final)
    """
    # Caso Base: Chegamos ao fim da lista original
    if atual is None:
        # Se lista_obj foi passado, atualizamos o head para ser o último nó processado (anterior)
        if lista_obj is not None:
            lista_obj._head = anterior
        return

    # Salva quem é o próximo original antes de quebrarmos o link
    proximo_original = atual._next
    
    # Inverte o ponteiro: atual aponta para trás (anterior)
    atual._next = anterior
    
    # Chama recursão para o próximo
    reverter_recursivo(proximo_original, atual, lista_obj)

def imprimir_lista(lista):
    # Função auxiliar visual
    nos = []
    curr = lista._head
    while curr:
        nos.append(str(curr._element))
        curr = curr._next
    return " -> ".join(nos)

def testar_exercicio_17():
    print("--- [Exercício 17] Reverter Recursivo ---")
    lista = LinkedQueue()
    lista.enqueue(1)
    lista.enqueue(2)
    lista.enqueue(3)
    
    print(f"Original: {imprimir_lista(lista)}")
    
    # Chamada inicial: atual=Head, anterior=None
    reverter_recursivo(lista._head, None, lista)
    
    print(f"Revertida: {imprimir_lista(lista)}") # Esperado: 3->2->1

if __name__ == "__main__":
    testar_exercicio_17()