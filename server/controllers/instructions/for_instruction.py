from controllers.interfaces.instruction import Instruction
from controllers.interfaces.expression import Expression
from controllers.environment.ast import Ast
from controllers.environment.environment import Environment
from controllers.environment.symbol import Symbol
from controllers.environment.types import ExpressionType
from controllers.instructions.declaration import Declaration
from controllers.instructions.break_statement import BreakException
from controllers.instructions.continue_statement import ContinueException


class For(Instruction):
    def __init__(self, declaration: Declaration, exp: Expression, modification: list, block: list, line, column):
        self.declaration = declaration
        self.exp = exp
        self.modification = modification
        self.block = block
        self.line = line
        self.column = column

    def run1(self, ast: Ast, env: Environment):
        for_env = Environment(env, "for")
        self.declaration.run(ast, for_env)

        for_env.table[self.modification[0]] = Symbol(
            for_env.table[self.modification[0]].line,
            for_env.table[self.modification[0]].col,
            for_env.table[self.modification[0]].value,
            for_env.table[self.modification[0]].type,
        )
        while self.exp.run(ast, for_env).value:
            try:
                for inst in self.block:
                    try:
                        for_env = Environment(for_env, "for")
                        inst.run(ast, for_env)
                    except ContinueException:
                        break
                for_env.update_variable(ast, self.modification[0], "++", Symbol(
                    self.line, self.column, 1, ExpressionType.NUMBER), self.line, self.column)
            except BreakException:
                break
            # except ContinueException:
            #     continue



    def run(self, ast: Ast, env: Environment):
        for_env = Environment(env, "for")
        self.declaration.run(ast, for_env)
        for_env.table[self.modification[0]] = Symbol(
                for_env.table[self.modification[0]].line,
                for_env.table[self.modification[0]].col,
                for_env.table[self.modification[0]].value,
                for_env.table[self.modification[0]].type,
        )
        while True:
            for_env2 = Environment(for_env, "for")
            # print(self.exp.run(ast, for_env).value)
            if not self.exp.run(ast, for_env).value:
                break
            # print(for_env.table.keys(),list(for_env.table.values())[0].value)
            for instruction in self.block:
                instruction.run(ast, for_env2)
            for_env.table[self.modification[0]].value = for_env.table[self.modification[0]].value + 1

            # for_env.table[self.modification[0]].value = for_env.table[self.modification[0]].value + 1
            # print(for_env.table.keys(),list(for_env.table.values())[0].value)
                # for_env.update_variable(ast,self.modification[0],self.modification[1],Symbol(self.line,self.column, 1, ExpressionType.NUMBER),self.line,self.column)
        ast.symbol_table.append([env.id, for_env.table])











































    def run2(self, ast: Ast, env: Environment):
        for_env = Environment(env, "for")
        self.declaration.run(ast, for_env)

        for_env.table[self.modification[0]] = Symbol(
            for_env.table[self.modification[0]].line,
            for_env.table[self.modification[0]].col,
            for_env.table[self.modification[0]].value,
            for_env.table[self.modification[0]].type,
        )
        while self.exp.run(ast, for_env).value:
            try:
                for inst in self.block:
                    try:
                        for_env = Environment(for_env, "for")
                        inst.run(ast, for_env)
                    except ContinueException:
                        break
                for_env.update_variable(ast, self.modification[0], "++", Symbol(
                    self.line, self.column, 1, ExpressionType.NUMBER), self.line, self.column)
            except BreakException:
                break
            # except ContinueException:
            #     continue
