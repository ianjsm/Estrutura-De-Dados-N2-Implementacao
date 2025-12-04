from Exercicio01 import ArrayStack

def inverter_lista(lista):
    """
    Exercício 5: Inverte a ordem dos elementos de uma lista usando uma Pilha.
    
    Argumentos:
    lista -- Uma lista padrão do Python (ex: [1, 2, 3])
    
    Retorno:
    A mesma lista, mas com os elementos invertidos.
    """
    S = ArrayStack()

    # Passo 1: "Ler" a lista e empilhar todos os elementos
    for elemento in lista:
        S.push(elemento)
        
    # Passo 2: "Escrever" de volta na lista removendo da pilha
    # Como a pilha devolve o último que entrou primeiro, a ordem se inverte.
    for i in range(len(lista)):
        lista[i] = S.pop()

    return lista

if __name__ == "__main__":
    # Teste com números
    numeros = [1, 2, 3, 4, 5]
    print(f"Lista Original: {numeros}")
    
    inverter_lista(numeros)
    print(f"Lista Invertida: {numeros}") # Deve ser [5, 4, 3, 2, 1]

    print("-" * 20)

    # Teste com strings (palavras)
    palavras = ["Estrutura", "de", "Dados"]
    print(f"Original: {palavras}")
    
    inverter_lista(palavras)
    print(f"Invertida: {palavras}") # Deve ser ['Dados', 'de', 'Estrutura']