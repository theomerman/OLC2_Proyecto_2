from controllers.interfaces.instruction import Instruction
from controllers.interfaces.expression import Expression
from controllers.environment.environment import Environment
from controllers.instructions.break_statement import BreakException
from controllers.environment.ast import Ast
from controllers.environment.error import Error


class Switch(Instruction):
    def __init__(self, exp: Expression, cases: list, line, column):
        self.exp = exp
        self.cases = cases
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        exp = self.exp.run(ast, env).value
        default_case = []
        for case in self.cases:
            if case[0] is None:
                default_case.append(case[1])
        if len(default_case) > 1:
            ast.add_error(Error(
                "No puede haber mas de un caso default",
                env.id,
                "Semantico",
                self.line,
                self.column
            ))
            return
        for case in self.cases:
            if case[0] is None:
                if len(self.cases) == 1:
                    self.cases.clear()
                else:
                    self.cases = self.cases[1:]
            elif case[0].run(ast, env).value != exp:
                if len(self.cases) == 1:
                    self.cases.clear()
                else:
                    self.cases = self.cases[1:]
            elif case[0].run(ast, env).value == exp:
                break
        # print(len(self.cases))
        if len(self.cases) == 0:
            if len(default_case) == 0:
                return
            for inst in default_case[0]:
                try:
                    switch_env = Environment(env, "switch")
                    inst.run(ast, switch_env)
                except BreakException:
                    break
        else:
            for case in self.cases:
                try:
                    for inst in case[1]:
                        switch_env = Environment(env, "switch")
                        inst.run(ast, switch_env)
                except BreakException:
                    break
