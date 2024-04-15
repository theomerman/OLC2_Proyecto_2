from controllers.interfaces.expression import Expression
from controllers.environment.error import Error
from controllers.environment.ast import Ast
from controllers.environment.environment import Environment
from controllers.environment.symbol import Symbol
from controllers.environment.types import ExpressionType
class AccessObjectAtribute(Expression):
    def __init__(self, id: str, id_object: str, line: int, column: int):
        self.id = id
        self.id_object = id_object
        self.line = line
        self.column = column
    def run(self, ast: Ast, env: Environment):
        if not isinstance(self.id, str):
            tmp = self.id.run(ast, env).value
            if self.id_object not in tmp:
                ast.add_error(Error(
                "El objeto " + self.id.run(ast,env).value + " no tiene el atributo " + self.id_object,
                env.id,
                "Semantico",
                self.line,
                self.column
                )
                )
                return Symbol(self.line, self.column, ExpressionType.NULL.name, ExpressionType.NULL)
            return tmp[self.id_object]
        #     self.id = self.id.run(ast, env)
            
        # print(self.id)
        if self.id not in env.table:
            ast.add_error(Error(
                "No se encontro la variable " + self.id,
                env.id,
                "Semantico",
                self.line,
                self.column
            )
            )
            return Symbol(self.line, self.column, ExpressionType.NULL.name, ExpressionType.NULL)
        if env.table[self.id].type != ExpressionType.INTERFACE:
            ast.add_error(Error(
            "La variable " + self.id + " no es un objeto",
            env.id,
            "Semantico",
            self.line,
            self.column
            )
            )
            return Symbol(self.line, self.column, ExpressionType.NULL.name, ExpressionType.NULL)
        atributes = env.table[self.id].value
        if self.id_object not in atributes:
            ast.add_error(Error(
            "El objeto " + self.id + " no tiene el atributo " + self.id_object,
            env.id,
            "Semantico",
            self.line,
            self.column
            )
            )
            return Symbol(self.line, self.column, ExpressionType.NULL.name, ExpressionType.NULL)
        else:
            return atributes[self.id_object]

