import numpy as np
from controllers.interfaces.instruction import Instruction
from controllers.environment.error import Error
from controllers.expressions.access_array import get_index
from controllers.environment.types import ExpressionType
from controllers.expressions.primitive import Primitive
from controllers.environment.ast import Ast
from controllers.environment.environment import Environment


class ArrayAssignment(Instruction):
    def __init__(self, id: str, indexes: list, exp, line, column):
        self.id = id
        self.indexes = indexes
        self.exp = exp
        self.line = line
        self.column = column

    def run(self, ast:Ast, env: Environment):
        arr = env.get_variable(ast, self.id)
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
        tmp = get_index(ast, env, arr.value, self.indexes,
                        self.line, self.column)
        if isinstance(tmp, Primitive):
            if tmp.type == ExpressionType.NULL:
                return tmp
        insert(ast, env, arr.value, self.indexes,
               self.exp, self.line, self.column)


# insert value in array
def insert(ast: Ast, env: Environment, array: list, indexes: list, new_value: Primitive, line, column):
    arr = array
    try:
        for index in indexes[:-1]:
            arr = arr[index.run(ast, env).value]
        arr.pop(indexes[-1].run(ast, env).value)
        arr.insert(indexes[-1].run(ast, env).value, new_value)

    except IndexError:
        ast.add_error(Error(
            "El indice no existe en el arreglo",
            env.id,
            "Semantico",
            line,
            column
        ))
    return arr
