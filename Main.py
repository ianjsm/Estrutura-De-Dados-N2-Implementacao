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
    print("1.  Exercicio 02")
    print("2.  Exercicio 03")
    print("3.  Exercicio 04")
    print("4.  Exercicio 05")
    print("5.  Exercicio 06")
    print("6.  Exercicio 07")
    print("7.  Exercicio 08")
    print("8.  Exercicio 09")
    print("9.  Exercicio 10")
    print("10. Exercicio 11")
    print("12. Exercicio 13")
    print("13. Exercicio 14")
    print("14. Exercicio 15")
    print("15. Exercicio 16")
    print("16. Exercicio 17")
    print("17. Exercicio 18")
    print("18. Exercicio 19")
    print("19. Exercicio 20")
    print("0.  Sair")
    return input("Escolha uma opcao: ")

if __name__ == "__main__":
    while True:
        try:
            opcao = exibir_menu()
            
            if opcao == '0':
                break

            elif opcao == '1': 
                Exercicio02.exercicio_2()
            elif opcao == '2': 
                from Exercicio01 import ArrayStack
                s, t = ArrayStack(), ArrayStack()
                s.push(1); s.push(2); s.push(3)
                print(f"S original: {s._dados}")
                Exercicio03.transfer(s, t)
                print(f"T final: {t._dados}")

            elif opcao == '3': 
                Exercicio04.testar_exercicio_04()
            elif opcao == '4': 
                Exercicio05.testar_exercicio_05()
            elif opcao == '5': 
                Exercicio06.testar_exercicio_06()
            elif opcao == '6': 
                Exercicio07.testar_exercicio_07()
            elif opcao == '7': 
                Exercicio08.testar_exercicio_08()
            elif opcao == '8': 
                Exercicio09.testar_exercicio_09()
            elif opcao == '9': 
                print(Exercicio10.calcular("3 4 + 5 *"))
            elif opcao == '10': 
                Exercicio11.testar_exercicio_11()
            elif opcao == '12': 
                Exercicio13.testar_exercicio_13()
            elif opcao == '13': 
                Exercicio14.testar_exercicio_14()
            elif opcao == '14': 
                Exercicio15.testar_exercicio_15()
            elif opcao == '15': 
                Exercicio16.testar_exercicio_16()
            elif opcao == '16': 
                Exercicio17.testar_exercicio_17()
            elif opcao == '17': 
                Exercicio18.testar_exercicio_18()
            elif opcao == '18': 
                Exercicio19.testar_exercicio_19()
            elif opcao == '19': 
                Exercicio20.testar_exercicio_20()
            
            else:
                print("Erro")
                
            input("Pressione enter para continuar")

        except Exception as e:
            print(f"Erro")
            input("Enter para voltar ao menu")