'''Calculadora de Expressões Matemáticas:
Crie uma calculadora que pode avaliar expressões matemáticas complexas, incluindo parênteses e operadores aritméticos. Use pilhas para resolver as expressões.

'''



def evaluate_expression(expression):
    def precedence(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            values.append(left / right)

    operators = []
    values = []
    i = 0

    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        if expression[i] in '0123456789':
            j = i
            while i < len(expression) and expression[i] in '0123456789':
                i += 1
            values.append(int(expression[j:i]))
        elif expression[i] in "+-*/":
            while (
                operators and operators[-1] in "+-*/" and
                precedence(operators[-1]) >= precedence(expression[i])
            ):
                apply_operator(operators, values)
            operators.append(expression[i])
            i += 1
        elif expression[i] == '(':
            operators.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
            i += 1
        else:
            raise ValueError("Operador inválido: " + expression[i])

    while operators:
        apply_operator(operators, values)

    return values[0]

# Exemplo de uso:
expression = "3 + (5 * 2)"
result = evaluate_expression(expression)
print("Resultado:", result)
