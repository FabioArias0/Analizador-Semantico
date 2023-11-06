import ply.yacc as yacc
from ply.lex import lex

# Definición de tokens
tokens = (
    'ID',
    'NUM',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'ASSIGN',
    )

# Expresiones regulares para los tokens
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_ASSIGN = r'\='


# Ignora espacios y tabulaciones
t_ignore = ' \t'

# Reglas para los numeros
def t_NUM(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t
# Función para permitirnos ver el tipo de dato en la variable
def mostrar_variables():
    print("Variables definidas:")
    for nombre, valor in variables.items():
        tipo = 'INT' if isinstance(valor, int) else 'DOUBLE'
        print(f"{nombre}: {tipo} = {valor}")

# Definir la regla para identificadores (variables)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Error al encontrar un caracter no reconocido
def t_error(t):
    print(f"Caracter no reconocido: '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex()

# Gramatica y reglas semanticas
def p_statement_assign(p):
    '''
    statement : ID ASSIGN expression
    '''
    variables[p[1]] = p[3]

def p_expression_binop(p):
    '''
    expression : expression PLUS term
               | expression MINUS term
               | term
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]

def p_term_binop(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
         | factor
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]

def p_factor_num(p):
    '''
    factor : NUM
    '''
    p[0] = p[1]

def p_factor_id(p):
    '''
    factor : ID
    '''
    value = variables.get(p[1], None)
    if value is not None:
        p[0] = value
    else:
        print(f"Variable '{p[1]}' no definida")



# Error al analizar la gramática
def p_error(p):
    print("Error de sintaxis")

# Construir el analizador sintáctico
parser = yacc.yacc()

# Función para evaluar una expresión
def evaluar(expresion):
    return parser.parse(expresion)

# Función para repetir el proceso
def repetir():
    while True:
        expresion1 = input("Ingresar expresion x (o 'q' para salir): ")
        if expresion1 == 'q':
            break
        evaluar(expresion1)
        

        expresion2 = input("Ingresar formula para y (o 'q' para salir): ")
        if expresion2 == 'q':
            break
        evaluar(expresion2)
        mostrar_variables()

        resultado = variables.get('y')
        print(f"El valor de 'y' es: {resultado}")

# Inicializar diccionario de variables
variables = {}


repetir()
