from Exercicio01 import Deque

def executar():
    print("Exercício 7")
    d = Deque()
    while True:
        print(f"\nDeque: {d._dados}")
        print("1.Inserir Inicio  2.Inserir Final")
        print("3.Remover Inicio  4.Remover Final")
        op = input("Escolha (0 para sair): ")
        
        if op == '1': d.inserir_inicio(input("Valor: "))
        elif op == '2': d.inserir_final(input("Valor: "))
        elif op == '3': print(f"Saiu: {d.remover_inicio()}")
        elif op == '4': print(f"Saiu: {d.remover_final()}")
        elif op == '0': break