from controllers.interfaces.expression import Expression
from controllers.environment.ast import Ast
from controllers.environment.environment import Environment
from controllers.environment.error import Error
from controllers.environment.types import ExpressionType
from controllers.environment.symbol import Symbol


class Ternary(Expression):
    def __init__(self, left, if_true, if_false, line, column) -> None:
        self.left = left
        self.if_true = if_true
        self.if_false = if_false
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment) -> Symbol:
        left = self.left.run(ast, env)
        if left.type != ExpressionType.BOOLEAN:
            ast.add_error(
                Error(
                    "The condition of the ternary operator must be a boolean",
                    env,
                    "Semantico",
                    self.line,
                    self.column,
                )
            )
            print("entro error")
            return Symbol(self.line, self.column, ExpressionType.NULL.name, ExpressionType.NULL)
        if left.value:
            return self.if_true.run(ast, env)
        else:
            return self.if_false.run(ast, env)
