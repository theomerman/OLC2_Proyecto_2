from icecream import ic
from controllers.interfaces.instruction import Instruction
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.instructions.break_statement import BreakException
from controllers.instructions.continue_statement import ContinueException
from controllers.environment.generator import Generator


class While(Instruction):
    def __init__(self, condition, instructions, line, column):
        self.condition = condition
        self.instructions = instructions
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment, gen: Generator):


        gen.label_counter += 1
        begin_label = int(gen.label_counter)

        gen.label_counter += 1
        if_true_label = int(gen.label_counter)

        gen.label_counter += 1
        exit_label = int(gen.label_counter)



        gen.break_stack.insert(0, begin_label)
        gen.break_stack.insert(0, exit_label)


        gen.label_queue[0].append(f"\tj begin_loop{begin_label}\n")
        gen.code = gen.code + gen.label_queue[0]
        gen.label_queue = gen.label_queue[1:]


        gen.label_queue.insert(0, [])
        gen.label_queue[0].append(f"begin_loop{begin_label}:\n")
        tmp_value = self.condition.run(ast, env, gen)
        gen.label_queue[0].append(f"\tli t0, {tmp_value.value}\n")
        gen.label_queue[0].append(f"\tlw t0, {gen.get_offset()}(t0)\n")
        gen.label_queue[0].append(f"\tbgtz t0, if_true{if_true_label}\n")
        gen.label_queue[0].append(f"\tj exit{exit_label}\n")


        gen.code = gen.code + gen.label_queue[0]
        gen.label_queue = gen.label_queue[1:]

        gen.label_queue.insert(0, [])
        gen.label_queue[0].append(f"if_true{if_true_label}:\n")


        # for instruction in self.instructions:
        #     instruction.run(ast, env, gen)

        while_env = Environment(env, "while")
        for instruction in self.instructions:
            instruction.run(ast, while_env, gen)


        # while self.condition.run(ast, env, gen).value:
        #     while_env = Environment(env, "while")
        #     try:
        #         for instruction in self.instructions:
        #             instruction.run(ast, while_env, gen)
        #     except BreakException:
        #         break
        #     except ContinueException:
        #         continue

        gen.label_queue[0].append(f"\tj begin_loop{begin_label}\n")
        gen.code = gen.code + gen.label_queue[0]
        gen.label_queue = gen.label_queue[1:]

        gen.label_queue.insert(0, [])
        gen.label_queue[0].append(f"exit{exit_label}:\n")
        gen.break_stack.pop(0)
        gen.break_stack.pop(0)
        # gen.label_queue[0].append(f"\taddi sp, sp, 4\n")
