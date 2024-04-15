from controllers.interfaces.instruction import Instruction
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.error import Error
from controllers.environment.types import ExpressionType


class If(Instruction):
    def __init__(self, ctx: list, line, column):
        self.ctx = ctx
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        if_env = Environment(env, "if")

        for arr in self.ctx:
            if arr[0].run(ast, if_env).type != ExpressionType.BOOLEAN:
                ast.add_error(Error(
                    "La condición del if debe ser de tipo booleano",
                    env.id,
                    "Semántico",
                    self.line,
                    self.column
                ))
                return
            if arr[0].run(ast, if_env).value == True:
                for inst in arr[1]:
                    inst.run(ast, if_env)
                break
        ast.symbol_table.append([if_env.id,if_env.table])
