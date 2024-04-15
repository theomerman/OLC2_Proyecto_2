import numpy as np
from controllers.interfaces.instruction import Instruction
from controllers.interfaces.expression import Expression
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.error import Error
from controllers.environment.types import ExpressionType
from controllers.expressions.primitive import Primitive

class Push(Instruction):
    def __init__(self, id: str, value: Expression, line, column):
        self.id = id
        self.value = value
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        arr = env.get_variable(ast, self.id)
        if arr.type == ExpressionType.NULL:
            ast.add_error(
                f"La variable {self.id} no existe", self.line, self.column)
            return
        if arr.type != ExpressionType.ARRAY:
            ast.add_error(
                f"La variable {self.id} no es un vector", self.line, self.column)
            return
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
            return
        if arr.array_type != self.value.run(ast, env).type:
            ast.add_error(
                Error(
                    f"No se puede asignar un tipo {self.value.run(ast, env)} a un vector de tipo {arr.array_type}",
                    env.id,
                    "Semantico",
                    self.line,
                    self.column
                )
            )



        # for item in arr.value:
        #     print(item.run(ast, env).value)

        # print("---------------------")
        new_value = Primitive(self.value.run(ast, env).value,self.value.run(ast,env).type,self.line, self.column)
        arr.value.append(new_value)



        # for item in arr.value:
        #     print(item.run(ast, env).value)

        # arr.value.insert(arr.value[-1], self.value)
