from icecream import ic
import numpy as np
from controllers.interfaces.expression import Expression
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.types import ExpressionType
from controllers.environment.error import Error
from controllers.expressions.primitive import Primitive
from controllers.environment.generator import Generator


class VectorFunctions(Expression):
    def __init__(self, id: str, function: str, value: Expression, line, column):
        self.id = id
        self.function = function
        self.value = value
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment, gen: Generator):
        arr = env.get_variable(ast, self.id)
        if arr.type == ExpressionType.NULL:
            ast.add_error(
                Error(
                    f"La variable {self.id} no ha sido inicializada",
                    env.id,
                    "Semantico",
                    self.line,
                    self.column
                    )
                    )
            return arr
        if arr.type != ExpressionType.ARRAY:
            ast.add_error(
                Error(
                        f"La variable {self.id} no es un vector",
                        env.id,
                        "Semantico",
                        self.line,
                        self.column
                        )
                        )
            return Primitive(ExpressionType.NULL.name, ExpressionType.NULL, self.line, self.column)
        # if np.array(arr.value).ndim != 1:
        #     ast.add_error(
        #         Error(
        #             "La variable es una Matriz",
        #             env.id,
        #             "Semantico",
        #             self.line,
        #             self.column
        #         )
        #     )
        #     return Primitive(ExpressionType.NULL.name, ExpressionType.NULL, self.line, self.column)
        if self.function == "pop":

            gen.label_queue[0].append(f"\t# Inicio de la instruccion pop\n")
            # gen.label_queue[0].append(f"\tlw t0, {arr.value}\n")
            # gen.label_queue[0].append(f"\tli t1 4\n")
            # gen.label_queue[0].append(f"\tmul t0, t0, t1\n")

            gen.label_queue[0].append(f"\tlw t0, {arr.value}\n")
            gen.label_queue[0].append(f"\tli t1, 4\n")
            gen.label_queue[0].append(f"\tmul t1, t0, t1\n")
            # gen.label_queue[0].append(f"\taddi t1, t1, 4\n")

            gen.label_queue[0].append(f"\tla t0, {arr.value}\n")
            gen.label_queue[0].append(f"\tadd t0, t0, t1\n")

            gen.base += 4
            gen.label_queue[0].append(f"\tlw t2, 0(t0)\n")
            gen.label_queue[0].append(f"\tli t3, {gen.get_base()}\n")
            gen.label_queue[0].append(f"\tsw t2, {gen.get_offset()}(t3)\n")

            gen.label_queue[0].append(f"\tli t1, 0\n")
            gen.label_queue[0].append(f"\tlw t1, {gen.get_offset()}(t1)\n")
            gen.label_queue[0].append(f"\tsw t1, 0(t0)\n")


            gen.label_queue[0].append(f"\tla t0, {self.id}\n")
            gen.label_queue[0].append(f"\tlw t1, {self.id}\n")
            gen.label_queue[0].append(f"\taddi t1, t1, -1\n")
            gen.label_queue[0].append(f"\tsw t1, 0(t0)\n")

            return Primitive(gen.get_base(), ExpressionType.NUMBER, self.line, self.column)
        elif self.function == "indexOf":
            index = 0

            source = self.value.run(ast, env, gen)
            ic(source.value)
            ic(gen.get_base())

            gen.label_counter += 1
            begin = gen.label_counter
            gen.label_counter += 1
            index_true = gen.label_counter
            gen.label_counter += 1
            return_index = gen.label_counter
            gen.label_counter += 1
            end = gen.label_counter


            

            # cargar el valor a buscar: t3 = value
            gen.label_queue[0].append(f"\tli t3, {source.value}\n")
            gen.label_queue[0].append(f"\tlw t3, {gen.get_offset()}(t3)\n")

            # carga el contador del indice en sp: sp = index
            gen.label_queue[0].append(f"\taddi sp, sp, -4\n")
            gen.label_queue[0].append(f"\tli t0, 0\n")
            gen.label_queue[0].append(f"\tsw t0, 0(sp)\n")

            # cargar el tamaño del vector en t1: t4 = size
            gen.label_queue[0].append(f"\tlw t4, {arr.value}\n")
            # gen.label_queue[0].append(f"\tlw t4, {gen.get_offset()}(t4)\n")

            gen.label_queue[0].append(f"\tj begin_indexof{begin}\n")



            gen.label_queue[0].append(f"\t# Inicio del ciclo\n")
            gen.label_queue[0].append(f"begin_indexof{begin}:\n")
            gen.label_queue[0].append(f"\t# Cargar el contador del indice en t0\n")
            gen.label_queue[0].append(f"\tlw t0, 0(sp)\n")
            gen.label_queue[0].append(f"\tbgt t4, t0, index_true{index_true}\n")
            gen.base += 4
            gen.label_queue[0].append(f"\tli t0, -1\n")
            gen.label_queue[0].append(f"\tli t1, {gen.get_base()}\n")
            gen.label_queue[0].append(f"\tsw t0, {gen.get_offset()}(t1)\n")
            gen.label_queue[0].append(f"\tj end_indexof{end}\n")

            gen.label_queue[0].append(f"index_true{index_true}:\n")
            gen.label_queue[0].append(f"\tlw t0, 0(sp)\n")
            gen.label_queue[0].append(f"\taddi t1, t0, 1\n")
            gen.label_queue[0].append(f"\tsw t1, 0(sp)\n")

            # gen.label_queue[0].append(f"\tlw t0, \n")
            gen.label_queue[0].append(f"\tli t1, 4\n")
            gen.label_queue[0].append(f"\tmul t0, t0, t1\n")
            gen.label_queue[0].append(f"\taddi t0, t0, 4\n")

            gen.label_queue[0].append(f"\tla t1, {arr.value}\n")
            gen.label_queue[0].append(f"\tadd t0, t0, t1\n")
            gen.label_queue[0].append(f"\tlw t0, 0(t0)\n")
            gen.label_queue[0].append(f"\tbeq t0, t3, return_index{end}\n")
            gen.label_queue[0].append(f"\tj begin_indexof{begin}\n")


            # return_index
            gen.label_queue[0].append(f"return_index{end}:\n")
            gen.label_queue[0].append(f"\tlw t0, 0(sp)\n")
            gen.label_queue[0].append(f"\taddi t0, t0, -1\n")
            gen.label_queue[0].append(f"\tli t1, {gen.get_base()}\n")
            gen.label_queue[0].append(f"\tsw t0, {gen.get_offset()}(t1)\n")
            gen.label_queue[0].append(f"\tj end_indexof{end}\n")




            gen.label_queue[0].append(f"end_indexof{end}:\n")
            gen.label_queue[0].append(f"\taddi sp, sp, 4\n")


            # gen.label_queue[0].append(f"\tmv a0, t0\n")
            # gen.label_queue[0].append(f"\tli a7, 1\n")
            # gen.label_queue[0].append(f"\tecall\n")

            # for item in arr.value:
            #     if item.run(ast, env, gen).value == self.value.run(ast, env, gen).value:
            #         return Primitive(index, ExpressionType.NUMBER, self.line, self.column)
            #     index += 1
            return Primitive(gen.get_base(), ExpressionType.NUMBER, self.line, self.column)
        elif self.function == "join":
            result = ""
            for item in arr.value:
                if result == "":
                    result += str(item.run(ast, env).value)
                else:
                    result += "," + str(item.run(ast, env).value)
            return Primitive(result, ExpressionType.STRING, self.line, self.column)
        elif self.function == "length":
            ic(arr.value)
            gen.base += 4

            gen.label_queue[0].append(f"\tlw t0, {arr.value}\n")
            gen.label_queue[0].append(f"\tli t1, {gen.get_base()}\n")
            gen.label_queue[0].append(f"\tsw t0, {gen.get_offset()}(t1)\n")
            return Primitive(gen.get_base(), ExpressionType.NUMBER, self.line, self.column)
