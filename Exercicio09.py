from Exercicio01 import ArrayStack

def eh_operador(token):
    return token in ['+', '-', '*', '/']

def converter_prefixa(expressao, destino="infixa"):
    pilha = ArrayStack()
    
    # Divide a string em tokens e INVERTE a lista
    # Ex: "+ 3 4" vira ["4", "3", "+"]
    tokens = expressao.split()
    tokens_invertidos = tokens[::-1] # Atalho do Python para inverter lista
    
    for token in tokens_invertidos:
        if not eh_operador(token):
            # É operando (número), apenas empilha
            pilha.push(token)
        else:
            # É operador, precisamos de dois operandos da pilha
            op1 = pilha.pop() # O que estava no topo (primeiro operando)
            op2 = pilha.pop() # O próximo (segundo operando)
            
            nova_string = ""
            
            if destino == "infixa":
                # Formato: (A + B)
                nova_string = f"({op1} {token} {op2})"
            
            elif destino == "posfixa":
                # Formato: A B +
                nova_string = f"{op1} {op2} {token}"
            
            # Empilha o resultado combinado
            pilha.push(nova_string)

    # O resultado final é o único item que sobra na pilha
    return pilha.pop()

def testar_exercicio_09():
    print("--- [Exercício 09] Conversor de Prefixa ---")
    
    # Exemplo 1: Soma simples
    # Prefixa: + 3 4
    expr1 = "+ 3 4"
    print(f"\nOriginal: {expr1}")
    print(f"Infixa:   {converter_prefixa(expr1, 'infixa')}")   # (3 + 4)
    print(f"Pós-fixa: {converter_prefixa(expr1, 'posfixa')}")  # 3 4 +

    # Exemplo 2: Expressão composta
    # Prefixa: * + 5 3 - 8 2 
    # Infixa esperada: ((5 + 3) * (8 - 2))
    # Cálculo: 8 * 6 = 48
    expr2 = "* + 5 3 - 8 2"
    print(f"\nOriginal: {expr2}")
    print(f"Infixa:   {converter_prefixa(expr2, 'infixa')}")
    print(f"Pós-fixa: {converter_prefixa(expr2, 'posfixa')}")

if __name__ == "__main__":
    testar_exercicio_09()