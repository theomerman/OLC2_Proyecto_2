from icecream import ic
import numpy as np
from controllers.interfaces.expression import Expression
from controllers.expressions.primitive import Primitive
from controllers.expressions.access import Access
from controllers.environment.error import Error
from controllers.environment.types import ExpressionType
from controllers.environment.ast import Ast
from controllers.environment.environment import Environment
from controllers.environment.generator import Generator


class AccessArray(Expression):
    def __init__(self, id: Access, line, column):
        self.id = id
        self.indexes = []
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment, gen: Generator):
        arr = env.get_variable(ast, self.id.id)
        if arr.type == ExpressionType.NULL:
            return arr
        # if len(self.indexes) != np.array(arr.value).ndim:
        #     ast.add_error(Error(
        #         "La cantidad de dimensiones no coincide",
        #         env.id,
        #         "Semantico",
        #         self.line,
        #         self.column
        #     ))
        #
        #     return Primitive(ExpressionType.NULL.name, ExpressionType.NULL, self.line, self.column)
        return get_index(ast, env, gen, arr.value, self.indexes, self.line, self.column)


def get_index(ast: Ast, env: Environment, gen: Generator, array: str, indexes: list, line, column):
    arr = array
    index = indexes[0].run(ast, env, gen).value

    gen.label_queue[0].append(f"\tli t0, {str(index)}\n")
    gen.label_queue[0].append(f"\tlw t0, {gen.get_offset()}(t0)\n")
    gen.label_queue[0].append(f"\tli t1, 4\n")
    gen.label_queue[0].append(f"\tmul t0, t0, t1\n")
    gen.label_queue[0].append(f"\tla t1, {arr}\n")
    gen.label_queue[0].append(f"\tadd t0, t0, t1\n")
    gen.label_queue[0].append(f"\taddi t0, t0, 4\n")
    gen.label_queue[0].append(f"\tlw t0, 0(t0)\n")
    gen.base += 4
    gen.label_queue[0].append(f"\tli t1, {gen.get_base()}\n")
    gen.label_queue[0].append(f"\tsw t0, {gen.get_offset()}(t1)\n")
    return Primitive(f"{gen.get_base()}", ExpressionType.NUMBER, line, column)

