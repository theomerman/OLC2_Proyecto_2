from controllers.interfaces.expression import Expression
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.error import Error
from controllers.environment.symbol import Symbol
from controllers.environment.types import ExpressionType
from controllers.expressions.primitive import Primitive
from controllers.expressions.returns import ReturnValue
class CallFunction(Expression):
    def __init__(self, id: str, parameters: list,line,column):
        self.id = id
        self.parameters = parameters
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        env_global = env
        while env_global.id != "global":
            env_global = env_global.previus

        function_env = Environment(env, "function " + self.id)

        if self.id not in env_global.functions:
            ast.add_error(Error(
                f"La funcion {self.id} no existe",
                env.id,
                "Semantico",
                self.line,
                self.column
            ))
            return Primitive(ExpressionType.NULL.name,ExpressionType.NULL, self.line, self.column)
        if len(self.parameters) != len(env_global.functions[self.id]["parameters"]):
            ast.add_error(Error(
                f"Se esperaban {len(env_global.functions[self.id]['parameters'])} parametros en la funcion {self.id} pero se recibieron {len(self.parameters)}",
                env.id,
                "Semantico",
                self.line,
                self.column
            ))
            return Primitive(ExpressionType.NULL.name,ExpressionType.NULL, self.line, self.column)
        for i in range(len(self.parameters)):
            if env_global.functions[self.id]["parameters"][i][1] != self.parameters[i].run(ast,env).type:
                ast.add_error(Error(
                    f"El tipo de parametro {i+1} en la funcion {self.id} no coincide",
                    env.id,
                    "Semantico",
                    self.line,
                    self.column
                ))
                return Primitive(ExpressionType.NULL.name,ExpressionType.NULL, self.line, self.column)
            if self.parameters[i].run(ast,env).type == ExpressionType.ARRAY:
                if env_global.functions[self.id]["parameters"][i][2] != self.parameters[i].run(ast,env).array_type:
                    ast.add_error(Error(
                        f"Se esperaba un array de tipo {env_global.functions[self.id]['parameters'][i][2].name} pero se recibio un array de tipo {self.parameters[i].run(ast,env).array_type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    ))
                    return Primitive(ExpressionType.NULL.name,ExpressionType.NULL, self.line, self.column)
        for i in range(len(self.parameters)):
            function_env.table[env_global.functions[self.id]["parameters"][i][0]] = self.parameters[i].run(ast,env)
        try:
            for instruction in env_global.functions[self.id]["block"]:
                instruction.run(ast,function_env)
        except ReturnValue as e:
            # print(e.expression.run(ast,function_env).value)
            return e.expression.run(ast,function_env)
        # for instruction in env_global.functions[self.id]["block"]:
        #     result = instruction.run(ast,function_env)
        #     if isinstance(result,ReturnValue):
        #         return result.expression.run(ast,function_env)
        ast.symbol_table.append([function_env.id,function_env.table])
