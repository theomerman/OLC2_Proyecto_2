from controllers.environment.symbol import Symbol
from controllers.environment.ast import Ast
from controllers.environment.error import Error
from controllers.environment.types import ExpressionType


class Environment:
    def __init__(self, previus, id: str):
        self.previus = previus
        self.id = id
        self.table = {}
        self.interfaces = {}
        self.functions = {}

    def save_variable(self, ast: Ast, id: str, symbol: Symbol, line, column):
        if id in self.table:
            ast.add_error(Error(
                f"La variable \"{id}\" ya existe",
                self.id,
                "Semantico",
                line,
                column
            )
            )
            return
        self.table[id] = symbol

    def get_variable(self, ast: Ast, id: str):
        # print(self.id, self.table)
        if id in self.table:
            return self.table[id]
        if self.previus is not None:
            return self.previus.get_variable(ast, id)
        ast.add_error(Error(
            f"La variable \"{id}\" no existe",
            self.id,
            "Semantico",
            0,
            0
        )
        )
        return Symbol(0, 0, ExpressionType.NULL.name, ExpressionType.NULL)

    def update_variable(self, ast: Ast, id: str, operator: str, symbol: Symbol, line, column):
        # print(operator)
        if id in self.table:

            if self.table[id].constant:
                ast.add_error(Error(
                    f"La variable \"{id}\" es constante y no se puede modificar",
                    self.id,
                    "Semantico",
                    line,
                    column
                )
                )
                return

            if self.table[id].type != symbol.type:
                ast.add_error(Error(
                    f"La variable \"{id}\" no es del mismo tipo",
                    self.id,
                    "Semantico",
                    line,
                    column
                )
                )
                return
            if operator == "=":
                self.table[id] = symbol
                # print(symbol.value)
                # self.table[id].value = symbol.value
                # self.table[id].array_type = symbol.array_type
                # self.table[id].interface = symbol.interface
                # self.table[id].type = symbol.type
                # self.table[id].col = symbol.col
                # self.table[id].line = symbol.line
                return
            elif operator == "+=":
                if self.table[id].type not in [ExpressionType.NUMBER, ExpressionType.STRING, ExpressionType.FLOAT]:
                    ast.add_error(Error(
                        f"No se puede incrementar una variable de tipo {self.table[id].type}",
                        self.id,
                        "Semantico",
                        line,
                        column
                    )
                    )
                    return
                if self.table[id].type == symbol.type:
                    self.table[id].value += symbol.value
                    return
                return
            elif operator == "-=":
                if self.table[id].type not in [ExpressionType.NUMBER, ExpressionType.FLOAT]:
                    ast.add_error(Error(
                        f"No se puede decrementar una variable de tipo {self.table[id].type}",
                        self.id,
                        "Semantico",
                        line,
                        column
                    )
                    )
                    return
                if self.table[id].type == symbol.type:
                    self.table[id].value -= symbol.value
                    return
                return
            elif operator == "++":
                if self.table[id].type != ExpressionType.NUMBER:
                    ast.add_error(Error(
                        f"No se puede incrementar una variable de tipo {self.table[id].type}",
                        self.id,
                        "Semantico",
                        line,
                        column
                    )
                    )
                    return
                self.table[id].value += 1
                return
            elif operator == "--":
                if self.table[id].type != ExpressionType.NUMBER:
                    ast.add_error(Error(
                        f"No se puede decrementar una variable de tipo {self.table[id].type}",
                        self.id,
                        "Semantico",
                        line,
                        column
                    )
                    )
                    return
                self.table[id].value -= 1
                return
            return
        if self.previus is not None:
            self.previus.update_variable(
                ast, id, operator, symbol, line, column)
            return
        ast.add_error(Error(
            f"La variable \"{id}\" no existe",
            self.id,
            "Semantico",
            line,
            column
        )
        )
    def set_interface(self, ast: Ast, id: str, atributes: dict, line, column):
        if self.id != "global":
            ast.add_error(Error(
            f"Las interfaces solo se pueden declarar en el ambito global",
            self.id,
            "Semantico",
            line,
            column
            )
            )
            return
        if id in self.interfaces:
            ast.add_error(Error(
                f"La interfaz \"{id}\" ya existe",
                self.id,
                "Semantico",
                line,
                column
            )
            )
            return
        self.interfaces[id] = atributes

