from controllers.interfaces.instruction import Instruction
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.interfaces.expression import Expression
from controllers.expressions.access_object_atribute import AccessObjectAtribute
from controllers.environment.symbol import Symbol
from controllers.environment.types import ExpressionType
from controllers.environment.error import Error

class ModifyObjectAttribute(Instruction):
    def __init__(self, id: list , value : Expression, line, column):
        self.id = id
        self.value = value
        self.line = line
        self.column = column

    def run(self, ast:Ast, env: Environment):
        # object = env.get_variable(ast, self.id[0])
        obj = AccessObjectAtribute(self.id[0],self.id[1],self.line, self.column).run(ast,env)
        for i in range(len(self.id) - 1):
            if isinstance(obj, Symbol):
                break
            obj = AccessObjectAtribute(obj,self.id[i+1],self.line, self.column).run(ast,env)

        if obj.type != self.value.run(ast, env).type:
            ast.add_error(Error(
            "El tipo de dato no coincide con el tipo de la variable",
            env.id,
            "Semantico",
            self.line,
            self.column
            )
            )
            return
        if obj.interface != self.value.run(ast, env).interface:
            ast.add_error(Error(
            "El tipo de dato no coincide con el tipo de la variable",
            env.id,
            "Semantico",
            self.line,
            self.column
            )
            )
            return
        obj.value = self.value.run(ast, env).value
