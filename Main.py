import sys
import Exercicio01
import Exercicio02
import Exercicio03
import Exercicio04
import Exercicio05
import Exercicio06
import Exercicio07
import Exercicio08
import Exercicio09
import Exercicio10
import Exercicio11
import Exercicio12
import Exercicio13
import Exercicio14
import Exercicio15
import Exercicio16
import Exercicio17
import Exercicio18
import Exercicio19
import Exercicio20

def menu():
    print("\n--- MENU PRINCIPAL ---")
    for i in range(1, 21):
        print(f"{i}. Exercício {i}")
    print("0. Sair")
    return input("Escolha: ")

if __name__ == "__main__":
    while True:
        op = menu()
        if op == '0': break
        try:
            modulo = eval(f"Exercicio{op.zfill(2)}")
            modulo.executar()
        except (NameError, AttributeError, SyntaxError):
            print("Opção inválida ou exercício não encontrado.")
        except Exception as e:
            print(f"Erro na execução: {e}")