from controllers.interfaces.expression import Expression
from controllers.environment.ast import Ast
from controllers.environment.environment import Environment
from controllers.environment.types import ExpressionType
from controllers.environment.symbol import Symbol
from controllers.expressions.primitive import Primitive
from controllers.environment.error import Error
from controllers.environment.generator import Generator
from controllers.environment.value import Value


class Operation(Expression):
    def __init__(self, left, operator, right,  line, column):
        self.left = left
        self.right = right
        self.operator = operator
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment, gen: Generator) -> Value:
        left = None
        right = self.right.run(ast, env, gen)
        if self.operator not in ['--', '!']:
            left = self.left.run(ast, env, gen)
        if self.operator == '+':
            value_object = sum(gen, left, right, self.line, self.column)
            if value_object.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede sumar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return value_object
        if self.operator == '-':
            value_object = sub(gen, left, right, self.line, self.column)
            if value_object.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede restar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return value_object
        if self.operator == '*':
            value_object = mul(gen, left, right, self.line, self.column)
            if value_object.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede multiplicar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return value_object
        if self.operator == '/':
            value_object = div(gen, left, right, self.line, self.column)
            if value_object.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede dividir {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return value_object
        # if self.operator == '%':
        #     symbol = mod(left, right, self.line, self.column)
        #     if symbol.type == ExpressionType.NULL:
        #         ast.add_error(
        #             Error(
        #                 f"No se puede modular {left.type.name} con {right.type.name}",
        #                 env.id,
        #                 "Semantico",
        #                 self.line,
        #                 self.column
        #             )
        #         )
        #     return symbol
        # if self.operator == '--':
        #     symbol = unary_minus(right, self.line, self.column)
        #     if symbol.type == ExpressionType.NULL:
        #         ast.add_error(
        #             Error(
        #                 f"No se puede negar {right.type.name}",
        #                 env.id,
        #                 "Semantico",
        #                 self.line,
        #                 self.column
        #             )
        #         )
        #     return symbol
        # if self.operator == '==':
        #     symbol = equal(left, right, self.line, self.column)
        #     if symbol.type == ExpressionType.NULL:
        #         ast.add_error(
        #             Error(
        #                 f"No se puede comparar {left.type.name} con {right.type.name}",
        #                 env.id,
        #                 "Semantico",
        #                 self.line,
        #                 self.column
        #             )
        #         )
        #     return symbol
        # if self.operator == '!=':
        #     symbol = different(left, right, self.line, self.column)
        #     if symbol.type == ExpressionType.NULL:
        #         ast.add_error(
        #             Error(
        #                 f"No se puede comparar {left.type.name} con {right.type.name}",
        #                 env.id,
        #                 "Semantico",
        #                 self.line,
        #                 self.column
        #             )
        #         )
        #     return symbol
        # if self.operator == '>':
        #     symbol = greater_than(left, right, self.line, self.column)
        #     if symbol.type == ExpressionType.NULL:
        #         ast.add_error(
        #             Error(
        #                 f"No se puede comparar {left.type.name} con {right.type.name}",
        #                 env.id,
        #                 "Semantico",
        #                 self.line,
        #                 self.column
        #             )
        #         )
        #     return symbol
        # if self.operator == '<':
        #     symbol = less_than(left, right, self.line, self.column)
        #     if symbol.type == ExpressionType.NULL:
        #         ast.add_error(
        #             Error(
        #                 f"No se puede comparar {left.type.name} con {right.type.name}",
        #                 env.id,
        #                 "Semantico",
        #                 self.line,
        #                 self.column
        #             )
        #         )
        #     return symbol
        # if self.operator == '>=':
        #     symbol = greater_than_or_equal(left, right, self.line, self.column)
        #     if symbol.type == ExpressionType.NULL:
        #         ast.add_error(
        #             Error(
        #                 f"No se puede comparar {left.type.name} con {right.type.name}",
        #                 env.id,
        #                 "Semantico",
        #                 self.line,
        #                 self.column
        #             )
        #         )
        #     return symbol
        # if self.operator == '<=':
        #     symbol = less_than_or_equal(left, right, self.line, self.column)
        #     if symbol.type == ExpressionType.NULL:
        #         ast.add_error(
        #             Error(
        #                 f"No se puede comparar {left.type.name} con {right.type.name}",
        #                 env.id,
        #                 "Semantico",
        #                 self.line,
        #                 self.column
        #             )
        #         )
        #     return symbol
        # if self.operator == '&&':
        #     symbol = and_op(left, right, self.line, self.column)
        #     if symbol.type == ExpressionType.NULL:
        #         ast.add_error(
        #             Error(
        #                 f"No se puede operar {left.type.name} con {right.type.name}",
        #                 env.id,
        #                 "Semantico",
        #                 self.line,
        #                 self.column
        #             )
        #         )
        #     return symbol
        # if self.operator == '||':
        #     symbol = or_op(left, right, self.line, self.column)
        #     if symbol.type == ExpressionType.NULL:
        #         ast.add_error(
        #             Error(
        #                 f"No se puede operar {left.type.name} con {right.type.name}",
        #                 env.id,
        #                 "Semantico",
        #                 self.line,
        #                 self.column
        #             )
        #         )
        #     return symbol
        # if self.operator == '!':
        #     symbol = negation(right, self.line, self.column)
        #     if symbol.type == ExpressionType.NULL:
        #         ast.add_error(
        #             Error(
        #                 f"No se puede negar {right.type.name}",
        #                 env.id,
        #                 "Semantico",
        #                 self.line,
        #                 self.column
        #             )
        #         )
        #     return symbol


def sum(gen: Generator, left: Primitive, right: Primitive, line, column) -> Value:
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            # return Symbol(line, column, left.value + right.value, ExpressionType.NUMBER)
            
            # gen.add_li("t0", gen.get_base())
            gen.add_li("t0", left.value)
            gen.add_lw("t0", gen.offset, "t0")
            gen.add_li("t1", right.value)
            gen.add_lw("t1", gen.offset, "t1")

            gen.code.append("\tadd t2, t0, t1\n")
            gen.base += 4
            gen.add_li("t0",gen.base)
            gen.add_sw("t2",gen.offset,"t0")
            return Value(str(gen.base),ExpressionType.NUMBER, line, column)
    #     if right.type == ExpressionType.FLOAT:
    #         return Symbol(line, column, left.value + right.value, ExpressionType.FLOAT)
    # if left.type == ExpressionType.FLOAT:
    #     if right.type == ExpressionType.NUMBER:
    #         return Symbol(line, column, left.value + right.value, ExpressionType.FLOAT)
    #     if right.type == ExpressionType.FLOAT:
    #         return Symbol(line, column, left.value + right.value, ExpressionType.FLOAT)
    # if left.type == ExpressionType.STRING:
    #     if right.type == ExpressionType.STRING:
    #         return Symbol(line, column, left.value + right.value, ExpressionType.STRING)
    #
    # return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
    return Value("x0", ExpressionType.NULL, line, column)


def sub(gen: Generator, left: Primitive, right: Primitive, line, column) -> Value:
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            # return Symbol(line, column, left.value + right.value, ExpressionType.NUMBER)
            
            # gen.add_li("t0", gen.get_base())
            gen.add_li("t0", left.value)
            gen.add_lw("t0", gen.offset, "t0")
            gen.add_li("t1", right.value)
            gen.add_lw("t1", gen.offset, "t1")

            gen.code.append("\tsub t2, t0, t1\n")
            gen.base += 4
            gen.add_li("t0",gen.base)
            gen.add_sw("t2",gen.offset,"t0")
    return Value(str(gen.base),ExpressionType.NUMBER, line, column)
#     if left.type == ExpressionType.NUMBER:
#         if right.type == ExpressionType.NUMBER:
#             return Symbol(line, column, left.value - right.value, ExpressionType.NUMBER)
#         if right.type == ExpressionType.FLOAT:
#             return Symbol(line, column, left.value - right.value, ExpressionType.FLOAT)
#     if left.type == ExpressionType.FLOAT:
#         if right.type == ExpressionType.NUMBER:
#             return Symbol(line, column, left.value - right.value, ExpressionType.FLOAT)
#         if right.type == ExpressionType.FLOAT:
#             return Symbol(line, column, left.value - right.value, ExpressionType.FLOAT)
#     return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
#
#
def mul(gen: Generator, left: Primitive, right: Primitive, line, column) -> Value:
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            # return Symbol(line, column, left.value + right.value, ExpressionType.NUMBER)
            
            # gen.add_li("t0", gen.get_base())
            gen.add_li("t0", left.value)
            gen.add_lw("t0", gen.offset, "t0")
            gen.add_li("t1", right.value)
            gen.add_lw("t1", gen.offset, "t1")

            gen.code.append("\tmul t2, t0, t1\n")
            gen.base += 4
            gen.add_li("t0",gen.base)
            gen.add_sw("t2", gen.offset,"t0")
    return Value(str(gen.base),ExpressionType.NUMBER, line, column)
#     if left.type == ExpressionType.NUMBER:
#         if right.type == ExpressionType.NUMBER:
#             return Symbol(line, column, left.value * right.value, ExpressionType.NUMBER)
#         if right.type == ExpressionType.FLOAT:
#             return Symbol(line, column, left.value * right.value, ExpressionType.FLOAT)
#     if left.type == ExpressionType.FLOAT:
#         if right.type == ExpressionType.NUMBER:
#             return Symbol(line, column, left.value * right.value, ExpressionType.FLOAT)
#         if right.type == ExpressionType.FLOAT:
#             return Symbol(line, column, left.value * right.value, ExpressionType.FLOAT)
#     return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
#
#
def div(gen: Generator, left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            # return Symbol(line, column, left.value + right.value, ExpressionType.NUMBER)
            
            # gen.add_li("t0", gen.get_base())
            gen.add_li("t0", left.value)
            gen.add_lw("t0", gen.offset, "t0")
            gen.add_li("t1", right.value)
            gen.add_lw("t1", gen.offset, "t1")

            gen.code.append("\tdiv t2, t0, t1\n")
            gen.base += 4
            gen.add_li("t0",gen.base)
            gen.add_sw("t2",gen.offset,"t0")
    return Value(str(gen.base),ExpressionType.NUMBER, line, column)
#     if left.type == ExpressionType.NUMBER:
#         if right.type == ExpressionType.NUMBER:
#             if right.value != 0:
#                 return Symbol(line, column, left.value / right.value, ExpressionType.NUMBER)
#             return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
#         if right.type == ExpressionType.FLOAT:
#             if right.value != 0:
#                 return Symbol(line, column, left.value / right.value, ExpressionType.FLOAT)
#             return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
#     if left.type == ExpressionType.FLOAT:
#         if right.type == ExpressionType.NUMBER:
#             if right.value != 0:
#                 return Symbol(line, column, left.value / right.value, ExpressionType.FLOAT)
#             return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
#         if right.type == ExpressionType.FLOAT:
#             if right.value != 0:
#                 return Symbol(line, column, left.value / right.value, ExpressionType.FLOAT)
#             return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
#     return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
#
#
# def mod(left: Primitive, right: Primitive, line, column):
#     if left.type == ExpressionType.NUMBER:
#         if right.type == ExpressionType.NUMBER:
#             if right.value != 0:
#                 return Symbol(line, column, left.value % right.value, ExpressionType.NUMBER)
#             return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
#     return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
#
#
# def unary_minus(exp: Primitive, line, column):
#     if exp.type == ExpressionType.NUMBER:
#         return Symbol(line, column, -exp.value, ExpressionType.NUMBER)
#     if exp.type == ExpressionType.FLOAT:
#         return Symbol(line, column, -exp.value, ExpressionType.FLOAT)
#     return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
#
#
# def equal(left: Primitive, right: Primitive, line, column):
#     if left.type == ExpressionType.NUMBER:
#         if right.type == ExpressionType.NUMBER:
#             return Symbol(line, column, left.value == right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.FLOAT:
#         if right.type == ExpressionType.FLOAT:
#             return Symbol(line, column, left.value == right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.BOOLEAN:
#         if right.type == ExpressionType.BOOLEAN:
#             return Symbol(line, column, left.value == right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.STRING:
#         if right.type == ExpressionType.STRING:
#             return Symbol(line, column, left.value == right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.CHAR:
#         if right.type == ExpressionType.CHAR:
#             return Symbol(line, column, left.value == right.value, ExpressionType.BOOLEAN)
#     return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
#
#
# def different(left: Primitive, right: Primitive, line, column):
#     if left.type == ExpressionType.NUMBER:
#         if right.type == ExpressionType.NUMBER:
#             return Symbol(line, column, left.value != right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.FLOAT:
#         if right.type == ExpressionType.FLOAT:
#             return Symbol(line, column, left.value != right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.BOOLEAN:
#         if right.type == ExpressionType.BOOLEAN:
#             return Symbol(line, column, left.value != right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.STRING:
#         if right.type == ExpressionType.STRING:
#             return Symbol(line, column, left.value != right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.CHAR:
#         if right.type == ExpressionType.CHAR:
#             return Symbol(line, column, left.value != right.value, ExpressionType.BOOLEAN)
#     return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
#
#
# def greater_than(left: Primitive, right: Primitive, line, column):
#     if left.type == ExpressionType.NUMBER:
#         if right.type == ExpressionType.NUMBER:
#             return Symbol(line, column, left.value > right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.FLOAT:
#         if right.type == ExpressionType.FLOAT:
#             return Symbol(line, column, left.value > right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.STRING:
#         if right.type == ExpressionType.STRING:
#             return Symbol(line, column, left.value > right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.CHAR:
#         if right.type == ExpressionType.CHAR:
#             return Symbol(line, column, left.value > right.value, ExpressionType.BOOLEAN)
#     return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
#
#
# def less_than(left: Primitive, right: Primitive, line, column):
#     if left.type == ExpressionType.NUMBER:
#         if right.type == ExpressionType.NUMBER:
#             return Symbol(line, column, left.value < right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.FLOAT:
#         if right.type == ExpressionType.FLOAT:
#             return Symbol(line, column, left.value < right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.STRING:
#         if right.type == ExpressionType.STRING:
#             return Symbol(line, column, left.value < right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.CHAR:
#         if right.type == ExpressionType.CHAR:
#             return Symbol(line, column, left.value < right.value, ExpressionType.BOOLEAN)
#     return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
#
#
# def greater_than_or_equal(left: Primitive, right: Primitive, line, column):
#     if left.type == ExpressionType.NUMBER:
#         if right.type == ExpressionType.NUMBER:
#             return Symbol(line, column, left.value >= right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.FLOAT:
#         if right.type == ExpressionType.FLOAT:
#             return Symbol(line, column, left.value >= right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.STRING:
#         if right.type == ExpressionType.STRING:
#             return Symbol(line, column, left.value >= right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.CHAR:
#         if right.type == ExpressionType.CHAR:
#             return Symbol(line, column, left.value >= right.value, ExpressionType.BOOLEAN)
#     return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
#
#
# def less_than_or_equal(left: Primitive, right: Primitive, line, column):
#     if left.type == ExpressionType.NUMBER:
#         if right.type == ExpressionType.NUMBER:
#             return Symbol(line, column, left.value <= right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.FLOAT:
#         if right.type == ExpressionType.FLOAT:
#             return Symbol(line, column, left.value <= right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.STRING:
#         if right.type == ExpressionType.STRING:
#             return Symbol(line, column, left.value <= right.value, ExpressionType.BOOLEAN)
#     if left.type == ExpressionType.CHAR:
#         if right.type == ExpressionType.CHAR:
#             return Symbol(line, column, left.value <= right.value, ExpressionType.BOOLEAN)
#     return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
#
#
# def and_op(left: Primitive, right: Primitive, line, column):
#     if left.type == ExpressionType.BOOLEAN and right.type == ExpressionType.BOOLEAN:
#         return Symbol(line, column, left.value and right.value, ExpressionType.BOOLEAN)
#     return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
#
#
# def or_op(left: Primitive, right: Primitive, line, column):
#     if left.type == ExpressionType.BOOLEAN and right.type == ExpressionType.BOOLEAN:
#         return Symbol(line, column, left.value or right.value, ExpressionType.BOOLEAN)
#     return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
#
#
# def negation(exp: Primitive, line, column):
#     if exp.type == ExpressionType.BOOLEAN:
#         return Symbol(line, column, not exp.value, ExpressionType.BOOLEAN)
#     return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
