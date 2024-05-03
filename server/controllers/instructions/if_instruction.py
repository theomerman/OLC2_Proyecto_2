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


        gen.label_counter += 1
        gen.label_queue[0].append(f"\tj begin_if{gen.get_label_counter()}\n")
        gen.code = gen.code + gen.label_queue[0]
        gen.label_queue = gen.label_queue[1:]


        gen.label_queue.insert(0, [])
        gen.label_queue[0].append(f"begin_if{gen.get_label_counter()}:\n")


        counter_tmp = int(gen.label_counter)
        gen.label_counter += len(self.ctx)



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



            counter_tmp += 1
            tmp_value = arr[0].run(ast, if_env, gen)
            gen.label_queue[0].append(f"\tli t0, {tmp_value.value}\n")
            gen.label_queue[0].append(f"\tlw t0, {gen.get_offset()}(t0)\n")
            gen.label_queue[0].append(f"\tbgtz t0, if_true{counter_tmp}\n")


        gen.label_queue[0].append(f"\tj end_if{exit_label}\n")

        gen.code = gen.code + gen.label_queue[0]
        gen.label_queue = gen.label_queue[1:]

        counter_tmp = counter_tmp - len(self.ctx)


        for arr in self.ctx:
            gen.label_queue.insert(0, [])
            counter_tmp += 1
            gen.label_queue[0].append(f"if_true{counter_tmp}:\n")
            for inst in arr[1]:
                inst.run(ast, if_env, gen)
            gen.label_queue[0].append(f"\tj end_if{exit_label}\n")
            gen.code = gen.code + gen.label_queue[0]
            gen.label_queue = gen.label_queue[1:]

        gen.label_queue.insert(0, [])
        gen.label_queue[0].append(f"end_if{exit_label}:\n")
        


####################
            # gen.label_counter += 1
            # gen.label_queue.insert(0, [])
            # gen.label_queue[0].append(f"# Inicio del If")
            # gen.label_queue[0].append(f"if{gen.get_label_counter()}:\n")
            # gen.label_queue[0].append(f"\tli t0, {str(arr[0].run(ast, if_env, gen).value)}\n")
            # gen.label_queue[0].append(f"\tlw t0, {gen.get_offset()}(t0)\n")
            # gen.label_queue.insert(0, [])
####################


            # tmp_arr = gen.code if gen.target == "code" else gen.labels
            # tmp_arr.append(f"\t# Inicio del if\n")
            # tmp_arr.append(f"\tli t0, {str(arr[0].run(ast, if_env, gen).value)}\n")
            # tmp_arr.append(f"\tlw t0, {gen.offset}(t0)\n")



####################
            # gen.label_counter += 1
            # gen.label_queue[0].append(f"\tbgtz t0, if_true{gen.label_counter}\n")
####################


            # tmp_arr.append(f"\tbgtz t0, if_true{gen.label_counter}\n")

            # gen.labels.append(f"if_true{gen.label_counter}:\n")
####################
            # gen.label_queue[0][0].append(f"if_true{gen.label_counter}\n")
            #
            # for inst in arr[1]:
            #     inst.run(ast, if_env, gen)
####################

            # gen.labels.append(f"\tj if_end{exit_label}\n")

####################
            # gen.label_queue[0][0].append(f"if_end{exit_label}\n")
            # gen.target = "code"
####################


            # if arr[0].run(ast, if_env, gen).value == True:
            #     for inst in arr[1]:
            #         inst.run(ast, if_env, gen)
            #     break

####################

        # tmp_arr = gen.code if gen.target == "code" else gen.labels
        # tmp_arr.append(f"\t# Fin del if\n")
        # tmp_arr.append(f"if_end{exit_label}:\n")
####################
        ast.symbol_table.append([if_env.id,if_env.table])
