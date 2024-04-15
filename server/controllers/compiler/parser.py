import ply.yacc as yacc
import numpy as np
from controllers.compiler.lexer import tokens
from controllers.compiler.lexer import lexer
from controllers.expressions.operation import Operation
from controllers.instructions.declaration import Declaration
from controllers.expressions.access import Access
from controllers.expressions.ternary import Ternary
from controllers.instructions.print import Print
from controllers.instructions.assignment import Assignment
from controllers.instructions.array_declaration import ArrayDeclaration
from controllers.expressions.primitive import Primitive
from controllers.environment.types import ExpressionType
from controllers.expressions.access_array import AccessArray
from controllers.instructions.array_assignment import ArrayAssignment
from controllers.instructions.push import Push
from controllers.expressions.vector_functions import VectorFunctions
from controllers.expressions.embed_functions import EmbedFunctions
from controllers.instructions.if_instruction import If
from controllers.instructions.for_instruction import For
from controllers.instructions.for_each_instruction import ForEach
from controllers.instructions.while_instruction import While
from controllers.instructions.switch import Switch
from controllers.instructions.break_statement import Break
from controllers.instructions.continue_statement import Continue
from controllers.instructions.interface import Interface
from controllers.instructions.interface_assignment import InterfaceAssignment
from controllers.expressions.access_object_atribute import AccessObjectAtribute
from controllers.instructions.modify_object_attribute import ModifyObjectAttribute
from controllers.instructions.function import Function
from controllers.expressions.returns import Return
from controllers.expressions.call_function import CallFunction
from controllers.instructions.sintactic_error import SyntaxError
from controllers.instructions.empty import Empty
# from controllers.environment.environment import Environment
# from controllers.environment.ast import Ast
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'COMPARASION', 'DIFFERENT'),
    ('left', 'GREATER', 'LESS', 'GREATER_EQUAL', 'LESS_EQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'DIVIDE', 'MOD', 'TIMES'),
    ('right', 'UNOT', 'UMINUS'),

)


def p_start(p):
    '''start : block'''
    p[0] = p[1]


def p_init(p):
    '''block : block instruction
            | instruction'''
    if len(p) == 3:
        p[1].append(p[2])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_instruction(p):
    '''instruction  : assignment
                    | declaration
                    | declaration_array
                    | declaration_matrix
                    | vector_functions
                    | interface
                    | function
                    | call_function
                    | declaration_interface
                    | interface_attribute
                    | if_statement
                    | switch
                    | while
                    | for
                    | foreach
                    | break
                    | continue
                    | return
                    | print
                    | empty
    '''
    p[0] = p[1]

def p_instruction_error(p):
    '''instruction : exp SEMICOLON'''
    print("Error en la instruccion")
    position = get_params(p)
    p[0] = SyntaxError(
        "Se esperaba ';' pero se encontro '" + p[1].value + "'",
        "instruccion",
        "Sintactico", 
        position.line,
        position.column
            )

#######################################################################
# functions
def p_function_error(p):
    '''function : FUNCTION error RBRACE'''
    position = get_params(p)
    p[0] = SyntaxError(
        "Se esperaba '}' pero se encontro '" + p[2].value + "'",
        "funcion",
        "Sintactico", 
        position.line,
        position.column
            )
def p_function_error2(p):
    '''function : FUNCTION ID LPAREN parameters RPAREN return_type LBRACE error RBRACE'''
    position = get_params(p)
    p[0] = SyntaxError(
        "Se esperaba '}' pero se encontro '" + p[8].value + "'",
        "funcion",
        "Sintactico", 
        position.line,
        position.column
            )


def p_function(p):
    '''function : FUNCTION ID LPAREN parameters RPAREN return_type LBRACE  block RBRACE'''
    position = get_params(p)
    p[0] = Function(p[2], p[4], p[6],p[8], position.line, position.column)
