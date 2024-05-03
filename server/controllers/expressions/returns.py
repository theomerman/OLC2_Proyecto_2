
from controllers.interfaces.expression import Expression
from controllers.environment.ast import Ast
from controllers.environment.environment import Environment
from controllers.environment.error import Error

class Return(Expression):
    def __init__(self, expression : Expression, line, column):
        self.expression = expression
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        flag = False
        while env.previus != None:
            if env.id.find("function") != -1:
                flag = True
                break
            env = env.previus
        if not flag:
            ast.add_error(Error(
                "No se puede usar return fuera de una funcion",
                env.id,
                "Semantico",
                self.line,
                self.column
            ))
            return
        raise ReturnValue(self.expression, self.line, self.column)
        # return ReturnValue(self.expression, self.line, self.column)

        
#     def __init__(self, expression, line, column):
#         self.expression = expression
#         self.line = line
#         self.column = column
#         print(self.expression.value)

class ReturnValue(Exception):
    def __init__(self, expression, line, column):
        super().__init__("Return Value")
        self.expression = expression
        self.line = line
        self.column = column
        # print(self.expression.value)


