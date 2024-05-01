from controllers.interfaces.instruction import Instruction
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.error import Error


class Continue(Instruction):
    def __init__(self, line, column):
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        while env.id not in ("while", "for", "global"):
            env = env.previus
        if env.id == "global":
            ast.add_error(Error(
                "No se puede usar continue fuera de un ciclo",
                env.id,
                "Semantico",
                self.line,
                self.column
            ))
            return
        raise ContinueException()


class ContinueException(Exception):
    pass
