from controllers.interfaces.instruction import Instruction
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.instructions.break_statement import BreakException
from controllers.instructions.continue_statement import ContinueException


class While(Instruction):
    def __init__(self, condition, instructions, line, column):
        self.condition = condition
        self.instructions = instructions
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        while self.condition.run(ast, env).value:
            while_env = Environment(env, "while")
            try:
                for instruction in self.instructions:
                    instruction.run(ast, while_env)
            except BreakException:
                break
            except ContinueException:
                continue
