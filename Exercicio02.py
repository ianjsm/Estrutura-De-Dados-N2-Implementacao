from Exercicio01 import ArrayStack

def exercicio_2():
    S = ArrayStack()

    S.push(5)
    print(f"push(5)") 
    print("Pilha: {S._dados}")

    S.push(3)
    print(f"push(3)") 
    print("Pilha: {S._dados}")

    print(f"pop()") 
    print("Pilha: {S._dados}")

    S.push(2)
    print(f"push(2)") 
    print("Pilha: {S._dados}")

    S.push(8)
    print(f"push(8)") 
    print("Pilha: {S._dados}")

    print(f"pop()") 
    print("Pilha: {S._dados}")

    print(f"pop()") 
    print("Pilha: {S._dados}")

    S.push(9)
    print(f"push(9)") 
    print("Pilha: {S._dados}")

    S.push(1)
    print(f"push(1)") 
    print("Pilha: {S._dados}")

    print(f"pop()") 
    print("Pilha: {S._dados}")

    S.push(7)
    print(f"push(7)") 
    print("Pilha: {S._dados}")

    S.push(6)
    print(f"push(6)") 
    print("Pilha: {S._dados}")

    print(f"pop()") 
    print("Pilha: {S._dados}")

    print(f"pop()") 
    print("Pilha: {S._dados}")

    S.push(4)
    print(f"push(4)") 
    print("Pilha: {S._dados}")

    print(f"pop()") 
    print("Pilha: {S._dados}")

    print(f"pop()") 
    print("Pilha: {S._dados}")

    print(f"Estado final da pilha: {S._dados}")
    print(f"Tamanho final: {len(S)}")

def executar():
    exercicio_2()

if __name__ == "__main__":
    executar()