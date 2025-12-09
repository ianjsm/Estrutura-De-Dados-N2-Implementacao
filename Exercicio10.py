from Exercicio01 import Pilha

def calcular_rpn(expr):
    p = Pilha()
    for token in expr.split():
        try:
            p.empilhar(int(token))
        except ValueError:
            val2 = p.desempilhar()
            val1 = p.desempilhar()
            if token == '+': r = val1 + val2
            elif token == '-': r = val1 - val2
            elif token == '*': r = val1 * val2
            elif token == '/': r = val1 // val2
            p.empilhar(r)
    return p.desempilhar()

def executar():
    print("Exercício 10")
    expr = input("Digite a expressão (ex: 3 4 +): ")
    try:
        print(f"Resultado: {calcular_rpn(expr)}")
    except:
        print("Erro no cálculo.")