from controllers.interfaces.instruction import Instruction
from controllers.environment.ast import Ast
from controllers.environment.environment import Environment
from controllers.environment.error import Error
from controllers.environment.types import ExpressionType
from controllers.environment.symbol import Symbol

class InterfaceAssignment(Instruction):
    def __init__(self,constant:bool,  id: str, id_object:str, atributes:list, line, column):
        self.constant = constant
        self.id = id
        self.id_object = id_object
        self.atributes = atributes
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment):
        tmp = ""
        count = 0
        for atribute in self.atributes:
            tmp = atribute[0]
            count = 0
            for atribute2 in self.atributes:
                if tmp == atribute2[0]:
                    count += 1
            if count > 1:
                ast.add_error(Error(
                    f"El atributo {tmp} se encuentra duplicado en la interfaz {self.id}",
                    env.id,
                    "Semantico",
                    self.line,
                    self.column
                ))
                return
        if self.id in env.table:
            ast.add_error(Error(
                f"La variable \"{self.id}\" ya existe",
                env.id,
                "Semantico",
                self.line,
                self.column
            ))
        for atribute in self.atributes:
            if atribute[0] not in env.interfaces[self.id_object]:
                ast.add_error(Error(
                    f"El atributo \"{atribute[0]}\" no pertenece a la interfaz \"{self.id}\"",
                    env.id,
                    "Semantico",
                    self.line,
                    self.column
                ))
                return
        if len(self.atributes) != len(env.interfaces[self.id_object]):
            ast.add_error(Error(
                f"La interfaz \"{self.id}\" no tiene la misma cantidad de atributos que el objeto \"{self.id_object}\"",
                env.id,
                "Semantico",
                self.line,
                self.column
            ))
            return
        for atribute in self.atributes:
            if atribute[1].run(ast, env).type != env.interfaces[self.id_object][atribute[0]]:
                # print(env.interfaces[self.id_object][atribute[0]])
                # print(atribute[1].run(ast, env).type)
                # print(env.interfaces[self.id_object][atribute[0]])
                if atribute[1].run(ast, env).type == ExpressionType.INTERFACE:
                    if atribute[1].run(ast, env).interface == env.interfaces[self.id_object][atribute[0]]:
                        continue
                    else:
                        try:
                            ast.add_error(Error(
                                f"El atributo \"{atribute[0]}\" de la interfaz \"{self.id}\" tiene que ser de tipo \"{env.interfaces[self.id_object][atribute[0]].name}\" pero se encontro \"{atribute[1].run(ast, env).interface}\"",
                                env.id,
                                "Semantico",
                                self.line,
                                self.column
                            ))
                            return
                        except AttributeError:
                            ast.add_error(Error(
                                f"El atributo \"{atribute[0]}\" de la interfaz \"{self.id}\" tiene que ser de tipo \"{env.interfaces[self.id_object][atribute[0]]}\" pero se encontro \"{atribute[1].run(ast, env).interface}\"",
                                env.id,
                                "Semantico",
                                self.line,
                                self.column
                            ))
                            return
                try:
                    ast.add_error(Error(
                        f"El atributo \"{atribute[0]}\" de la interfaz \"{self.id}\" tiene que ser de tipo \"{env.interfaces[self.id_object][atribute[0]].name}\" pero se encontro \"{atribute[1].run(ast, env).type.name}\"",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    ))
                    return
                except AttributeError:
                    ast.add_error(Error(
                        f"El atributo \"{atribute[0]}\" de la interfaz \"{self.id}\" tiene que ser de tipo \"{env.interfaces[self.id_object][atribute[0]]}\" pero se encontro \"{atribute[1].run(ast, env).type.name}\"",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    ))
                    return

        atributes = {}
        for atribute in self.atributes:
            atributes[atribute[0]] = atribute[1].run(ast, env)
        env.table[self.id] = Symbol(self.line,self.column,atributes,ExpressionType.INTERFACE)
        env.table[self.id].interface = self.id_object
        env.table[self.id].constant = self.constant
        return