def p_parameters(p):
    '''parameters : parameters_list
                  | empty'''
    if isinstance(p[1], list):
        p[0] = p[1]
    else:
        p[0] = None

def p_parameters_list(p):
    '''parameters_list : parameters_list COMMA parameter
                  | parameter'''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_parameter(p):
    '''parameter : ID COLON type LBRACKET RBRACKET
                 | ID COLON type'''
    if len(p) == 6:
        p[0] = [p[1],ExpressionType.ARRAY, p[3]]
    else:
        p[0] = [p[1], p[3]]

def p_return_types(p):
    '''return_type : COLON type LBRACKET RBRACKET
                    | COLON type
                    | empty
    '''
    if len(p) == 5:
        p[0] = [ExpressionType.ARRAY,p[2]]
    elif len(p) == 3:
        p[0] = [p[2]]
    else:
        p[0] = None
#######################################################################
# call function

def p_call_function_error(p):
    '''call_function : ID LPAREN error SEMICOLON'''
    position = get_params(p)
    p[0] = SyntaxError(
        "Se esperaba una lista de parametros pero se encontro '" + p[3].value + "'",
        "funcion",
        "Sintactico", 
        position.line,
        position.column
            )

def p_call_function(p):
    '''call_function : ID LPAREN exp_list RPAREN SEMICOLON'''
    position = get_params(p)
    p[0] = CallFunction(p[1], p[3], position.line, position.column)
def p_call_function2(p):
    '''call_function : ID LPAREN RPAREN SEMICOLON'''
    position = get_params(p)
    p[0] = CallFunction(p[1], [], position.line, position.column)

#######################################################################
# switch case

def p_switch_error(p):
    '''switch : SWITCH error RBRACE'''
    position = get_params(p)
    p[0] = SyntaxError(
        "Se esperaba '}' pero se encontro '" + p[2].value + "'",
        "switch",
        "Sintactico", 
        position.line,
        position.column
            )

def p_switch(p):
    '''switch : SWITCH LPAREN exp RPAREN LBRACE cases RBRACE'''
    position = get_params(p)
    p[0] = Switch(p[3], p[6], position.line, position.column)

def p_cases(p):
    '''cases : cases case
            | case'''
    if len(p) == 3:
        p[1].append(p[2])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_case(p):
    '''case : CASE exp COLON block
            | DEFAULT COLON block'''
    if len(p) == 5:
        p[0] = [p[2], p[4]]
    else:
        p[0] = [None, p[3]]
#######################################################################
# if

def p_if_error(p):
    '''if_statement : IF error RBRACE'''
    position = get_params(p)
    p[0] = SyntaxError(
        "Se esperaba '}' pero se encontro '" + p[2].value + "'",
        "if",
        "Sintactico", 
        position.line,
        position.column
            )

def p_if_statement(p):
    '''if_statement : if'''
    position = get_params(p)
    p[0] = If(p[1], position.line, position.column)


def p_if_1(p):
    '''if : IF LPAREN exp RPAREN LBRACE block RBRACE ELSE if'''
    p[0] = [[p[3], p[6]]] + p[9]


def p_if_3(p):
    '''if : IF LPAREN exp RPAREN LBRACE block RBRACE'''
    p[0] = [[p[3], p[6]]]


def p_if_2(p):
    '''if : IF LPAREN exp RPAREN LBRACE block RBRACE ELSE LBRACE block RBRACE'''
    position = get_params(p)
    p[0] = [[p[3], p[6]], [Primitive(
        True, ExpressionType.BOOLEAN, position.line,position.column), p[10]]]


#######################################################################
# while


def p_while_error(p):
    '''while : WHILE error RBRACE'''
    position = get_params(p)
    p[0] = SyntaxError(
        "Se esperaba '}' pero se encontro '" + p[2].value + "'",
        "while",
        "Sintactico", 
        position.line,
        position.column
            )

def p_while(p):
    '''while : WHILE LPAREN exp RPAREN LBRACE block RBRACE'''
    position = get_params(p)
    p[0] = While(p[3], p[6], position.line, position.column)

