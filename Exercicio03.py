from Exercicio01 import ArrayStack

def transfer(S, T):
    while not S.is_empty():
        elemento = S.pop()
        T.push(elemento)

if __name__ == "__main__":
    S = ArrayStack()
    T = ArrayStack()

    S.push(10)
    S.push(20)
    S.push(30)

    print(f"Estado inicial de S: {S._dados}")
    print(f"Estado inicial de T: {T._dados}")

    print("Transferindo S para T")
    transfer(S, T)

    print(f"Estado final de S: {S._dados}")
    print(f"Estado final de T: {T._dados}")

    if not T.is_empty():
        print(f"Novo topo de T: {T.top()}")