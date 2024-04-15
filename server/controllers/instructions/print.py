from controllers.interfaces.instruction import Instruction
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.symbol import Symbol
from controllers.environment.types import ExpressionType

string = ""


class Print(Instruction):
    def __init__(self, exps: list, line, column):
        self.exps = exps
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        global string
        console = ""
        for exp in self.exps:
            value = exp.run(ast, env)
            if isinstance(value, Symbol):
                if value.type == ExpressionType.ARRAY:
                    string = ""
                    array_to_string(ast, env, value.value)
                    console += string
                else:
                    console += str(value.value) + " "

            else:
                if value.run(ast, env).type == ExpressionType.ARRAY:
                    string = ""
                    array_to_string(ast, env, value.value)
                    string = ""
                else:
                    console += str(value.run(ast, env).value) + " "
        ast.set_console(console)


def array_to_string(ast: Ast, env: Environment, array: list):
    global string
    string += "["
    for item in array:
        if isinstance(item, list):
            array_to_string(ast, env, item)
        else:
            string += str(item.run(ast, env).value) + ", "
    if string.endswith(", "):
        string = string[:-2]
    string += "]"
