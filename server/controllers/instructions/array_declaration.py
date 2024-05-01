from controllers.interfaces.instruction import Instruction
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.types import ExpressionType
from controllers.environment.error import Error
from controllers.instructions.declaration import set_variable
from controllers.expressions.primitive import Primitive
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

    def run(self, ast: Ast, env: Environment):
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
        if not is_same_type(ast, env, self.type, self.array,
                            self.line, self.column):
            return
        if self.dimensions > 1:
            arr = Primitive(self.array, ExpressionType.ARRAY,
                            self.line, self.column)
            arr.symbol.array_type = self.type
            set_variable(ast, env, self.id, arr,
                         ExpressionType.ARRAY, self.line, self.column, self.constant)
        else:
            # if isinstance(self.array, list):
            arr = Primitive(self.array, ExpressionType.ARRAY,
                            self.line, self.column)
            arr.symbol.array_type = self.type
            set_variable(ast, env, self.id, arr,
                         ExpressionType.ARRAY, self.line, self.column, self.constant)


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
