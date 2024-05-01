from controllers.interfaces.expression import Expression
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.error import Error
from controllers.expressions.primitive import Primitive
from controllers.environment.types import ExpressionType
from controllers.environment.symbol import Symbol


class EmbedFunctions(Expression):
    def __init__(self, function_name: str, expression: Expression, line, column):
        self.function_name = function_name
        self.expression = expression
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        if isinstance(self.expression, str):
            self.expression = env.get_variable(ast, self.expression)
            self.expression = Primitive(
                self.expression.value, self.expression.type, self.line, self.column)
        if self.expression.run(ast, env).type == ExpressionType.NULL:
            ast.add_error(
                Error(
                    "No se puede ejecutar una función sobre un valor nulo",
                    env.id,
                    "Semántico",
                    self.line,
                    self.column
                )
            )
            return Primitive(ExpressionType.NULL.name, ExpressionType.NULL, self.line, self.column)
        exp = self.expression.run(ast, env)
        if self.function_name == "parseInt":
            return parseInt(ast, env, exp, self.line, self.column)
        elif self.function_name == "typeof":
            return Primitive(exp.type.name.lower(), ExpressionType.STRING, self.line, self.column)
        elif self.function_name == "parseFloat":
            return parseFloat(ast, env, exp, self.line, self.column)
        elif self.function_name == "toString":
            return toString(ast, env, exp, self.line, self.column)
        elif self.function_name == "toLowerCase":
            return toLowerCase(ast, env, exp, self.line, self.column)
        elif self.function_name == "toUpperCase":
            return toUpperCase(ast, env, exp, self.line, self.column)
        elif self.function_name == "values":
            return values(ast, env, exp, self.line, self.column)
        elif self.function_name == "keys":
            return keys(ast, env, exp, self.line, self.column)


def parseInt(ast: Ast, env: Environment, exp: Symbol, line, column):
    if exp.type == ExpressionType.STRING:
        try:
            value = float(exp.value)
            value = int(value)
            return Primitive(value, ExpressionType.NUMBER, line, column)
        except ValueError:
            ast.add_error(
                Error(
                    "La cadena no es un número válido",
                    env.id,
                    "Semántico",
                    line,
                    column
                )

            )
            return Primitive(ExpressionType.NULL.name, ExpressionType.NULL, line, column)
    ast.add_error(
        Error(
            f"No se puede convertir {exp.type.name} a número",
            env.id,
            "Semántico",
            line,
            column
        )
    )
    return Primitive(ExpressionType.NULL.name, ExpressionType.NULL, line, column)


def parseFloat(ast: Ast, env: Environment, exp: Symbol, line, column):
    if exp.type == ExpressionType.STRING:
        try:
            value = float(exp.value)
            return Primitive(value, ExpressionType.FLOAT, line, column)
        except ValueError:
            ast.add_error(
                Error(
                    f"La cadena no es un número válido",
                    env.id,
                    "Semántico",
                    line,
                    column
                )
            )
            return Primitive(ExpressionType.NULL.name, ExpressionType.NULL, line, column)
    ast.add_error(
        Error(
            f"No se puede convertir {exp.type.name} a número",
            env.id,
            "Semántico",
            line,
            column
        )
    )
    return Primitive(ExpressionType.NULL.name, ExpressionType.NULL, line, column)


def toString(ast: Ast, env: Environment, exp: Symbol, line, column):
    if exp.type == ExpressionType.NUMBER or exp.type == ExpressionType.BOOLEAN or exp.type == ExpressionType.STRING or exp.type == ExpressionType.FLOAT:
        return Primitive(str(exp.value), ExpressionType.STRING, line, column)
    ast.add_error(
        Error(
            f"No se puede convertir {exp.type.name} a cadena",
            env.id,
            "Semántico",
            line,
            column
        )
    )
    return Primitive(ExpressionType.NULL.name, ExpressionType.NULL, line, column)


def toLowerCase(ast: Ast, env: Environment, exp: Symbol, line, column):
    if exp.type == ExpressionType.STRING:
        return Primitive(exp.value.lower(), ExpressionType.STRING, line, column)
    ast.add_error(
        Error(
            f"No se puede convertir {exp.type.name} a cadena",
            env.id,
            "Semántico",
            line,
            column
        )
    )
    return Primitive(ExpressionType.NULL.name, ExpressionType.NULL, line, column)


def toUpperCase(ast: Ast, env: Environment, exp: Symbol, line, column):
    if exp.type == ExpressionType.STRING:
        return Primitive(exp.value.upper(), ExpressionType.STRING, line, column)
    ast.add_error(
        Error(
            f"No se puede convertir {exp.type.name} a cadena",
            env.id,
            "Semántico",
            line,
            column
        )
    )
    return Primitive(ExpressionType.NULL.name, ExpressionType.NULL, line, column)


def keys(ast: Ast, env: Environment, exp: Symbol, line, column):
    symbol = Symbol(line, column,[],ExpressionType.ARRAY)
    if exp.type == ExpressionType.INTERFACE:
        for key in exp.value:
            symbol.value.append(Primitive(key, ExpressionType.STRING, line, column))
        return symbol
    ast.add_error(
        Error(
            f"No se puede obtener las llaves de un {exp.type.name}",
            env.id,
            "Semántico",
            line,
            column
        )
    )
    return Primitive(ExpressionType.NULL.name, ExpressionType.NULL, line, column)


def values(ast: Ast, env: Environment, exp: Symbol, line, column):
    symbol = Symbol(line, column,[],ExpressionType.ARRAY)
    if exp.type == ExpressionType.INTERFACE:
        for value in exp.value.values():
            symbol.value.append(Primitive(str(value.value),ExpressionType.STRING, line, column))
        return symbol
        # for key in exp.value:
        #     symbol.value.append(Primitive(key, ExpressionType.STRING, line, column))
        # return symbol
    # print(list(exp.value.values()))
    # print(list(exp.value.values())[0].value)
    # symbol = Symbol(line, column,[],ExpressionType.ARRAY)
    # if exp.type == ExpressionType.INTERFACE:
    #     return symbol
    #     # for key in exp.value:
    #     #     symbol.value.append(exp.value[key])
    #     # return symbol
    ast.add_error(
        Error(
            f"No se puede obtener los valores de un {exp.type.name}",
            env.id,
            "Semántico",
            line,
            column
        )
    )
    return Primitive(ExpressionType.NULL.name, ExpressionType.NULL, line, column)
