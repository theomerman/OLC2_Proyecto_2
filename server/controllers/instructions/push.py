from icecream import ic
import numpy as np
from controllers.interfaces.instruction import Instruction
from controllers.interfaces.expression import Expression
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.error import Error
from controllers.environment.types import ExpressionType
from controllers.expressions.primitive import Primitive
from controllers.environment.generator import Generator

class Push(Instruction):
    def __init__(self, id: str, value: Expression, line, column):
        self.id = id
        self.value = value
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment, gen: Generator):
        arr = env.get_variable(ast, self.id)
        if arr.type == ExpressionType.NULL:
            ast.add_error(Error(
                f"La variable {self.id} no ha sido inicializada", 
                env.id,
                "Semantico",
                self.line,
                self.column))
            return
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
            return
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
        #     return
        if arr.array_type != self.value.run(ast, env, gen).type:
            ast.add_error(
                Error(
                    f"No se puede asignar un tipo {self.value.run(ast, env, gen)} a un vector de tipo {arr.array_type}",
                    env.id,
                    "Semantico",
                    self.line,
                    self.column
                )
            )

        new_value = self.value.run(ast, env, gen).value

        gen.label_queue[0].append(f"\t# Inicio de la instruccion push\n")
        gen.label_queue[0].append(f"\tlw t0, {self.id}\n")
        gen.label_queue[0].append(f"\tli t1, 4\n")
        gen.label_queue[0].append(f"\tmul t1, t0, t1\n")
        gen.label_queue[0].append(f"\taddi t1, t1, 4\n")



        gen.label_queue[0].append(f"\tla t0, {self.id}\n")
        gen.label_queue[0].append(f"\tadd t0, t0, t1\n")

        gen.label_queue[0].append(f"\tli t1, {new_value}\n")
        gen.label_queue[0].append(f"\tlw t1, {gen.get_offset()}(t1)\n")
        gen.label_queue[0].append(f"\tsw t1, 0(t0)\n")


        gen.label_queue[0].append(f"\tla t0, {self.id}\n")
        gen.label_queue[0].append(f"\tlw t1, {self.id}\n")
        gen.label_queue[0].append(f"\taddi t1, t1, 1\n")
        gen.label_queue[0].append(f"\tsw t1, 0(t0)\n")




        # gen.label_queue[0].append(f"\tmv a0, t0\n")
        # gen.label_queue[0].append(f"\tli a7, 1\n")
        # gen.label_queue[0].append(f"\tecall\n")




        # new_value = Primitive(self.value.run(ast, env).value,self.value.run(ast,env).type,self.line, self.column)
        # arr.value.append(new_value)



