import numpy as np
from controllers.interfaces.expression import Expression
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.types import ExpressionType
from controllers.environment.error import Error
from controllers.expressions.primitive import Primitive


class VectorFunctions(Expression):
    def __init__(self, id: str, function: str, value: Expression, line, column):
        self.id = id
        self.function = function
        self.value = value
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        arr = env.get_variable(ast, self.id)
        if arr.type == ExpressionType.NULL:
            ast.add_error(
                f"La variable {self.id} no existe", self.line, self.column)
            return arr
        if arr.type != ExpressionType.ARRAY:
            ast.add_error(
                f"La variable {self.id} no es un vector", self.line, self.column)
            return Primitive(ExpressionType.NULL.name, ExpressionType.NULL, self.line, self.column)
        if np.array(arr.value).ndim != 1:
            ast.add_error(
                Error(
                    "La variable es una Matriz",
                    env.id,
                    "Semantico",
                    self.line,
                    self.column
                )
            )
            return Primitive(ExpressionType.NULL.name, ExpressionType.NULL, self.line, self.column)
        if self.function == "pop":
            deleted_value = arr.value[-1]
            arr.value.pop()
            return deleted_value
        elif self.function == "indexOf":
            index = 0
            for item in arr.value:
                if item.run(ast, env).value == self.value.run(ast, env).value:
                    return Primitive(index, ExpressionType.NUMBER, self.line, self.column)
                index += 1
            return Primitive(-1, ExpressionType.NUMBER, self.line, self.column)
        elif self.function == "join":
            result = ""
            for item in arr.value:
                if result == "":
                    result += str(item.run(ast, env).value)
                else:
                    result += "," + str(item.run(ast, env).value)
            return Primitive(result, ExpressionType.STRING, self.line, self.column)
        elif self.function == "length":
            length = len(arr.value)
            return Primitive(length, ExpressionType.NUMBER, self.line, self.column)
