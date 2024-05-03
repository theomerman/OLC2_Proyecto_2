from icecream import ic
from controllers.interfaces.instruction import Instruction
from controllers.environment.types import ExpressionType
from controllers.environment.ast import Ast
from controllers.interfaces.expression import Expression
from controllers.environment.error import Error
from controllers.environment.symbol import Symbol
from controllers.environment.environment import Environment
from controllers.environment.generator import Generator
from controllers.environment.value import Value
from controllers.expressions.primitive import Primitive
# from icecream import ic

class Declaration(Instruction):
    def __init__(self, id: str, exp: Expression, type: ExpressionType, line, column, constant=False) -> None:
        self.id = id
        self.exp = exp
        self.type = type
        self.line = line
        self.column = column
        self.constant = constant

    def run(self, ast: Ast, env: Environment, gen: Generator):

        if self.exp is None:
            set_variable_no_exp(ast, env, gen, self.id, self.type,
                                self.line, self.column)
            return
        if self.type is None:
            set_variable_no_type(
                ast, env, gen, self.id, self.exp, self.line, self.column, self.constant)
            return
        else:
            set_variable(ast, env, gen, self.id, self.exp,
                         self.type, self.line, self.column, self.constant)
            return


def set_variable_no_exp(ast: Ast, env: Environment,gen: Generator, id: str, type: ExpressionType, line, column):
    if id in env.table:
        ast.add_error(Error(
            f"La variable \"{id}\" ya existe",
            env.id,
            "Semantico",
            line,
            column
        )
        )
        return
    if type is ExpressionType.NUMBER:
        # env.table[id] = Symbol(line, column, 0, type)
        gen.base =+ 4
        # gen.add_li("t0", str(gen.base))
        # gen.add_li("t1", str(0))
        # gen.add_sw("t1", gen.offset, "t0")
        arr = gen.label_queue[0]
        arr.append(f"\tli t0, {gen.get_base()}\n")
        arr.append(f"\tli t1, 0\n")
        arr.append(f"\tsw t1, {gen.get_offset()}(t0)\n")
        tmp = Value(str(gen.base), ExpressionType.NUMBER, line, column)
        tmp.setGeneric(0)
        env.table[id] = tmp
    elif type is ExpressionType.STRING:
    #     env.table[id] = Symbol(line, column, "", type)
        gen.add_data(str(""))
        tmp = Value("str" + str(gen.string_counter - 1), ExpressionType.STRING, line, column)
        tmp.setGeneric("")
        env.table[id] = tmp

    elif type is ExpressionType.BOOLEAN:
    #     env.table[id] = Symbol(line, column, False, type)
        gen.base =+ 4
        # gen.add_li("t0", str(gen.base))
        # gen.add_li("t1", str(0))
        # gen.add_sw("t1", gen.offset, "t0")
        arr = gen.label_queue[0]
        arr.append(f"\tli t0, {gen.get_base()}\n")
        arr.append(f"\tli t1, 0\n")
        arr.append(f"\tsw t1, {gen.get_offset()}(t0)\n")
        tmp = Value(str(gen.base), ExpressionType.BOOLEAN, line, column)
        tmp.setGeneric(0)
        env.table[id] = tmp

    elif type is ExpressionType.CHAR:
    #     env.table[id] = Symbol(line, column, "", type)
        gen.add_data(str(""))
        tmp = Value("str" + str(gen.string_counter - 1), ExpressionType.CHAR, line, column)
        tmp.setGeneric("")
        env.table[id] = tmp
    elif type is ExpressionType.FLOAT:
    #     env.table[id] = Symbol(line, column, 0.0, type)
        gen.float_counter += 1
        gen.data.append(f"fl{gen.float_counter}: .float 0.0\n")
        tmp = Value("fl" + str(gen.float_counter), ExpressionType.FLOAT, line, column)
        tmp.setGeneric("0.0")
        env.table[id] = tmp


def set_variable_no_type(ast: Ast, env: Environment, gen: Generator, id: str, exp: Expression, line, column, constant):
    if id in env.table:
        ast.add_error(Error(
            f"La variable \"{id}\" ya existe",
            env.id,
            "Semantico",
            line,
            column
        )
        )
        return
    env.table[id] = exp.run(ast, env, gen)
    if constant:
        env.table[id].constant = True


def set_variable(ast: Ast, env: Environment, gen:Generator, id: str, exp: Expression, type: ExpressionType, line, column, constant):
    if id in env.table:
        ast.add_error(Error(
            f"La variable \"{id}\" ya existe",
            env.id,
            "Semantico",
            line,
            column
        )
        )
        return
    if isinstance(exp, Primitive):
        if exp.type != type:
            ast.add_error(Error(
                f"No se puede asignar un tipo \"{exp.type.name}\" a un \"{type.name}\"",
                env.id,
                "Semantico",
                line,
                column
            )
            )
            return
    # elif exp.run(ast, env, gen).type != type:
    #     ast.add_error(Error(
    #         f"No se puede asignar un tipo \"{exp.run(ast, env, gen).type.name}\" a un \"{type.name}\"",
    #         env.id,
    #         "Semantico",
    #         line,
    #         column
    #     )
    #     )
    #     return
    env.table[id] = exp.run(ast, env, gen)
    if constant:
        env.table[id].constant = True
    return