#######################################################################
# for


def p_for(p):
    '''for : FOR LPAREN declaration exp SEMICOLON increment_decrement RPAREN LBRACE block RBRACE'''
    position = get_params(p)
    p[0] = For(p[3], p[4], p[6], p[9], position.line, position.column)

def p_increment_decrement(p):
    '''increment_decrement : ID PLUS PLUS
                            | ID MINUS MINUS'''
    # p[0] = [p[1], p[2]]
    if p[2] == '+':
        p[0] = [p[1], '++']
    else:
        p[0] = [p[1], '--']


#######################################################################
# for each


def p_foreach(p):
    '''foreach : FOR LPAREN VAR ID OF ID RPAREN block'''
    position = get_params(p)
    p[0] = ForEach(p[4], p[6], p[8], position.line, position.column)
#######################################################################
# break

def p_break_error(p):
    '''break : BREAK error SEMICOLON'''
    position = get_params(p)
    p[0] = SyntaxError(
        "Se esperaba ';' pero se encontro '" + p[2].value + "'",
        "break",
        "Sintactico", 
        position.line,
        position.column
            )

def p_break(p):
    '''break : BREAK SEMICOLON'''
    position = get_params(p)
    p[0] = Break(position.line, position.column)
#######################################################################
# continue

def p_continue_error(p):
    '''continue : CONTINUE error SEMICOLON'''
    position = get_params(p)
    p[0] = SyntaxError(
        "Se esperaba ';' pero se encontro '" + p[2].value + "'",
        "continue",
        "Sintactico", 
        position.line,
        position.column
            )

def p_continue(p):
    '''continue : CONTINUE SEMICOLON'''
    position = get_params(p)
    p[0] = Continue(position.line, position.column)
#######################################################################
# return

def p_return_error(p):
    '''return : RETURN error SEMICOLON'''
    position = get_params(p)
    p[0] = SyntaxError(
        "Se esperaba ';' pero se encontro '" + p[2].value + "'",
        "return",
        "Sintactico", 
        position.line,
        position.column
            )

def p_return(p):
    '''return : RETURN exp SEMICOLON
              | RETURN SEMICOLON'''
    position = get_params(p)
    if len(p) == 4:
        p[0] = Return(p[2], position.line, position.column)
    else:
        p[0] = Return(None, position.line, position.column)
#######################################################################
# print

def p_print_error(p):
    '''print : CONSOLE error SEMICOLON'''
    position = get_params(p)
    p[0] = SyntaxError(
        "Se esperaba ';' pero se encontro '" + p[2].value + "'",
        "log",
        "Sintactico",
        position.line,
        position.column
            )

def p_instruction_console(p):
    '''
    print : CONSOLE DOT LOG LPAREN exp_list RPAREN SEMICOLON
    '''
    position = get_params(p)
    p[0] = Print(p[5], position.line, position.column)

#######################################################################
# Interface

def p_interface_error1(p):
    '''interface : INTERFACE error RBRACE'''
    position = get_params(p)
    p[0] = SyntaxError(
        "Se esperaba '}' pero se encontro '" + p[2].value +"'",
        "interface",
        "Sintactico", 
        position.line,
        position.column
            )


def p_interface(p):
    '''interface : INTERFACE ID LBRACE interface_body RBRACE'''
    position = get_params(p)
    p[0] = Interface(p[2], p[4], position.line, position.column)

def p_interface_body(p):
    '''interface_body : interface_body SEMICOLON ID COLON interface_type
                      | ID COLON interface_type'''
    if len(p) == 6:
        p[1].append([p[3], p[5]])
        p[0] = p[1]
    else:
        p[0] = [[p[1], p[3]]]

def p_interface_type(p):
    '''interface_type : ID
            | type'''
    p[0] = p[1]

#######################################################################
# declaration interface

