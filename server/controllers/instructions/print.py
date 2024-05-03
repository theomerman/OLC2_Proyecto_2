from controllers.interfaces.instruction import Instruction
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
# from controllers.environment.symbol import Symbol
from controllers.environment.types import ExpressionType
from controllers.environment.generator import Generator
from controllers.environment.value import Value
from icecream import ic

string = ""


class Print(Instruction):
    def __init__(self, exps: list, line, column):
        self.exps = exps
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment, gen: Generator):
        global string
        console = ""
        for exp in self.exps:
            value = exp.run(ast, env, gen)

            # ic(value.value)
            if isinstance(value, Value):
                if value.type == ExpressionType.ARRAY:
                    string = ""
                    array_to_string(ast, env, gen, value.value)
                    console += string
                else:
                    if value.type == ExpressionType.NUMBER:
                        # gen.add_print(value.value)
                        arr = gen.label_queue[0]
                        arr.append(f"\tli t0, {str(value.value)}\n")
                        arr.append(f"\tlw a0, {gen.get_offset()}(t0)\n")
                        arr.append(f"\tli a7, 1\n")
                        arr.append(f"\tecall\n")




                    elif value.type == ExpressionType.STRING:
                        # gen.add_print_string(value.value)
                        arr = gen.label_queue[0]
                        arr.append(f"\tla a0, {str(value.value)}\n")
                        arr.append(f"\tli a7, 4\n")
                        arr.append(f"\tecall\n")

                    elif value.type == ExpressionType.FLOAT:
                        gen.add_print_float(value.value)


                    elif value.type == ExpressionType.BOOLEAN:
                        arr = gen.label_queue[0]
                        # arr.append(f"\tli t0, {str(value.value)}\n")
                        # arr.append(f"\tlw a0, {gen.get_offset()}(t0)\n")
                        # arr.append(f"\tli a7, 1\n")
                        # arr.append(f"\tecall\n")

                        gen.label_counter += 1
                        start_print = gen.get_label_counter()
                        gen.label_counter += 1
                        true_print = gen.get_label_counter()
                        gen.label_counter += 1
                        end_print = gen.get_label_counter()

                        gen.label_queue[0].append(f"\tj print{start_print}\n")
                        gen.code = gen.code + gen.label_queue.pop(0)


                        gen.label_queue.insert(0, [])
                        gen.label_queue[0].append(f"print{start_print}:\n")
                        gen.label_queue[0].append(f"\tli t0, {str(value.value)}\n")
                        gen.label_queue[0].append(f"\tlw t0, {gen.get_offset()}(t0)\n")
                        gen.label_queue[0].append(f"\tbgtz t0, print_true{true_print}\n")
                        gen.label_queue[0].append(f"\tla a0, false\n")
                        gen.label_queue[0].append(f"\tli a7, 4\n")
                        gen.label_queue[0].append(f"\tecall\n")
                        gen.label_queue[0].append(f"\tj print_end{end_print}\n")

                        gen.code = gen.code + gen.label_queue.pop(0)

                        gen.label_queue.insert(0, [])
                        gen.label_queue[0].append(f"print_true{true_print}:\n")
                        gen.label_queue[0].append(f"\tla a0, true\n")
                        gen.label_queue[0].append(f"\tli a7, 4\n")
                        gen.label_queue[0].append(f"\tecall\n")
                        gen.label_queue[0].append(f"\tj print_end{end_print}\n")

                        gen.code = gen.code + gen.label_queue.pop(0)


                        gen.label_queue.insert(0, [])
                        gen.label_queue[0].append(f"print_end{end_print}:\n")
                        

                        
                    elif value.type == ExpressionType.CHAR:
                        # gen.add_print_string(value.value)
                        arr = gen.label_queue[0]
                        arr.append(f"\tla a0, {value.value}\n")
                        arr.append(f"\tli a7, 4\n")
                        arr.append(f"\tecall\n")
                    elif value.type == ExpressionType.NULL:
                        arr = gen.label_queue[0]
                        arr.append(f"\tla a0, null\n")
                        arr.append(f"\tli a7, 4\n")
                        arr.append(f"\tecall\n")


                    console += str(value.value) + " "

            else:
                if value.run(ast, env, gen).type == ExpressionType.ARRAY:
                    string = ""
                    array_to_string(ast, env, gen, value.value)
                    string = ""
                else:
                    if value.type == ExpressionType.NUMBER:
                        # gen.add_print(value.value)
                        arr = gen.label_queue[0]
                        arr.append(f"\tli t0, {str(value.value)}\n")
                        arr.append(f"\tlw a0, {gen.get_offset()}(t0)\n")
                        arr.append(f"\tli a7, 1\n")
                        arr.append(f"\tecall\n")




                    elif value.type == ExpressionType.STRING:
                        # gen.add_print_string(value.value)
                        arr = gen.label_queue[0]
                        arr.append(f"\tla a0, {str(value.value)}\n")
                        arr.append(f"\tli a7, 4\n")
                        arr.append(f"\tecall\n")

                    elif value.type == ExpressionType.FLOAT:
                        gen.add_print_float(value.value)


                    elif value.type == ExpressionType.BOOLEAN:
                        # gen.add_print(value.value)
                        arr = gen.label_queue[0]
                        arr.append(f"\tli t0, {str(value.value)}\n")
                        arr.append(f"\tlw a0, {gen.get_offset()}(t0)\n")
                        arr.append(f"\tli a7, 1\n")
                        arr.append(f"\tecall\n")

                    elif value.type == ExpressionType.CHAR:
                        # gen.add_print_string(value.value)
                        arr = gen.label_queue[0]
                        arr.append(f"\tla a0, {value.value}\n")
                        arr.append(f"\tli a7, 4\n")
                        arr.append(f"\tecall\n")
                    console += str(value.run(ast, env, gen).value) + " "

            arr = gen.label_queue[0]
            arr.append(f"\tla a0, space\n")
            arr.append(f"\tli a7, 4\n")
            arr.append(f"\tecall\n")

        # gen.add_la("a0", "next_line")
        # gen.add_li("a7", 4)
        # gen.add_ecall()
        arr = gen.label_queue[0]
        arr.append(f"\tla a0, next_line\n")
        arr.append(f"\tli a7, 4\n")
        arr.append(f"\tecall\n")

        ast.set_console(console)


