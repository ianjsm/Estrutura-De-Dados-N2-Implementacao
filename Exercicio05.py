from Exercicio01 import ArrayStack

def inverter_lista(lista):
    S = ArrayStack()

    for elemento in lista:
        S.push(elemento)
        
    for i in range(len(lista)):
        lista[i] = S.pop()

    return lista

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5]
    print(f"Lista original: {numeros}")
    
    inverter_lista(numeros)
    print(f"Lista inversa: {numeros}")

    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")

    palavras = ["Maça", "Banana", "Atum"]
    print(f"Original: {palavras}")
    
    inverter_lista(palavras)
    print(f"Invertida: {palavras}")