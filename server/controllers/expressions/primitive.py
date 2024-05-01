from icecream import ic
from controllers.interfaces.expression import Expression
from controllers.environment.symbol import Symbol
from controllers.environment.ast import Ast
from controllers.environment.environment import Environment
from controllers.environment.types import ExpressionType
from controllers.environment.generator import Generator
from controllers.environment.value import Value

class Primitive(Expression):
    def __init__(self, value, type: ExpressionType, line, column):
        self.value = value
        self.type = type
        self.line = line
        self.column = column
        # self.symbol = Symbol(self.line, self.column, self.value, self.type)
        # self.value_object = Value(value, True, self.type, [],[],[])
        self.value_object = Value(value, type, self.line, self.column)

    def run(self, ast: Ast, env: Environment, gen: Generator):
        # return Symbol(self.line, self.column, self.value, self.type)
        self.value_object.generic = self.value
        if self.type == ExpressionType.NUMBER:
            gen.base += 4
            gen.add_li("t0", self.value)
            gen.add_li("t1", str(gen.base))
            gen.add_sw("t0", gen.offset, "t1")

            # arr = gen.code if gen.target == "code" else gen.labels
            # arr.append(f"\tli t0, {self.value}\n")
            # arr.append(f"\tli t1, {str(gen.base)}\n")
            # arr.append(f"\tsw t0, {gen.offset}(t1)\n")
            self.value_object.value = gen.base
            return self.value_object
        if self.type == ExpressionType.STRING:
            gen.data += f"str{gen.string_counter}: .string \"{self.value}\"\n"
            self.value_object.value = "str" + str(gen.string_counter)
            gen.string_counter += 1
            return self.value_object
        if self.type == ExpressionType.FLOAT:
            gen.float_counter += 1
            gen.data += f"fl{gen.float_counter}: .float {self.value}\n"
            self.value_object.value = "fl" + str(gen.float_counter)
            return self.value_object
        if self.type == ExpressionType.BOOLEAN:
            gen.base += 4
            tmp = 1 if self.value else 0
            gen.add_li("t0", tmp)
            gen.add_li("t1", str(gen.base))
            gen.add_sw("t0", gen.offset, "t1")
            self.value_object.value = gen.base
            return self.value_object
        if self.type == ExpressionType.CHAR:
            gen.data += f"str{gen.string_counter}: .string \"{self.value}\"\n"
            self.value_object.value = "str" + str(gen.string_counter)
            gen.string_counter += 1
            return self.value_object

        return Value("x0", ExpressionType.NULL, self.line, self.column)

    def getType(self):
        return self.type
