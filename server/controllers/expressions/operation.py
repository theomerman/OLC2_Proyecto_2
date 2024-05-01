from icecream import ic
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
        if self.operator == '%':
            symbol = mod(gen, left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede modular {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '--':
            symbol = unary_minus(gen, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede negar {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '==':
            symbol = equal(gen, left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede comparar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '!=':
            symbol = different(gen, left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede comparar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '>':
            symbol = greater_than(gen, left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede comparar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '<':
            symbol = less_than(gen, left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede comparar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '>=':
            symbol = greater_than_or_equal(gen, left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede comparar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '<=':
            symbol = less_than_or_equal(gen, left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede comparar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '&&':
            symbol = and_op(gen, left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede operar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '||':
            symbol = or_op(gen, left, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede operar {left.type.name} con {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol
        if self.operator == '!':
            symbol = negation(gen, right, self.line, self.column)
            if symbol.type == ExpressionType.NULL:
                ast.add_error(
                    Error(
                        f"No se puede negar {right.type.name}",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                    )
                )
            return symbol


def sum(gen: Generator, left: Primitive, right: Primitive, line, column) -> Value:
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            # return Symbol(line, column, left.value + right.value, ExpressionType.NUMBER)

            # gen.add_li("t0", left.value)
            # gen.add_lw("t0", gen.offset, "t0")
            # gen.add_li("t1", right.value)
            # gen.add_lw("t1", gen.offset, "t1")
            #
            # gen.code.append("\tadd t2, t0, t1\n")
            # gen.base += 4
            # gen.add_li("t0",gen.base)
            # gen.add_sw("t2",gen.offset,"t0")


            arr = gen.code if gen.target == "code" else gen.labels
            arr.append(f"\tli t0, {left.value}\n")
            arr.append(f"\tlw t0, {gen.offset}(t0)\n")
            arr.append(f"\tli t1, {str(right.value)}\n")
            arr.append(f"\tlw t1, {gen.offset}(t1)\n")
            arr.append(f"\tadd t2, t0, t1\n")
            gen.base += 4
            arr.append(f"\tli t0, {str(gen.base)}\n")
            arr.append(f"\tsw t2, {gen.offset}(t0)\n")

            return Value(str(gen.base),ExpressionType.NUMBER, line, column)
    if left.type == ExpressionType.FLOAT:
        if right.type == ExpressionType.FLOAT:
            try:
                left_tmp = int(left.value)
                gen.add_li("t0", str(left_tmp))
                gen.code.append(f"\tflw f1 {gen.offset}(t0)\n")
            except:
                gen.add_flw("ft1", left.value, "t3")

            try:
                right_tmp = int(right.value)
                gen.add_li("t0", str(right_tmp))
                gen.code.append(f"\tflw f2 {gen.offset}(t0)\n")
            except:
                gen.add_flw("ft2", right.value, "t3")


                # gen.add_flw("ft1", left.value, "t3")
                # gen.add_flw("ft2", right.value, "t3")
            gen.code.append(f"\tfadd.s f1, f1, f2\n")

            gen.base += 4
            gen.add_li("t1", gen.base)
            gen.add_fsw("f1", "t1")
            return Value(str(gen.base),ExpressionType.FLOAT, line, column)
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
            # gen.add_li("t0", left.value)
            # gen.add_lw("t0", gen.offset, "t0")
            # gen.add_li("t1", right.value)
            # gen.add_lw("t1", gen.offset, "t1")
            #
            # gen.code.append("\tsub t2, t0, t1\n")
            # gen.base += 4
            # gen.add_li("t0",gen.base)
            # gen.add_sw("t2",gen.offset,"t0")

            arr = gen.code if gen.target == "code" else gen.labels
            arr.append(f"\tli t0, {left.value}\n")
            arr.append(f"\tlw t0, {gen.offset}(t0)\n")
            arr.append(f"\tli t1, {str(right.value)}\n")
            arr.append(f"\tlw t1, {gen.offset}(t1)\n")
            arr.append(f"\tsub t2, t0, t1\n")
            gen.base += 4
            arr.append(f"\tli t0, {str(gen.base)}\n")
            arr.append(f"\tsw t2, {gen.offset}(t0)\n")
            return Value(str(gen.base),ExpressionType.NUMBER, line, column)
    if left.type == ExpressionType.FLOAT:
        if right.type == ExpressionType.FLOAT:
            try:
                left_tmp = int(left.value)
                gen.add_li("t0", str(left_tmp))
                gen.code.append(f"\tflw f1 {gen.offset}(t0)\n")
            except:
                gen.add_flw("ft1", left.value, "t3")

            try:
                right_tmp = int(right.value)
                gen.add_li("t0", str(right_tmp))
                gen.code.append(f"\tflw f2 {gen.offset}(t0)\n")
            except:
                gen.add_flw("ft2", right.value, "t3")
            gen.code.append(f"\tfsub.s f1, f1, f2\n")

            gen.base += 4
            gen.add_li("t1", gen.base)
            gen.add_fsw("f1", "t1")
            return Value(str(gen.base),ExpressionType.FLOAT, line, column)
    return Value("x0", ExpressionType.NULL, line, column)
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


def mul(gen: Generator, left: Primitive, right: Primitive, line, column) -> Value:
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            # return Symbol(line, column, left.value + right.value, ExpressionType.NUMBER)
            
            # gen.add_li("t0", left.value)
            # gen.add_lw("t0", gen.offset, "t0")
            # gen.add_li("t1", right.value)
            # gen.add_lw("t1", gen.offset, "t1")
            #
            # gen.code.append("\tmul t2, t0, t1\n")
            # gen.base += 4
            # gen.add_li("t0",gen.base)
            # gen.add_sw("t2", gen.offset,"t0")
            arr = gen.code if gen.target == "code" else gen.labels
            arr.append(f"\tli t0, {left.value}\n")
            arr.append(f"\tlw t0, {gen.offset}(t0)\n")
            arr.append(f"\tli t1, {str(right.value)}\n")
            arr.append(f"\tlw t1, {gen.offset}(t1)\n")
            arr.append(f"\tmul t2, t0, t1\n")
            gen.base += 4
            arr.append(f"\tli t0, {str(gen.base)}\n")
            arr.append(f"\tsw t2, {gen.offset}(t0)\n")
            return Value(str(gen.base),ExpressionType.NUMBER, line, column)
    if left.type == ExpressionType.FLOAT:
        if right.type == ExpressionType.FLOAT:
            try:
                left_tmp = int(left.value)
                gen.add_li("t0", str(left_tmp))
                gen.code.append(f"\tflw f1 {gen.offset}(t0)\n")
            except:
                gen.add_flw("ft1", left.value, "t3")

            try:
                right_tmp = int(right.value)
                gen.add_li("t0", str(right_tmp))
                gen.code.append(f"\tflw f2 {gen.offset}(t0)\n")
            except:
                gen.add_flw("ft2", right.value, "t3")
            gen.code.append(f"\tfmul.s f1, f1, f2\n")

            gen.base += 4
            gen.add_li("t1", gen.base)
            gen.add_fsw("f1", "t1")
            return Value(str(gen.base),ExpressionType.FLOAT, line, column)
    return Value("x0", ExpressionType.NULL, line, column)
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
            # gen.add_li("t0", left.value)
            # gen.add_lw("t0", gen.offset, "t0")
            # gen.add_li("t1", right.value)
            # gen.add_lw("t1", gen.offset, "t1")
            #
            # gen.code.append("\tdiv t2, t0, t1\n")
            # gen.base += 4
            # gen.add_li("t0",gen.base)
            # gen.add_sw("t2",gen.offset,"t0")
            arr = gen.code if gen.target == "code" else gen.labels
            arr.append(f"\tli t0, {left.value}\n")
            arr.append(f"\tlw t0, {gen.offset}(t0)\n")
            arr.append(f"\tli t1, {str(right.value)}\n")
            arr.append(f"\tlw t1, {gen.offset}(t1)\n")
            arr.append(f"\tdiv t2, t0, t1\n")
            gen.base += 4
            arr.append(f"\tli t0, {str(gen.base)}\n")
            arr.append(f"\tsw t2, {gen.offset}(t0)\n")
            return Value(str(gen.base),ExpressionType.NUMBER, line, column)
    if left.type == ExpressionType.FLOAT:
        if right.type == ExpressionType.FLOAT:
            try:
                left_tmp = int(left.value)
                gen.add_li("t0", str(left_tmp))
                gen.code.append(f"\tflw f1 {gen.offset}(t0)\n")
            except:
                gen.add_flw("ft1", left.value, "t3")

            try:
                right_tmp = int(right.value)
                gen.add_li("t0", str(right_tmp))
                gen.code.append(f"\tflw f2 {gen.offset}(t0)\n")
            except:
                gen.add_flw("ft2", right.value, "t3")
            gen.code.append(f"\tfdiv.s f1, f1, f2\n")

            gen.base += 4
            gen.add_li("t1", gen.base)
            gen.add_fsw("f1", "t1")
            return Value(str(gen.base),ExpressionType.FLOAT, line, column)
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
def mod(gen: Generator, left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            if right.value != 0:
                arr = gen.code if gen.target == "code" else gen.labels
                gen.add_li("t0", str(left.value))
                gen.add_lw("t0", str(gen.offset), "t0")
                gen.add_li("t1", str(right.value))
                gen.add_lw("t1", str(gen.offset), "t1")
                arr.append(f"\trem t0, t0, t1\n")
                gen.base += 4
                gen.add_li("t1", gen.base)
                gen.add_sw("t0", gen.offset, "t1")
                # return Symbol(line, column, left.value % right.value, ExpressionType.NUMBER)
                return Value(str(gen.base), ExpressionType.NUMBER, line, column)

            # return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
            return Value("x0", ExpressionType.NULL, line, column)
    # return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
    return Value("x0", ExpressionType.NULL, line, column)


def unary_minus(gen: Generator, exp: Primitive, line, column):
    if exp.type == ExpressionType.NUMBER:
        # return Symbol(line, column, -exp.value, ExpressionType.NUMBER)
        arr = gen.code if gen.target == "code" else gen.labels
        gen.add_li("t0", str(exp.value))
        gen.add_lw("t0", str(gen.offset), "t0")
        gen.add_li("t1", str(-1))
        arr.append(f"\tmul t0, t0, t1\n")
        gen.add_li("t1", str(exp.value))
        gen.add_sw("t0", gen.offset, "t1")
        return Value(str(exp.value),ExpressionType.NUMBER, line, column)
    if exp.type == ExpressionType.FLOAT:
        # return Symbol(line, column, -exp.value, ExpressionType.FLOAT)
        gen.float_counter += 1
        gen.data.append(f"fl{str(gen.float_counter)}: .float -1.0\n")
        gen.add_flw("ft0", f"fl{str(gen.float_counter)}", "t3")
        gen.add_flw("ft1", f"{str(exp.value)}", "t3")
        gen.code.append(f"\tfmul.s f0, f1, f0\n")
        gen.code.append(f"\tfsw f0, {str(exp.value)}, t3\n")
        return Value(str(exp.value),ExpressionType.FLOAT, line, column)
    # return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
    return Value("x0", ExpressionType.NULL, line, column)


def equal(gen: Generator, left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            gen.base += 4
            gen.label_counter += 2
            arr = gen.code if gen.target == "code" else gen.labels
            arr.append(f"\tli t0, {left.value}\n")
            arr.append(f"\tlw t0, {gen.offset}(t0)\n")
            arr.append(f"\tli t1, {right.value}\n")
            arr.append(f"\tlw t1, {gen.offset}(t1)\n")
            arr.append(f"\tbeq t0, t1, if_true{gen.label_counter}\n")
            arr.append(f"\tli t0, {str(gen.base)}\n")
            arr.append(f"\tli t1, 0\n")
            arr.append(f"\tsw t1, {gen.offset}(t0)\n")
            arr.append(f"\tj if_exit{gen.label_counter - 1}\n")
            arr.append(f"if_exit{gen.label_counter - 1}:\n")

            tmp = []
            tmp.append(f"if_true{gen.label_counter}:\n")
            tmp.append(f"\tli t0, {str(gen.base)}\n")
            tmp.append(f"\tli t1, 1\n")
            tmp.append(f"\tsw t1, {gen.offset}(t0)\n")
            tmp.append(f"\tj if_exit{gen.label_counter - 1}\n")
            gen.labels = tmp + gen.labels
            return Value(str(gen.base), ExpressionType.BOOLEAN, line, column)
            # return Symbol(line, column, left.value == right.value, ExpressionType.BOOLEAN)
    # if left.type == ExpressionType.FLOAT:
    #     if right.type == ExpressionType.FLOAT:
    #         return Symbol(line, column, left.value == right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.BOOLEAN:
        if right.type == ExpressionType.BOOLEAN:
            gen.base += 4
            gen.label_counter += 2
            arr = gen.code if gen.target == "code" else gen.labels
            arr.append(f"\tli t0, {left.value}\n")
            arr.append(f"\tlw t0, {gen.offset}(t0)\n")
            arr.append(f"\tli t1, {right.value}\n")
            arr.append(f"\tlw t1, {gen.offset}(t1)\n")
            arr.append(f"\tbeq t0, t1, if_true{gen.label_counter}\n")
            arr.append(f"\tli t0, {str(gen.base)}\n")
            arr.append(f"\tli t1, 0\n")
            arr.append(f"\tsw t1, {gen.offset}(t0)\n")
            arr.append(f"\tj if_exit{gen.label_counter - 1}\n")
            arr.append(f"if_exit{gen.label_counter - 1}:\n")

            tmp = []
            tmp.append(f"if_true{gen.label_counter}:\n")
            tmp.append(f"\tli t0, {str(gen.base)}\n")
            tmp.append(f"\tli t1, 1\n")
            tmp.append(f"\tsw t1, {gen.offset}(t0)\n")
            tmp.append(f"\tj if_exit{gen.label_counter - 1}\n")
            gen.labels = tmp + gen.labels
            return Value(str(gen.base), ExpressionType.BOOLEAN, line, column)
            # return Symbol(line, column, left.value == right.value, ExpressionType.BOOLEAN)
    # if left.type == ExpressionType.STRING:
    #     if right.type == ExpressionType.STRING:
    #         return Symbol(line, column, left.value == right.value, ExpressionType.BOOLEAN)
    # if left.type == ExpressionType.CHAR:
    #     if right.type == ExpressionType.CHAR:
    #         return Symbol(line, column, left.value == right.value, ExpressionType.BOOLEAN)
    # return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
    return Value("x0", ExpressionType.NULL, line, column)


def different(gen: Generator, left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            # return Symbol(line, column, left.value != right.value, ExpressionType.BOOLEAN)
            gen.base += 4
            gen.label_counter += 2
            arr = gen.code if gen.target == "code" else gen.labels
            arr.append(f"\tli t0, {left.value}\n")
            arr.append(f"\tlw t0, {gen.offset}(t0)\n")
            arr.append(f"\tli t1, {right.value}\n")
            arr.append(f"\tlw t1, {gen.offset}(t1)\n")
            arr.append(f"\tbne t0, t1, if_true{gen.label_counter}\n")
            arr.append(f"\tli t0, {str(gen.base)}\n")
            arr.append(f"\tli t1, 0\n")
            arr.append(f"\tsw t1, {gen.offset}(t0)\n")
            arr.append(f"\tj if_exit{gen.label_counter - 1}\n")
            arr.append(f"if_exit{gen.label_counter - 1}:\n")

            tmp = []
            tmp.append(f"if_true{gen.label_counter}:\n")
            tmp.append(f"\tli t0, {str(gen.base)}\n")
            tmp.append(f"\tli t1, 1\n")
            tmp.append(f"\tsw t1, {gen.offset}(t0)\n")
            tmp.append(f"\tj if_exit{gen.label_counter - 1}\n")
            gen.labels = tmp + gen.labels
            return Value(str(gen.base), ExpressionType.BOOLEAN, line, column)
    # if left.type == ExpressionType.FLOAT:
    #     if right.type == ExpressionType.FLOAT:
    #         return Symbol(line, column, left.value != right.value, ExpressionType.BOOLEAN)
    if left.type == ExpressionType.BOOLEAN:
        if right.type == ExpressionType.BOOLEAN:
            # return Symbol(line, column, left.value != right.value, ExpressionType.BOOLEAN)
            gen.base += 4
            gen.label_counter += 2
            arr = gen.code if gen.target == "code" else gen.labels
            arr.append(f"\tli t0, {left.value}\n")
            arr.append(f"\tlw t0, {gen.offset}(t0)\n")
            arr.append(f"\tli t1, {right.value}\n")
            arr.append(f"\tlw t1, {gen.offset}(t1)\n")
            arr.append(f"\tbne t0, t1, if_true{gen.label_counter}\n")
            arr.append(f"\tli t0, {str(gen.base)}\n")
            arr.append(f"\tli t1, 0\n")
            arr.append(f"\tsw t1, {gen.offset}(t0)\n")
            arr.append(f"\tj if_exit{gen.label_counter - 1}\n")
            arr.append(f"if_exit{gen.label_counter - 1}:\n")

            tmp = []
            tmp.append(f"if_true{gen.label_counter}:\n")
            tmp.append(f"\tli t0, {str(gen.base)}\n")
            tmp.append(f"\tli t1, 1\n")
            tmp.append(f"\tsw t1, {gen.offset}(t0)\n")
            tmp.append(f"\tj if_exit{gen.label_counter - 1}\n")
            gen.labels = tmp + gen.labels
            return Value(str(gen.base), ExpressionType.BOOLEAN, line, column)
    # if left.type == ExpressionType.STRING:
    #     if right.type == ExpressionType.STRING:
    #         return Symbol(line, column, left.value != right.value, ExpressionType.BOOLEAN)
    # if left.type == ExpressionType.CHAR:
    #     if right.type == ExpressionType.CHAR:
    #         return Symbol(line, column, left.value != right.value, ExpressionType.BOOLEAN)
    # return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
    return Value("x0", ExpressionType.NULL, line, column)


def greater_than(gen:Generator, left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            # return Symbol(line, column, left.value > right.value, ExpressionType.BOOLEAN)
            gen.base += 4
            gen.label_counter += 2
            arr = gen.code if gen.target == "code" else gen.labels
            arr.append(f"\tli t0, {left.value}\n")
            arr.append(f"\tlw t0, {gen.offset}(t0)\n")
            arr.append(f"\tli t1, {right.value}\n")
            arr.append(f"\tlw t1, {gen.offset}(t1)\n")
            arr.append(f"\tbgt t0, t1, if_true{gen.label_counter}\n")
            arr.append(f"\tli t0, {str(gen.base)}\n")
            arr.append(f"\tli t1, 0\n")
            arr.append(f"\tsw t1, {gen.offset}(t0)\n")
            arr.append(f"\tj if_exit{gen.label_counter - 1}\n")
            arr.append(f"if_exit{gen.label_counter - 1}:\n")

            tmp = []
            tmp.append(f"if_true{gen.label_counter}:\n")
            tmp.append(f"\tli t0, {str(gen.base)}\n")
            tmp.append(f"\tli t1, 1\n")
            tmp.append(f"\tsw t1, {gen.offset}(t0)\n")
            tmp.append(f"\tj if_exit{gen.label_counter - 1}\n")
            gen.labels = tmp + gen.labels
            return Value(str(gen.base), ExpressionType.BOOLEAN, line, column)
    # if left.type == ExpressionType.FLOAT:
    #     if right.type == ExpressionType.FLOAT:
    #         return Symbol(line, column, left.value > right.value, ExpressionType.BOOLEAN)
    # if left.type == ExpressionType.STRING:
    #     if right.type == ExpressionType.STRING:
    #         return Symbol(line, column, left.value > right.value, ExpressionType.BOOLEAN)
    # if left.type == ExpressionType.CHAR:
    #     if right.type == ExpressionType.CHAR:
    #         return Symbol(line, column, left.value > right.value, ExpressionType.BOOLEAN)
    # return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
    return Value("x0", ExpressionType.NULL, line, column)


def less_than(gen:Generator, left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            # return Symbol(line, column, left.value < right.value, ExpressionType.BOOLEAN)
            gen.base += 4
            gen.label_counter += 2
            arr = gen.code if gen.target == "code" else gen.labels
            arr.append(f"\tli t0, {left.value}\n")
            arr.append(f"\tlw t0, {gen.offset}(t0)\n")
            arr.append(f"\tli t1, {right.value}\n")
            arr.append(f"\tlw t1, {gen.offset}(t1)\n")
            arr.append(f"\tblt t0, t1, if_true{gen.label_counter}\n")
            arr.append(f"\tli t0, {str(gen.base)}\n")
            arr.append(f"\tli t1, 0\n")
            arr.append(f"\tsw t1, {gen.offset}(t0)\n")
            arr.append(f"\tj if_exit{gen.label_counter - 1}\n")
            arr.append(f"if_exit{gen.label_counter - 1}:\n")

            tmp = []
            tmp.append(f"if_true{gen.label_counter}:\n")
            tmp.append(f"\tli t0, {str(gen.base)}\n")
            tmp.append(f"\tli t1, 1\n")
            tmp.append(f"\tsw t1, {gen.offset}(t0)\n")
            tmp.append(f"\tj if_exit{gen.label_counter - 1}\n")
            gen.labels = tmp + gen.labels
            return Value(str(gen.base), ExpressionType.BOOLEAN, line, column)
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
    return Value("x0", ExpressionType.NULL, line, column)


def greater_than_or_equal(gen:Generator, left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            # return Symbol(line, column, left.value >= right.value, ExpressionType.BOOLEAN)
            
            gen.base += 4
            gen.label_counter += 2
            arr = gen.code if gen.target == "code" else gen.labels
            arr.append(f"\tli t0, {left.value}\n")
            arr.append(f"\tlw t0, {gen.offset}(t0)\n")
            arr.append(f"\tli t1, {right.value}\n")
            arr.append(f"\tlw t1, {gen.offset}(t1)\n")
            arr.append(f"\tbge t0, t1, if_true{gen.label_counter}\n")
            arr.append(f"\tli t0, {str(gen.base)}\n")
            arr.append(f"\tli t1, 0\n")
            arr.append(f"\tsw t1, {gen.offset}(t0)\n")
            arr.append(f"\tj if_exit{gen.label_counter - 1}\n")
            arr.append(f"if_exit{gen.label_counter - 1}:\n")

            tmp = []
            tmp.append(f"if_true{gen.label_counter}:\n")
            tmp.append(f"\tli t0, {str(gen.base)}\n")
            tmp.append(f"\tli t1, 1\n")
            tmp.append(f"\tsw t1, {gen.offset}(t0)\n")
            tmp.append(f"\tj if_exit{gen.label_counter - 1}\n")
            gen.labels = tmp + gen.labels
            return Value(str(gen.base), ExpressionType.BOOLEAN, line, column)
    # if left.type == ExpressionType.FLOAT:
    #     if right.type == ExpressionType.FLOAT:
    #         return Symbol(line, column, left.value >= right.value, ExpressionType.BOOLEAN)
    # if left.type == ExpressionType.STRING:
    #     if right.type == ExpressionType.STRING:
    #         return Symbol(line, column, left.value >= right.value, ExpressionType.BOOLEAN)
    # if left.type == ExpressionType.CHAR:
    #     if right.type == ExpressionType.CHAR:
    #         return Symbol(line, column, left.value >= right.value, ExpressionType.BOOLEAN)
    # return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
    return Value("x0", ExpressionType.NULL, line, column)


def less_than_or_equal(gen:Generator, left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.NUMBER:
        if right.type == ExpressionType.NUMBER:
            # return Symbol(line, column, left.value <= right.value, ExpressionType.BOOLEAN)
            
            gen.base += 4
            gen.label_counter += 2
            arr = gen.code if gen.target == "code" else gen.labels
            arr.append(f"\tli t0, {left.value}\n")
            arr.append(f"\tlw t0, {gen.offset}(t0)\n")
            arr.append(f"\tli t1, {right.value}\n")
            arr.append(f"\tlw t1, {gen.offset}(t1)\n")
            arr.append(f"\tble t0, t1, if_true{gen.label_counter}\n")
            arr.append(f"\tli t0, {str(gen.base)}\n")
            arr.append(f"\tli t1, 0\n")
            arr.append(f"\tsw t1, {gen.offset}(t0)\n")
            arr.append(f"\tj if_exit{gen.label_counter - 1}\n")
            arr.append(f"if_exit{gen.label_counter - 1}:\n")

            tmp = []
            tmp.append(f"if_true{gen.label_counter}:\n")
            tmp.append(f"\tli t0, {str(gen.base)}\n")
            tmp.append(f"\tli t1, 1\n")
            tmp.append(f"\tsw t1, {gen.offset}(t0)\n")
            tmp.append(f"\tj if_exit{gen.label_counter - 1}\n")
            gen.labels = tmp + gen.labels
            return Value(str(gen.base), ExpressionType.BOOLEAN, line, column)
    # if left.type == ExpressionType.FLOAT:
    #     if right.type == ExpressionType.FLOAT:
    #         return Symbol(line, column, left.value <= right.value, ExpressionType.BOOLEAN)
    # if left.type == ExpressionType.STRING:
    #     if right.type == ExpressionType.STRING:
    #         return Symbol(line, column, left.value <= right.value, ExpressionType.BOOLEAN)
    # if left.type == ExpressionType.CHAR:
    #     if right.type == ExpressionType.CHAR:
    #         return Symbol(line, column, left.value <= right.value, ExpressionType.BOOLEAN)
    # return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
    return Value("x0", ExpressionType.NULL, line, column)


def and_op(gen: Generator, left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.BOOLEAN and right.type == ExpressionType.BOOLEAN:
        # return Symbol(line, column, left.value and right.value, ExpressionType.BOOLEAN)
            gen.base += 4
            arr = gen.code if gen.target == "code" else gen.labels
            arr.append(f"\tli t0, {left.value}\n")
            arr.append(f"\tlw t0, {gen.offset}(t0)\n")
            arr.append(f"\tli t1, {right.value}\n")
            arr.append(f"\tlw t1, {gen.offset}(t1)\n")
            arr.append(f"\tand t0, t0, t1\n")
            arr.append(f"\tli t1, {str(gen.base)}\n")
            arr.append(f"\tsw t0, {gen.offset}(t1)\n")
            return Value(str(gen.base), ExpressionType.BOOLEAN, line, column)
    # return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
    return Value("x0", ExpressionType.NULL, line, column)


def or_op(gen: Generator, left: Primitive, right: Primitive, line, column):
    if left.type == ExpressionType.BOOLEAN and right.type == ExpressionType.BOOLEAN:
        # return Symbol(line, column, left.value or right.value, ExpressionType.BOOLEAN)
            gen.base += 4
            arr = gen.code if gen.target == "code" else gen.labels
            arr.append(f"\tli t0, {left.value}\n")
            arr.append(f"\tlw t0, {gen.offset}(t0)\n")
            arr.append(f"\tli t1, {right.value}\n")
            arr.append(f"\tlw t1, {gen.offset}(t1)\n")
            arr.append(f"\tor t0, t0, t1\n")
            arr.append(f"\tli t1, {str(gen.base)}\n")
            arr.append(f"\tsw t0, {gen.offset}(t1)\n")
            return Value(str(gen.base), ExpressionType.BOOLEAN, line, column)
    # return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
    return Value("x0", ExpressionType.NULL, line, column)


def negation(gen: Generator, exp: Primitive, line, column):
    if exp.type == ExpressionType.BOOLEAN:
        gen.base += 4
        ic(gen.label_counter)
        gen.label_counter += 2
        arr = gen.code if gen.target == "code" else gen.labels
        arr.append(f"\tli t0, {exp.value}\n")
        arr.append(f"\tlw t1, {gen.offset}(t0)\n")
        arr.append(f"\tbeqz t1, if_true{gen.label_counter}\n")
        arr.append(f"\tli t1, 0\n")
        arr.append(f"\tli t0, {str(gen.base)}\n")
        arr.append(f"\tsw t1, {gen.offset}(t0)\n")
        arr.append(f"\tj if_exit{gen.label_counter - 1}\n")
        arr.append(f"if_exit{gen.label_counter - 1}:\n")

        tmp = []
        tmp.append(f"if_true{gen.label_counter}:\n")
        tmp.append(f"\tli t0, {str(gen.base)}\n")
        tmp.append(f"\tli t1, 1\n")
        tmp.append(f"\tsw t1, {gen.offset}(t0)\n")
        tmp.append(f"\tj if_exit{gen.label_counter - 1}\n")
        gen.labels = tmp + gen.labels



        return Value(str(gen.base), ExpressionType.BOOLEAN, line, column)
        # return Symbol(line, column, not exp.value, ExpressionType.BOOLEAN)
    # return Symbol(line, column, ExpressionType.NULL.name, ExpressionType.NULL)
    return Value("x0", ExpressionType.NULL, line, column)