def p_declaration_interface(p):
    '''declaration_interface : VAR ID COLON ID EQUAL LBRACE declaration_interface_body RBRACE SEMICOLON'''
    position = get_params(p)
    p[0] = InterfaceAssignment(False, p[2], p[4], p[7], position.line, position.column)
def p_declaration_interface1(p):
    '''declaration_interface : CONST ID COLON ID EQUAL LBRACE declaration_interface_body RBRACE SEMICOLON'''
    position = get_params(p)
    p[0] = InterfaceAssignment(True, p[2], p[4], p[7], position.line, position.column)
def p_declaration_interface_body(p):
    '''declaration_interface_body : declaration_interface_body COMMA ID COLON exp
                                  | ID COLON exp'''
    if len(p) == 6:
        p[1].append([p[3], p[5]])
        p[0] = p[1]
    else:
        p[0] = [[p[1], p[3]]]
#######################################################################
# interface attribute

def p_interface_attribute_error(p):
    '''interface_attribute : interface_object error SEMICOLON'''
    position = get_params(p)
    p[0] = SyntaxError(
        "Se esperaba una asignacion pero se encontro '" + p[2].value + "'",
        "asignacion",
        "Sintactico", 
        position.line,
        position.column
            )

def p_interface_attribute(p):
    '''interface_attribute : interface_object EQUAL exp SEMICOLON'''
    position = get_params(p)
    p[0] = ModifyObjectAttribute(p[1], p[3], position.line, position.column)

def p_interface_attribute1(p):
    '''interface_object : interface_object DOT ID
                        | ID DOT ID'''
    if not isinstance(p[1],str):
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1],p[3]]

#######################################################################
# declaration vector
def p_declaration_array(p):
    '''declaration_array : VAR ID COLON type LBRACKET RBRACKET EQUAL definition_array SEMICOLON'''
    position = get_params(p)
    p[0] = ArrayDeclaration(False, p[2], p[4], 1, p[8],
                            position.line, position.column)

def p_declaration_array_error(p):
    '''declaration_array : VAR ID COLON type LBRACKET RBRACKET EQUAL error SEMICOLON'''
    print("Error en la declaracion de array ")
    position = get_params(p)
    p[0] = Primitive(
        ExpressionType.NULL.name, ExpressionType.NULL, position.line, position.column)

def p_declaration_array2(p):
    '''declaration_array : CONST ID COLON type LBRACKET RBRACKET EQUAL definition_array SEMICOLON'''
    position = get_params(p)
    p[0] = ArrayDeclaration(True, p[2], p[4], 1, p[8],
                            position.line, position.column)


def p_defination_array(p):
    '''definition_array : LBRACKET exp_list RBRACKET
                        | LBRACKET RBRACKET
                        | exp'''
    if len(p) == 4:
        p[0] = p[2]
    elif len(p) == 3:
        p[0] = []
    elif len(p) == 2:
        p[0] = p[1]


#######################################################################
# declaration matrix


def p_declaration_matrix(p):
    '''declaration_matrix : VAR ID COLON type matrix_dimension EQUAL LBRACKET values_list RBRACKET SEMICOLON'''
    position = get_params(p)
    p[0] = ArrayDeclaration(False, p[2], p[4], p[5],
                            p[8], position.line, position.column)


def p_declaration_matrix2(p):
    '''declaration_matrix : CONST ID COLON type matrix_dimension EQUAL LBRACKET values_list RBRACKET SEMICOLON'''
    position = get_params(p)
    p[0] = ArrayDeclaration(True, p[2], p[4], p[5],
                            p[8], position.line, position.column)


def p_matrix_dimension(p):
    '''matrix_dimension : matrix_dimension LBRACKET RBRACKET
                        | LBRACKET RBRACKET LBRACKET RBRACKET'''
    if len(p) == 4:
        p[0] = p[1] + 1
    else:
        p[0] = 2


