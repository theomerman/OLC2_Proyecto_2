from controllers.interfaces.instruction import Instruction
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
# from controllers.environment.symbol import Symbol
from controllers.environment.types import ExpressionType
from controllers.environment.generator import Generator
from controllers.environment.value import Value

string = ""


class Print(Instruction):
    def __init__(self, exps: list, line, column):
        self.exps = exps
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment, gen: Generator):
        global string
        console = ""
        for exp in self.exps:
            value = exp.run(ast, env, gen)
            if isinstance(value, Value):
                if value.type == ExpressionType.ARRAY:
                    string = ""
                    array_to_string(ast, env, gen, value.value)
                    console += string
                else:
                    if value.type == ExpressionType.NUMBER:
                        gen.add_print(value.value)

                    console += str(value.value) + " "

            else:
                if value.run(ast, env, gen).type == ExpressionType.ARRAY:
                    string = ""
                    array_to_string(ast, env, gen, value.value)
                    string = ""
                else:
                    if value.type == ExpressionType.NUMBER:
                        gen.add_print(value.run(ast,env,gen).value)
                    console += str(value.run(ast, env, gen).value) + " "
        ast.set_console(console)


def array_to_string(ast: Ast, env: Environment,gen: Generator, array: list):
    global string
    string += "["
    for item in array:
        if isinstance(item, list):
            array_to_string(ast, env,gen, item)
        else:
            string += str(item.run(ast, env, gen).value) + ", "
    if string.endswith(", "):
        string = string[:-2]
    string += "]"
