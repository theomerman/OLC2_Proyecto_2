from controllers.interfaces.expression import Expression
from controllers.environment.ast import Ast
from controllers.environment.environment import Environment
from controllers.environment.types import ExpressionType
from controllers.environment.symbol import Symbol
from controllers.expressions.primitive import Primitive
from controllers.environment.error import Error


class Operation(Expression):
    def __init__(self, left, operator, right,  line, column):
        self.left = left
        self.right = right
        self.operator = operator
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment) -> Symbol:
        left = None
        right = self.right.run(ast, env)
        if self.operator not in ['--', '!']:
            left = self.left.run(ast, env)
        if self.operator == '+':
            symbol = sum(left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede sumar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '-':
            symbol = sub(left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede restar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '*':
            symbol = mul(left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede multiplicar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '/':
            symbol = div(left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede dividir {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '%':
            symbol = mod(left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede modular {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '--':
            symbol = unary_minus(right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede negar {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '==':
            symbol = equal(left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede comparar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '!=':
            symbol = different(left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede comparar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '>':
            symbol = greater_than(left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede comparar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '<':
            symbol = less_than(left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede comparar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '>=':
            symbol = greater_than_or_equal(left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede comparar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '<=':
            symbol = less_than_or_equal(left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede comparar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '&&':
            symbol = and_op(left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede operar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '||':
            symbol = or_op(left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede operar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '!':
            symbol = negation(right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede negar {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
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

    return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)


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
    return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)


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
    return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)


def div(left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            if right.value != 0:
                return Symbol(line, column, left.value / right.value, ExpressionType.NUMBER)
            return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
        if right.type == ExpressionType.FLOAT:
            if right.value != 0:
                return Symbol(line, column, left.value / right.value, ExpressionType.FLOAT)
            return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
    if left.type == ExpressionType.FLOAT:
        if right.type == ExpressionType.NUMBER:
            if right.value != 0:
                return Symbol(line, column, left.value / right.value, ExpressionType.FLOAT)
            return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
        if right.type == ExpressionType.FLOAT:
            if right.value != 0:
                return Symbol(line, column, left.value / right.value, ExpressionType.FLOAT)
            return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
    return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)


def mod(left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            if right.value != 0:
                return Symbol(line, column, left.value % right.value, ExpressionType.NUMBER)
            return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
    return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)


def unary_minus(exp: Primitive, line, column):
    if exp.type == ExpressionType.NUMBER:
        return Symbol(line, column, -exp.value, ExpressionType.NUMBER)
    if exp.type == ExpressionType.FLOAT:
        return Symbol(line, column, -exp.value, ExpressionType.FLOAT)
    return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)


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
    return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)


def different(left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            return Symbol(line, column, left.value != right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.FLOAT:
        if right.type == ExpressionType.FLOAT:
            return Symbol(line, column, left.value != right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.BOOLEAN:
        if right.type == ExpressionType.BOOLEAN:
            return Symbol(line, column, left.value != right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.STRING:
        if right.type == ExpressionType.STRING:
            return Symbol(line, column, left.value != right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.CHAR:
        if right.type == ExpressionType.CHAR:
            return Symbol(line, column, left.value != right.value, ExpressionType.BOOLEAN)
    return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)


def greater_than(left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            return Symbol(line, column, left.value > right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.FLOAT:
        if right.type == ExpressionType.FLOAT:
            return Symbol(line, column, left.value > right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.STRING:
        if right.type == ExpressionType.STRING:
            return Symbol(line, column, left.value > right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.CHAR:
        if right.type == ExpressionType.CHAR:
            return Symbol(line, column, left.value > right.value, ExpressionType.BOOLEAN)
    return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)


def less_than(left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            return Symbol(line, column, left.value < right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.FLOAT:
        if right.type == ExpressionType.FLOAT:
            return Symbol(line, column, left.value < right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.STRING:
        if right.type == ExpressionType.STRING:
            return Symbol(line, column, left.value < right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.CHAR:
        if right.type == ExpressionType.CHAR:
            return Symbol(line, column, left.value < right.value, ExpressionType.BOOLEAN)
    return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)


def greater_than_or_equal(left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            return Symbol(line, column, left.value >= right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.FLOAT:
        if right.type == ExpressionType.FLOAT:
            return Symbol(line, column, left.value >= right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.STRING:
        if right.type == ExpressionType.STRING:
            return Symbol(line, column, left.value >= right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.CHAR:
        if right.type == ExpressionType.CHAR:
            return Symbol(line, column, left.value >= right.value, ExpressionType.BOOLEAN)
    return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)


def less_than_or_equal(left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            return Symbol(line, column, left.value <= right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.FLOAT:
        if right.type == ExpressionType.FLOAT:
            return Symbol(line, column, left.value <= right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.STRING:
        if right.type == ExpressionType.STRING:
            return Symbol(line, column, left.value <= right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.CHAR:
        if right.type == ExpressionType.CHAR:
            return Symbol(line, column, left.value <= right.value, ExpressionType.BOOLEAN)
    return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)


def and_op(left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.BOOLEAN and right.type == ExpressionType.BOOLEAN:
        return Symbol(line, column, left.value and right.value, ExpressionType.BOOLEAN)
    return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)


def or_op(left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.BOOLEAN and right.type == ExpressionType.BOOLEAN:
        return Symbol(line, column, left.value or right.value, ExpressionType.BOOLEAN)
    return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)


def negation(exp: Primitive, line, column):
    if exp.type == ExpressionType.BOOLEAN:
        return Symbol(line, column, not exp.value, ExpressionType.BOOLEAN)
    return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
