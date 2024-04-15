from controllers.environment.symbol import Symbol
from controllers.expressions.primitive import Primitive
from controllers.environment.types import ExpressionType
# ------------------------------------------------------------
# calclex.py
import ply.lex as lex

# List of token names.   This is always required
tokens = [
    'ID',
    'COMMENT',
    'COMMENT2',
    'NUMBER_LEX',
    'FLOAT_LEX',
    'STRING_LEX',
    'CHAR_LEX',
    'BOOLEAN',
    'TYPES',

    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'SEMICOLON',
    'COLON',
    'COMMA',
    'DOT',
    'PLUS_EQUAL',
    'MINUS_EQUAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',


    'COMPARASION',
    'EQUAL',
    'DIFFERENT',
    'GREATER',
    'LESS',
    'GREATER_EQUAL',
    'LESS_EQUAL',

    'AND',
    'OR',
    'NOT',
    'QUESTION'


]

reserved = {
    'null': 'NULL',
    # 'true': 'TRUE',
    # 'false': 'FALSE',
    'var': 'VAR',
    'const': 'CONST',

    # 'number': 'NUMBER',
    # 'string': 'STRING',
    # 'float': 'FLOAT',
    # 'char': 'CHAR',
    # 'bool': 'BOOL',

    'function': 'FUNCTION',

    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',

    'if': 'IF',
    'else': 'ELSE',

    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',

    'while': 'WHILE',

    'for': 'FOR',
    'of': 'OF',

    'push': 'PUSH',
    'pop': 'POP',
    'indexOf': 'INDEXOF',
    'join': 'JOIN',
    'length': 'LENGTH',
    'console': 'CONSOLE',
    'log': 'LOG',
    'parseInt': 'PARSEINT',
    'parseFloat': 'PARSEFLOAT',
    'toString': 'TOSTRING',
    'toLowerCase': 'TOLOWERCASE',
    'toUpperCase': 'TOUPPERCASE',
    'typeof': 'TYPEOF',


    'interface': 'INTERFACE',
    'Object': 'OBJECT',
    'keys': 'KEYS',
    'values': 'VALUES',



}

tokens = tokens + list(reserved.values())

# Regular expression rules for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r'\;'
t_COLON = r'\:'
t_COMMA = r'\,'
t_DOT = r'\.'
t_PLUS_EQUAL = r'\+\='
t_MINUS_EQUAL = r'\-\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_MOD = r'\%'

t_COMPARASION = r'\=\='
t_EQUAL = r'\='
t_DIFFERENT = r'\!\='
t_GREATER = r'\>'
t_LESS = r'\<'
t_GREATER_EQUAL = r'\>\='
t_LESS_EQUAL = r'\<\='

t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'\!'

t_QUESTION = r'\?'

# def t_TRUE(t):
#     r'true'
#     value = bool(t.value)
#     line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
#     column = t.lexpos - line
#     t.value = Primitive(value, ExpressionType.BOOLEAN, line, column)
#     return t
#
# def t_FALSE(t):
#     r'false'
#     value = bool(t.value)
#     line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
#     column = t.lexpos - line
#     t.value = Primitive(value, ExpressionType.BOOLEAN, line, column)
#     return t


def t_TYPES(t):
    r'number|string|float|char|boolean'
    if t.value == 'number':
        t.value = ExpressionType.NUMBER
    elif t.value == 'string':
        t.value = ExpressionType.STRING
    elif t.value == 'float':
        t.value = ExpressionType.FLOAT
    elif t.value == 'char':
        t.value = ExpressionType.CHAR
    elif t.value == 'boolean':
        t.value = ExpressionType.BOOLEAN
    return t


def t_BOOLEAN(t):
    r'true|false'
    value = bool(t.value)
    if t.value == 'true':
        value = True
    if t.value == 'false':
        value = False
    line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
    column = t.lexpos - line
    t.value = Primitive(value, ExpressionType.BOOLEAN, line, column)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t


def t_COMMENT(t):
    r'\/\/.*'
    t.lexer.lineno += 1
    pass


def t_COMMENT2(t):
    r'\/\*[\s\S]*?\*\/'
    t.lexer.lineno += t.value.count('\n')
    pass


def t_FLOAT_LEX(t):
    r'\d+\.\d+'
    value = float(t.value)
    line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
    column = t.lexpos - line
    t.value = Primitive(value, ExpressionType.FLOAT, line, column)
    return t


def t_NUMBER_LEX(t):
    r'\d+'
    # value = t.value.ParseInt()
    value = int(t.value)
    line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
    column = t.lexpos - line
    t.value = Primitive(value, ExpressionType.NUMBER, line, column)
    return t


def t_STRING_LEX(t):
    r'"([^"\\]|\\.)*"'
    string_value = str(t.value[1:-1])
    line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
    column = t.lexpos - line
    t.value = Primitive(string_value, ExpressionType.STRING, line, column)
    return t


def t_CHAR_LEX(t):
    r'\'[a-zA-Z0-9]\''
    string_value = str(t.value[1:-1])
    line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
    column = t.lexpos - line
    t.value = Primitive(string_value, ExpressionType.CHAR, line, column)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
# Define a rule so we can track column numbers


def t_column(t):
    r'\t+'
    t.lexer.column += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