def p_values_list(p):
    '''values_list : values_list COMMA LBRACKET arg RBRACKET
                    | LBRACKET arg RBRACKET'''
    if len(p) == 6:
        p[1].append(p[4])
        p[0] = p[1]
    else:
        p[0] = [p[2]]


def p_arg(p):
    '''arg : values_list
            | exp_list'''
    p[0] = p[1]

#######################################################################
# vector functions
# def p_vector_functions_error(p):
#     '''vector_functions : ID DOT error  SEMICOLON'''
#     p[0] = SintacticError(
#         "Se esperaba ';' pero se encontro " + p[3].value,
#         "funcion de vector",
#         "Sintactico", 
#         p.lineno(1),
#         p.lexpos(1)
#     )

def p_vector_functions(p):
    '''vector_functions : ID DOT PUSH LPAREN exp RPAREN SEMICOLON'''
    position = get_params(p)
    p[0] = Push(p[1], p[5], position.line, position.column)


def p_vector_expression(p):
    '''exp : ID DOT POP LPAREN RPAREN'''
    position = get_params(p)
    p[0] = VectorFunctions(p[1], p[3], p[5], position.line, position.column)


def p_vector_expression2(p):
    '''exp : ID DOT INDEXOF LPAREN exp RPAREN'''
    position = get_params(p)
    p[0] = VectorFunctions(p[1], p[3], p[5], position.line, position.column)


def p_vector_expression3(p):
    '''exp : ID DOT JOIN LPAREN RPAREN'''
    position = get_params(p)
    p[0] = VectorFunctions(p[1], p[3], p[5], position.line, position.column)


def p_vector_expression4(p):
    '''exp : ID DOT LENGTH'''
    position = get_params(p)
    p[0] = VectorFunctions(p[1], p[3], p[3], position.line, position.column)
#######################################################################
# embed functions


def p_embed_functions(p):
    '''exp : PARSEINT LPAREN exp RPAREN'''
    position = get_params(p)
    p[0] = EmbedFunctions(p[1], p[3], position.line, position.column)


def p_embed_functions2(p):
    '''exp : PARSEFLOAT LPAREN exp RPAREN'''
    position = get_params(p)
    p[0] = EmbedFunctions(p[1], p[3], position.line, position.column)


def p_embed_functions3(p):
    '''exp : exp DOT TOSTRING LPAREN RPAREN'''
    position = get_params(p)
    p[0] = EmbedFunctions(p[3], p[1], position.line, position.column)


def p_embed_functions3_1(p):
    '''exp : ID DOT TOSTRING LPAREN RPAREN'''
    position = get_params(p)
    p[0] = EmbedFunctions(p[3], p[1], position.line, position.column)


def p_embed_functions4(p):
    '''exp : exp DOT TOLOWERCASE LPAREN RPAREN'''
    position = get_params(p)
    p[0] = EmbedFunctions(p[3], p[1], postion.line, position.column)


def p_embed_functions4_1(p):
    '''exp : ID DOT TOLOWERCASE LPAREN RPAREN'''
    position = get_params(p)
    p[0] = EmbedFunctions(p[3], p[1], position.line, position.column)


def p_embed_functions5(p):
    '''exp : exp DOT TOUPPERCASE LPAREN RPAREN'''
    position = get_params(p)
    p[0] = EmbedFunctions(p[3], p[1], position.line, position.column)


def p_embed_functions5_1(p):
    '''exp : ID DOT TOUPPERCASE LPAREN RPAREN'''
    position = get_params(p)
    p[0] = EmbedFunctions(p[3], p[1], position.line, position.column)


def p_embed_functions6(p):
    '''exp : TYPEOF exp'''
    position = get_params(p)
    p[0] = EmbedFunctions(p[1], p[2], position.line, position.column)


def p_embed_functions7(p):
    '''exp : OBJECT DOT VALUES LPAREN exp RPAREN'''
    position = get_params(p)
    p[0] = EmbedFunctions(p[3], p[5], position.line, position.column)


