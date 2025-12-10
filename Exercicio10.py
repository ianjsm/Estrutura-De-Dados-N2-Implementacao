from Exercicio01 import ArrayStack

def calcular(expressao):
    pilha = ArrayStack()
    
    tokens = expressao.split()

    for token in tokens:
        try:
            numero = int(token)
            pilha.push(numero)
        except ValueError:
            if len(pilha) < 2:
                print("Erro")
            val2 = pilha.pop()
            val1 = pilha.pop()
            
            resultado = 0
            
            if token == "+":
                resultado = val1 + val2
            elif token == "-":
                resultado = val1 - val2
            elif token == "*":
                resultado = val1 * val2
            elif token == "/":
                resultado = val1 // val2
            else:
                 print("Erro")

            pilha.push(resultado)
            print(f"Operação: {val1} {token} {val2} = {resultado} | Pilha: {pilha._dados}")

    if len(pilha) != 1:
         print("Erro")
    
    return pilha.pop()

if __name__ == "__main__":
    expr1 = "3 4 +"
    print(f"Calculando '{expr1}' -> Resultado: {calcular(expr1)}\n")

    expr2 = "10 2 * 5 +"
    print(f"Calculando '{expr2}' -> Resultado: {calcular(expr2)}\n")

    expr3 = "5 3 + 8 2 - *"
    print(f"Calculando '{expr3}' -> Resultado: {calcular(expr3)}\n")