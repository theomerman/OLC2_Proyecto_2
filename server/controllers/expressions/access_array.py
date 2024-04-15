import numpy as np
from controllers.interfaces.expression import Expression
from controllers.expressions.primitive import Primitive
from controllers.expressions.access import Access
from controllers.environment.error import Error
from controllers.environment.types import ExpressionType
from controllers.environment.ast import Ast
from controllers.environment.environment import Environment


class AccessArray(Expression):
    def __init__(self, id: Access, line, column):
        self.id = id
        self.indexes = []
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        arr = env.get_variable(ast, self.id.id)
        if arr.type == ExpressionType.NULL:
            return arr
        if len(self.indexes) != np.array(arr.value).ndim:
            ast.add_error(Error(
                "La cantidad de dimensiones no coincide",
                env.id,
                "Semantico",
                self.line,
                self.column
            ))

            return Primitive(ExpressionType.NULL.name, ExpressionType.NULL, self.line, self.column)
        return get_index(ast, env, arr.value, self.indexes, self.line, self.column)


def get_index(ast: Ast, env: Environment, array: list, indexes: list, line, column):
    arr = array
    try:
        for index in indexes:
            arr = arr[index.run(ast, env).value]
    except IndexError:
        ast.add_error(Error(
            "El indice no existe en el arreglo",
            env.id,
            "Semantico",
            line,
            column
        ))
        arr = Primitive(ExpressionType.NULL.name,
                        ExpressionType.NULL, line, column)
    return arr
