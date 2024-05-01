from controllers.interfaces.instruction import Instruction
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.error import Error


class Break(Instruction):
    def __init__(self, line, column):
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        while env.id not in ("while", "for", "switch", "global"):
            env = env.previus
        if env.id == "global":
            ast.add_error(Error(
                "No se puede usar break fuera de un ciclo o switch",
                env.id,
                "Semantico",
                self.line,
                self.column
            ))
            return
        raise BreakException()


class BreakException(Exception):
    pass