def p_embed_functions8(p):
    '''exp : OBJECT DOT KEYS LPAREN exp RPAREN'''
    position = get_params(p)
    p[0] = EmbedFunctions(p[3], p[5], position.line, position.column)
#######################################################################
# declaration const

def p_declaration_const_error(p):
    '''declaration : CONST error SEMICOLON'''
    position = get_params(p)
    p[0] = SyntaxError(
        "Se esperaba una declaracion pero se encontro '" + p[2].value + "'",
        "declaracion",
        "Sintactico", 
        position.line,
        position.column
            )

def p_declaration_const(p):
    '''declaration : CONST ID COLON type EQUAL exp SEMICOLON'''
    position = get_params(p)
    p[0] = Declaration(p[2], p[6], p[4], position.line, position.column, True)


def p_declaration_const2(p):
    '''declaration : CONST ID EQUAL exp SEMICOLON'''
    position = get_params(p)
    p[0] = Declaration(p[2], p[4], None, position.line, position.column, True)

#######################################################################
# declaration

def p_declaration_error(p):
    '''declaration : VAR error SEMICOLON'''
    position = get_params(p)
    p[0] = SyntaxError(
        "Se esperaba ';' pero se encontro '" + p[2].value + "'",
        "declaracion",
        "Sintactico", 
        position.line,
        position.column
            )

# declaration with type and value

def p_declaration(p):
    '''declaration : VAR ID COLON type EQUAL exp SEMICOLON'''
    position = get_params(p)
    p[0] = Declaration(p[2], p[6], p[4], position.line, position.column)
# declaration with value


def p_declaration2(p):
    '''declaration : VAR ID EQUAL exp SEMICOLON '''
    position = get_params(p)
    p[0] = Declaration(p[2], p[4], None, position.line, position.column)
# declaration with type and without value


def p_declaration3(p):
    '''declaration : VAR ID COLON type SEMICOLON'''
    position = get_params(p)
    p[0] = Declaration(p[2], None, p[4], position.line, position.column)


# def p_declaration5(p):
#     '''declaration : VAR error SEMICOLON
#     '''
#     print(f"Error de asignacion line: {p[2].lineno}, column: {p[2].lexpos} ")
#######################################################################
# assignment

def p_declaration4_error(p):
    '''assignment : ID error SEMICOLON'''
    position = get_params(p)
    p[0] = SyntaxError(
        "Se esperaba ';' pero se encontro '" + p[2].value + "'",
        "asignacion",
        "Sintactico", 
        position.line,
        position.column
    )

def p_declaration4(p):
    '''assignment : ID EQUAL exp SEMICOLON
                | ID PLUS_EQUAL exp SEMICOLON
                | ID MINUS_EQUAL exp SEMICOLON '''
    position = get_params(p)
    p[0] = Assignment(p[1], p[2], p[3], position.line, position.column)

def p_declaration5(p):
    '''assignment : ID index_list EQUAL exp SEMICOLON'''
    position = get_params(p)
    p[0] = ArrayAssignment(p[1], p[2], p[4], position.line, position.column)


def p_index_list(p):
    '''index_list : index_list LBRACKET exp RBRACKET
                | LBRACKET exp RBRACKET'''
    if len(p) == 5:
        p[1].append(p[3])
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = [p[2]]
#######################################################################
# types


def p_type(p):
    '''type : TYPES '''
    p[0] = p[1]

#######################################################################
# expressions


def p_exp_list(p):
    '''exp_list : exp_list COMMA exp
                | exp'''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_exp_plus(p):
    '''exp : exp PLUS exp
            | exp MINUS exp
            | exp TIMES exp
            | exp DIVIDE exp
            | exp MOD exp'''

    position = get_params(p)
    p[0] = Operation(p[1], p[2], p[3], position.line, position.column)


def p_exp_unary(p):
    '''exp : MINUS exp %prec UMINUS
            | NOT exp %prec UNOT'''
    position = get_params(p)
    if p[1] == '-':
        p[0] = Operation(None, '--', p[2], position.line, position.column)
    if p[1] == '!':
        p[0] = Operation(None, '!', p[2], position.line, position.column)


