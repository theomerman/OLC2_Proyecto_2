from controllers.interfaces.instruction import Instruction
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.error import Error
from controllers.environment.generator import Generator


class Break(Instruction):
    def __init__(self, line, column):
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment, gen: Generator):
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
        gen.label_queue[0].append(f"\tj exit{gen.break_stack[0]}\n")
        # raise BreakException()


class BreakException(Exception):
    pass