def array_to_string(ast: Ast, env: Environment,gen: Generator, head: str):

    # head contains the base address of the array, in position 0 we have the length of the array
    gen.label_queue[0].append(f"\t# entrando en print\n")
    gen.label_counter += 1
    start_print = gen.get_label_counter()
    gen.label_counter += 1
    true_print = gen.get_label_counter()
    gen.label_counter += 1
    end_print = gen.get_label_counter()

    gen.label_queue[0].append(f"\tla a0, bracketL\n")
    gen.label_queue[0].append(f"\tli a7, 4\n")
    gen.label_queue[0].append(f"\tecall\n")

    gen.label_queue[0].append(f"\tla t3, {head}\n")
    gen.label_queue[0].append(f"\tlw t4, 0(t3)\n")
    gen.label_queue[0].append(f"\tli t5, 0\n")
    gen.label_queue[0].append(f"\tj print{start_print}\n")

    gen.label_queue[0].append(f"print{start_print}:\n")
    gen.label_queue[0].append(f"\tbgt t4, t5, print_true{true_print}\n")
    gen.label_queue[0].append(f"\tj exit{end_print}\n")


    gen.label_queue[0].append(f"print_true{true_print}:\n")
    gen.label_queue[0].append(f"\taddi t5, t5, 1\n")
    gen.label_queue[0].append(f"\taddi t3, t3, 4\n")
    gen.label_queue[0].append(f"\tlw a0, 0(t3)\n")


    gen.label_queue[0].append(f"\tli a7, 1\n")
    gen.label_queue[0].append(f"\tecall\n")


    gen.label_queue[0].append(f"\tla a0, comma\n")
    gen.label_queue[0].append(f"\tli a7, 4\n")
    gen.label_queue[0].append(f"\tecall\n")


    gen.label_queue[0].append(f"\tj print{start_print}\n")

    gen.label_queue[0].append(f"exit{end_print}:\n")

    gen.label_queue[0].append(f"\tla a0, bracketR\n")
    gen.label_queue[0].append(f"\tli a7, 4\n")
    gen.label_queue[0].append(f"\tecall\n")


    # gen.label_queue[0].append(f"\tli t1, 4\n")






    # gen.label_queue[0].append(f"\tmv a0, t4\n")
    # gen.label_queue[0].append(f"\tli a7, 1\n")
    # gen.label_queue[0].append(f"\tecall\n")
















