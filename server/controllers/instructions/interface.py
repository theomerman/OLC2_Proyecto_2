from controllers.interfaces.instruction import Instruction
from controllers.environment.ast import Ast
from controllers.environment.environment import Environment
from controllers.interfaces.expression import Expression
from controllers.environment.error import Error

class Interface(Instruction):
    def __init__(self, id: str, atributes: dict, line, column):
        self.id = id
        self.atributes = atributes
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        tmp = ""
        count = 0
        for atribute in self.atributes:
            tmp = atribute[0]
            count = 0
            for atribute2 in self.atributes:
                if tmp == atribute2[0]:
                    count += 1
            if count > 1:
                ast.add_error(Error(
                    f"El atributo {tmp} se encuentra duplicado en la interfaz {self.id}",
                    env.id,
                    "Semantico",
                    self.line,
                    self.column
                ))
                return
        atributes = {}
        for atribute in self.atributes:
            atributes[atribute[0]] = atribute[1]
        for value in atributes.values():
            if isinstance(value,str):
                if value not in env.interfaces:
                    ast.add_error(Error(
                        f"La interfaz {value} no existe",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    ))
                    return
        env.set_interface(ast, self.id, atributes, self.line, self.column)

        # x = ["3", 4, 5, "3", 7, 8, 5, 10]
        # times = x.count("3")
        # print(times)
        # for atribute in self.atributes:
        #     print(atribute)
