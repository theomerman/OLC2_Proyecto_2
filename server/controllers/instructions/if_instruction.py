from icecream import ic
from controllers.interfaces.instruction import Instruction
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.error import Error
from controllers.environment.types import ExpressionType
from controllers.environment.generator import Generator
from controllers.expressions.primitive import Primitive
from controllers.expressions.access import Access

class If(Instruction):
    def __init__(self, ctx: list, line, column):
        self.ctx = ctx
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment, gen: Generator):
        if_env = Environment(env, "if")


        gen.label_counter += 1
        exit_label = int(gen.label_counter)
        for arr in self.ctx:
            if isinstance(arr[0],Primitive):
                if arr[0].type != ExpressionType.BOOLEAN:
                    ast.add_error(Error(
                        "La condición del if debe ser de tipo booleano",
                        env.id,
                        "Semántico",
                        self.line,
                        self.column
                    ))
                    return

            if isinstance(arr[0],Access):
                if arr[0].run(ast, if_env, gen).type != ExpressionType.BOOLEAN:
                    ast.add_error(Error(
                        "La condición del if debe ser de tipo booleano",
                        env.id,
                        "Semántico",
                        self.line,
                        self.column
                    ))
                    return
            # if arr[0].run(ast, if_env).type != ExpressionType.BOOLEAN:
            #     ast.add_error(Error(
            #         "La condición del if debe ser de tipo booleano",
            #         env.id,
            #         "Semántico",
            #         self.line,
            #         self.column
            #     ))
            #     return

            gen.label_queue.insert(0, [])

            tmp_arr = gen.code if gen.target == "code" else gen.labels
            tmp_arr.append(f"\t# Inicio del if\n")
            tmp_arr.append(f"\tli t0, {str(arr[0].run(ast, if_env, gen).value)}\n")
            tmp_arr.append(f"\tlw t0, {gen.offset}(t0)\n")

            gen.label_counter += 1
            tmp_arr.append(f"\tbgtz t0, if_true{gen.label_counter}\n")

            # gen.labels.append(f"if_true{gen.label_counter}:\n")
            gen.label_queue[0][0].append(f"if_true{gen.label_counter}\n")

            gen.target = "labels"
            for inst in arr[1]:
                inst.run(ast, if_env, gen)
            # gen.labels.append(f"\tj if_end{exit_label}\n")
            gen.label_queue[0][0].append(f"if_end{exit_label}\n")
            gen.target = "code"

            

            # if arr[0].run(ast, if_env, gen).value == True:
            #     for inst in arr[1]:
            #         inst.run(ast, if_env, gen)
            #     break
        tmp_arr = gen.code if gen.target == "code" else gen.labels
        tmp_arr.append(f"\t# Fin del if\n")
        tmp_arr.append(f"if_end{exit_label}:\n")

        ast.symbol_table.append([if_env.id,if_env.table])
