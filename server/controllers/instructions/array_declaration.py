from icecream import ic
from controllers.interfaces.instruction import Instruction
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.types import ExpressionType
from controllers.environment.error import Error
from controllers.instructions.declaration import set_variable
from controllers.expressions.primitive import Primitive
from controllers.environment.generator import Generator
import numpy as np


class ArrayDeclaration(Instruction):
    def __init__(self, constant: bool, id: str, type: ExpressionType, dimensions: int, array: list, line, column):
        self.constant = constant
        self.id = id
        self.type = type
        self.dimensions = dimensions
        self.array = array
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment, gen: Generator):
        # if id in env.table:
        #     ast.add_error(
        #         Error(
        #             f"La variable \"{id}\" ya existe",
        #             env.id,
        #             "Semantico",
        #             self.line,
        #             self.column
        #         )
        #     )
        #     return
        if not isinstance(self.array, list):
            self.array = self.array.run(ast, env)
            if self.array.type != ExpressionType.ARRAY:
                ast.add_error(
                    Error(
                        f"Error de asignacion, se esperaba un tipo {ExpressionType.ARRAY.name} y se encontro un tipo {self.array.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
                return
            self.array = self.array.value
        if self.dimensions != np.array(self.array).ndim:
            ast.add_error(
                Error(
                    f"Error de asignacion, se esperaban {self.dimensions} dimensiones y se encontro {np.array(self.array).ndim}",
                    env.id,
                    "Semantico",
                    self.line,
                    self.column
                )
            )
            return
        # if not is_same_type(ast, env, gen, self.type, self.array, self.line, self.column):
        #     return
        
        if self.dimensions > 1:
            # arr = Primitive(self.array, ExpressionType.ARRAY, self.line, self.column)
            # arr.value_object.array_type = self.type
            # set_variable(ast, env, self.id, arr, ExpressionType.ARRAY, self.line, self.column, self.constant)
            ast.add_error(
                    Error(
                        f"Error de asignacion, no se permite la declaracion de arreglos multidimensionales",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                                )
            return

        else:
            tmp = f"{len(self.array)}"
            for _ in range(15):
                tmp += f",0"
            gen.data.append(f"{self.id}: .word {tmp}\n")

            counter = 0
            for item in self.array:
                counter += 4
                base = item.run(ast, env, gen).value
                gen.label_queue[0].append(f"\tli t0, {base}\n")
                gen.label_queue[0].append(f"\tlw t0, {gen.get_offset()}(t0)\n")
                gen.label_queue[0].append(f"\tla t1, {self.id}\n")
                gen.label_queue[0].append(f"\taddi t1, t1, {counter}\n")
                gen.label_queue[0].append(f"\tsw t0, 0(t1)\n")

            # gen.label_queue[0].append(f"\t")


            arr = Primitive(self.id, ExpressionType.ARRAY, self.line, self.column)
            arr.value_object.array_type = self.type
            set_variable(ast, env, gen, self.id, arr, ExpressionType.ARRAY, self.line, self.column, self.constant)


def is_same_type(ast: Ast, env: Environment, type: ExpressionType, array: list, line, column):
    arr = np.array(array).flatten()
    for itemd in arr:
        item = itemd.run(ast, env)
        if type != item.type:
            ast.add_error(
                Error(
                    f"Error de asignacion, se esperaba un tipo {type.name} y se encontro un tipo {item.type.name}",
                    env.id,
                    "Semantico",
                    line,
                    column
                )
            )
            return False
    return True
