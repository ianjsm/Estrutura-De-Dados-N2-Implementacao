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

def exibir_menu():
    print("\n" + "="*40)
    print("   TRABALHO DE ESTRUTURA DE DADOS")
    print("="*40)
    print("1.  Ex 02: Operações Pilha (Teste de Mesa)")
    print("2.  Ex 03: Transferir Elementos (Pilha)")
    print("3.  Ex 04: Esvaziar Recursivo")
    print("4.  Ex 05: Inverter Lista")
    print("5.  Ex 06: Operações Fila (Teste de Mesa)")
    print("6.  Ex 07: Operações Deque (Teste de Mesa)")
    print("7.  Ex 08: Verificar Parênteses")
    print("8.  Ex 09: Conversor Prefixa -> Infixa/Pós")
    print("9.  Ex 10: Calculadora RPN")
    print("10. Ex 11: Palíndromo (Pilha + Fila)")
    print("11. Ex 12: Teste Estruturas Encadeadas")
    print("12. Ex 13: Encontrar Penúltimo Nó")
    print("13. Ex 14: Concatenar Listas")
    print("14. Ex 15: Contar Nós (Recursivo)")
    print("15. Ex 16: Contar Nós (Circular)")
    print("16. Ex 17: Reverter Lista (Recursivo)")
    print("17. Ex 18: Separar Positivos/Negativos")
    print("18. Ex 19: Remover Duplicatas (Dupla)")
    print("19. Ex 20: Reverse In-Place (Dupla)")
    print("0.  Sair")
    print("-" * 40)
    return input("Escolha uma opção: ")

if __name__ == "__main__":
    while True:
        try:
            opcao = exibir_menu()
            
            if opcao == '0':
                print("\nSaindo... Bom trabalho!")
                break
            
            # Bloco de Arrays
            elif opcao == '1': Exercicio02.exercicio_2()
            elif opcao == '2': 
                # Recriando teste rápido pois Ex03 original era script direto
                from Exercicio01 import ArrayStack
                s, t = ArrayStack(), ArrayStack()
                s.push(1); s.push(2); s.push(3)
                print(f"S original: {s._dados}")
                Exercicio03.transfer(s, t)
                print(f"T final: {t._dados}")

            elif opcao == '3': Exercicio04.testar_exercicio_04() # Ajustar nome se necessário
            elif opcao == '4': Exercicio05.testar_exercicio_05()
            
            # Bloco de Filas/Deques
            elif opcao == '5': Exercicio06.testar_exercicio_06()
            elif opcao == '6': Exercicio07.testar_exercicio_07()
            
            # Aplicações
            elif opcao == '7': Exercicio08.testar_exercicio_08()
            elif opcao == '8': Exercicio09.testar_exercicio_09()
            elif opcao == '9': 
                # Teste rápido calculadora
                print(Exercicio10.calcular("3 4 + 5 *"))

            elif opcao == '10': Exercicio11.testar_exercicio_11()
            
            # Bloco Encadeado
            elif opcao == '11': Exercicio12.testar_exercicio_12()
            elif opcao == '12': Exercicio13.testar_exercicio_13()
            elif opcao == '13': Exercicio14.testar_exercicio_14()
            elif opcao == '14': Exercicio15.testar_exercicio_15()
            elif opcao == '15': Exercicio16.testar_exercicio_16()
            elif opcao == '16': Exercicio17.testar_exercicio_17()
            elif opcao == '17': Exercicio18.testar_exercicio_18()
            elif opcao == '18': Exercicio19.testar_exercicio_19()
            elif opcao == '19': Exercicio20.testar_exercicio_20()
            
            else:
                print("Opção inválida, tente novamente.")
                
            input("\n[Pressione Enter para continuar...]")

        except Exception as e:
            print(f"\nOcorreu um erro na execução: {e}")
            input("[Enter para voltar ao menu]")