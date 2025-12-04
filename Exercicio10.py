from Exercicio01 import ArrayStack

def calcular(expressao):
    """
    Exercício 10: Calculadora Aritmética de Inteiros usando Pilha.
    Usa notação Pós-Fixada (RPN - Reverse Polish Notation).
    Exemplo: "3 4 +" resulta em 7.
    """
    pilha = ArrayStack()
    
    # Divide a string em partes pelos espaços. 
    # Ex: "10 2 *" vira ["10", "2", "*"]
    tokens = expressao.split()

    for token in tokens:
        # Tenta converter para inteiro. Se conseguir, é número.
        try:
            numero = int(token)
            pilha.push(numero)
        except ValueError:
            # Se deu erro ao converter, assumimos que é um operador (+, -, *, /)
            # Precisamos de 2 números para operar.
            if len(pilha) < 2:
                raise Exception("Expressão mal formada: faltam operandos.")
            
            # Atenção: O primeiro pop é o SEGUNDO operando (o da direita)
            # O segundo pop é o PRIMEIRO operando (o da esquerda)
            # Ex: na pilha [10, 2], o pop tira o 2, depois o 10. Conta: 10 / 2.
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
                # Divisão inteira conforme pede o enunciado "calculadora de inteiros"
                resultado = val1 // val2
            else:
                raise Exception(f"Operador desconhecido: {token}")
            
            # Empilha o resultado para ser usado na próxima operação
            pilha.push(resultado)
            print(f"Operação: {val1} {token} {val2} = {resultado} | Pilha: {pilha._dados}")

    # Ao final, deve sobrar apenas o resultado final na pilha
    if len(pilha) != 1:
        raise Exception("Expressão mal formada: sobrou item na pilha.")
    
    return pilha.pop()

if __name__ == "__main__":
    # Teste 1: Soma simples (3 + 4) -> 3 4 +
    expr1 = "3 4 +"
    print(f"Calculando '{expr1}' -> Resultado: {calcular(expr1)}\n")

    # Teste 2: Expressão composta ((10 * 2) + 5) -> 10 2 * 5 +
    expr2 = "10 2 * 5 +"
    print(f"Calculando '{expr2}' -> Resultado: {calcular(expr2)}\n")

    # Teste 3: Complexa ((5 + 3) * (8 - 2)) -> 5 3 + 8 2 - *
    # Lógica: 
    # 5 3 + = 8
    # 8 2 - = 6
    # 8 * 6 = 48
    expr3 = "5 3 + 8 2 - *"
    print(f"Calculando '{expr3}' -> Resultado: {calcular(expr3)}\n")