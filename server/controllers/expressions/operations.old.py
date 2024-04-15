
from controllers.interfaces.expression import Expression
from controllers.enviroment.ast import Ast
from controllers.enviroment.environment import Environment
from controllers.enviroment.types import ExpressionType
from controllers.enviroment.symbol import Symbol
from controllers.expressions.primitive import Primitive


class Operation(Expression):
    def __init__(self, left, operator, right,  line, column):
        self.left = left
        self.right = right
        self.operator = operator
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        left = None
        right = self.right.run(ast, env)
        if self.operator != '--':
            left = self.left.run(ast, env)
        if self.operator == '!':
            left = self.left.run(ast, env)
        if self.operator == '+':
            symbol = sum(left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    f"No se puede sumar {left.type.name} con {right.type.name}", self.line, self.column)
            return symbol
        if self.operator == '-':
            symbol = sub(left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    f"No se puede restar {left.type.name} con {right.type.name}", self.line, self.column)
            return symbol
        if self.operator == '*':
            symbol = mul(left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    f"No se puede multiplicar {left.type.name} con {right.type.name}", self.line, self.column)
            return symbol
        if self.operator == '/':
            symbol = div(left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    f"No se puede dividir {left.type.name} con {right.type.name}", self.line, self.column)
            return symbol
        if self.operator == '%':
            symbol = mod(left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    f"No se puede modular {left.type.name} con {right.type.name}", self.line, self.column)
            return symbol
        if self.operator == '--':
            symbol = unary_minus(right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    f"No se puede negar {right.type.name}", self.line, self.column)
            return symbol
        if self.operator == '!':
            symbol = Symbol(self.line, self.column,
                            not left.value, ExpressionType.BOOLEAN)
            return symbol


def sum(left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            return Symbol(line, column, left.value + right.value, ExpressionType.NUMBER)
        if right.type == ExpressionType.FLOAT:
            return Symbol(line, column, left.value + right.value, ExpressionType.FLOAT)
    if left.type == ExpressionType.FLOAT:
        if right.type == ExpressionType.NUMBER:
            return Symbol(line, column, left.value + right.value, ExpressionType.FLOAT)
        if right.type == ExpressionType.FLOAT:
            return Symbol(line, column, left.value + right.value, ExpressionType.FLOAT)
    if left.type == ExpressionType.STRING:
        if right.type == ExpressionType.STRING:
            return Symbol(line, column, left.value + right.value, ExpressionType.STRING)

    return Symbol(line, column, None, ExpressionType.NULL)


def sub(left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            return Symbol(line, column, left.value - right.value, ExpressionType.NUMBER)
        if right.type == ExpressionType.FLOAT:
            return Symbol(line, column, left.value - right.value, ExpressionType.FLOAT)
    if left.type == ExpressionType.FLOAT:
        if right.type == ExpressionType.NUMBER:
            return Symbol(line, column, left.value - right.value, ExpressionType.FLOAT)
        if right.type == ExpressionType.FLOAT:
            return Symbol(line, column, left.value - right.value, ExpressionType.FLOAT)
    return Symbol(line, column, None, ExpressionType.NULL)


def mul(left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            return Symbol(line, column, left.value * right.value, ExpressionType.NUMBER)
        if right.type == ExpressionType.FLOAT:
            return Symbol(line, column, left.value * right.value, ExpressionType.FLOAT)
    if left.type == ExpressionType.FLOAT:
        if right.type == ExpressionType.NUMBER:
            return Symbol(line, column, left.value * right.value, ExpressionType.FLOAT)
        if right.type == ExpressionType.FLOAT:
            return Symbol(line, column, left.value * right.value, ExpressionType.FLOAT)
    return Symbol(line, column, None, ExpressionType.NULL)


def div(left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            if right.value != 0:
                return Symbol(line, column, left.value / right.value, ExpressionType.NUMBER)
            return Symbol(line, column, None, ExpressionType.NULL)
        if right.type == ExpressionType.FLOAT:
            if right.value != 0:
                return Symbol(line, column, left.value / right.value, ExpressionType.FLOAT)
            return Symbol(line, column, None, ExpressionType.NULL)
    if left.type == ExpressionType.FLOAT:
        if right.type == ExpressionType.NUMBER:
            if right.value != 0:
                return Symbol(line, column, left.value / right.value, ExpressionType.FLOAT)
            return Symbol(line, column, None, ExpressionType.NULL)
        if right.type == ExpressionType.FLOAT:
            if right.value != 0:
                return Symbol(line, column, left.value / right.value, ExpressionType.FLOAT)
            return Symbol(line, column, None, ExpressionType.NULL)
    return Symbol(line, column, None, ExpressionType.NULL)


def mod(left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            if right.value != 0:
                return Symbol(line, column, left.value % right.value, ExpressionType.NUMBER)
            return Symbol(line, column, None, ExpressionType.NULL)
    return Symbol(line, column, None, ExpressionType.NULL)


def unary_minus(exp: Primitive, line, column):
    if exp.type == ExpressionType.NUMBER:
        return Symbol(line, column, -exp.value, ExpressionType.NUMBER)
    if exp.type == ExpressionType.FLOAT:
        return Symbol(line, column, -exp.value, ExpressionType.FLOAT)
    return Symbol(line, column, None, ExpressionType.NULL)


def equal(left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            return Symbol(line, column, left.value == right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.FLOAT:
        if right.type == ExpressionType.FLOAT:
            return Symbol(line, column, left.value == right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.BOOLEAN:
        if right.type == ExpressionType.BOOLEAN:
            return Symbol(line, column, left.value == right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.STRING:
        if right.type == ExpressionType.STRING:
            return Symbol(line, column, left.value == right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.CHAR:
        if right.type == ExpressionType.CHAR:
            return Symbol(line, column, left.value == right.value, ExpressionType.BOOLEAN)
