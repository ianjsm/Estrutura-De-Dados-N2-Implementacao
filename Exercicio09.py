from Exercicio01 import ArrayStack

def eh_operador(token):
    return token in ['+', '-', '*', '/']

def converter_prefixa(expressao, destino="infixa"):
    pilha = ArrayStack()

    tokens = expressao.split()
    tokens_invertidos = tokens[::-1]
    
    for token in tokens_invertidos:
        if not eh_operador(token):
            pilha.push(token)
        else:
            op1 = pilha.pop()
            op2 = pilha.pop() 
            
            nova_string = ""
            
            if destino == "infixa":
                nova_string = f"({op1} {token} {op2})"
            
            elif destino == "posfixa":
                nova_string = f"{op1} {op2} {token}"
            
            pilha.push(nova_string)

    return pilha.pop()

def testar_exercicio_09():

    expr1 = "+ 3 4"
    print(f"\nOriginal: {expr1}")
    print(f"Infixa:   {converter_prefixa(expr1, 'infixa')}")  
    print(f"Pós fixa: {converter_prefixa(expr1, 'posfixa')}") 

    expr2 = "* + 5 3 - 8 2"
    print(f"\nOriginal: {expr2}")
    print(f"Infixa:   {converter_prefixa(expr2, 'infixa')}")
    print(f"Pós fixa: {converter_prefixa(expr2, 'posfixa')}")

if __name__ == "__main__":
    testar_exercicio_09()