def p_exp_comparation(p):
    '''exp : exp COMPARASION exp
            | exp DIFFERENT exp
            | exp GREATER exp
            | exp LESS exp
            | exp GREATER_EQUAL exp
            | exp LESS_EQUAL exp
            | exp AND exp
            | exp OR exp
    '''
    position = get_params(p)
    p[0] = Operation(p[1], p[2], p[3], position.line, position.column)

def p_exp_function(p):
    '''exp : ID LPAREN exp_list RPAREN'''
    position = get_params(p)
    p[0] = CallFunction(p[1], p[3], position.line, position.column)

def p_exp_function2(p):
    '''exp : ID LPAREN RPAREN'''
    position = get_params(p)
    p[0] = CallFunction(p[1], [], position.line, position.column)

def p_exp_literals(p):
    '''exp : NUMBER_LEX
            | FLOAT_LEX
            | STRING_LEX
            | CHAR_LEX
            | BOOLEAN
            | list_access
    '''
    position = get_params(p)
    if isinstance(p[1], Primitive):
        # print("entro",position.line)
        p[1].symbol.line = position.line
        p[1].symbol.col = position.column

    p[0] = p[1]

# #######################################################################
def p_list_access(p):
    '''list_access : list_access LBRACKET exp RBRACKET
                | list_access DOT ID
                | ID DOT ID
                | ID
    '''
    position = get_params(p)
    if len(p) == 5:
        if isinstance(p[1], Access):
            access = AccessArray(p[1], position.line, position.column)
            access.indexes.append(p[3])
            p[0] = access
        elif isinstance(p[1], AccessArray):
            p[1].indexes.append(p[3])
            p[0] = p[1]
        else:
            print("No se puede acceder a un valor que no sea primitivo en un array")
            p[0] = Primitive(ExpressionType.NULL.name,
                            ExpressionType.NULL, position.line, position.column)
    elif len(p) == 4:
        # print(p[1], p[3])
        if isinstance(p[1], Access):
            print("list_access DOT ID")
        else:
            p[0] = AccessObjectAtribute(p[1],p[3], position.line, position.column)
    else:
        p[0] = Access(p[1], position.line, position.column)

#######################################################################
def p_exp_group(p):
    '''exp : LPAREN exp RPAREN'''
    p[0] = p[2]


def p_exp_ternary(p):
    '''exp : exp QUESTION exp COLON exp'''
    position = get_params(p)
    p[0] = Ternary(p[1], p[3], p[5], position.line, position.column)

#######################################################################
# empty


def p_empty(p):
    '''empty :'''
    p[0] = Empty()

#######################################################################
# error
def p_error(p):
    if not p:
        print("The file is empty")
        return
#######################################################################
# error and EOF
def p_escape(p):
    '''escape : SEMICOLON
              | empty '''
#######################################################################
# error
# def p_error(p):
#     if not p:
#         print("The file is empty")
#         return
#     print("Syntax error at line " + str(p.lineno) + " token " + str(p.value))
#     while True:
#         tok = parser.token()             # Get the next token
#         if not tok or tok.type == 'SEMICOLON' :
#             break
#     parser.restart()


# parser = yacc.yacc()
class codeParams:
    def __init__(self, line, column):
        self.line = line
        self.column = column
def get_params(t):
    line = t.lexer.lineno  # Obtener la línea actual desde el lexer
    lexpos = t.lexpos if isinstance(t.lexpos, int) else 0  # Verificar si lexpos es un entero
    column = lexpos - t.lexer.lexdata.rfind('\n', 0, lexpos) 
    return codeParams(line, column)

class Parser:
    def parse(self, data):
        lexer.lineno = 1
        lexer.lexpos = 0
        parser = yacc.yacc()
        result = parser.parse(data)
        return result
