from controllers.interfaces.instruction import Instruction
from controllers.environment.ast import Ast
from controllers.environment.environment import Environment
from controllers.environment.error import Error
from controllers.interfaces.expression import Expression
from controllers.expressions.operation import Operation
from controllers.expressions.returns import Return

class Function(Instruction):
    def __init__(self, id: str, parameters:list, return_types, block:list, line, column):
        self.id = id
        self.parameters = parameters
        self.return_types = return_types
        self.block = block
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        if env.id != "global":
            ast.add_error(Error(
            f"Solo se permite crear funciones en el ambito global",
            self.id,
            "Semantico",
            self.line,
            self.column
            )
            )
            return
        if self.id in env.functions:
            ast.add_error(Error(
            f"La funcion \"{self.id}\" ya existe",
            self.id,
            "Semantico",
            self.line,
            self.column
            )
            )
            return
        # if self.return_types is not None:
        #     flag = False
        #     for instruction in self.block:
        #         if isinstance(instruction, Return):
        #             flag = True
        #             break
        #     if not flag:
        #         ast.add_error(Error(
        #         f"La funcion \"{self.id}\" no tiene un retorno",
        #         self.id,
        #         "Semantico",
        #         self.line,
        #         self.column
        #         )
        #         )
        #         return
        if self.parameters is None:
            self.parameters = []
        for parameter in self.parameters:
            tmp = 0
            for i in self.parameters:
                if parameter[0] == i[0]:
                    tmp += 1
                if tmp > 1:
                    ast.add_error(Error(
                    f"El parametro \"{parameter[0]}\" se repite mas de una vez",
                    self.id,
                    "Semantico",
                    self.line,
                    self.column
                    )
                    )
                    return
        func = {
            "parameters": self.parameters,
            "return_type": self.return_types,
            "block": self.block,
        }
        env.functions[self.id] = func
