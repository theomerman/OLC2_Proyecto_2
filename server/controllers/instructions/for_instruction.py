from icecream import ic
from controllers.interfaces.instruction import Instruction
from controllers.interfaces.expression import Expression
from controllers.environment.ast import Ast
from controllers.environment.environment import Environment
from controllers.environment.symbol import Symbol
from controllers.environment.types import ExpressionType
from controllers.instructions.declaration import Declaration
from controllers.instructions.break_statement import BreakException
from controllers.instructions.continue_statement import ContinueException
from controllers.environment.generator import Generator


class For(Instruction):
    def __init__(self, declaration: Declaration, exp: Expression, modification: list, block: list, line, column):
        self.declaration = declaration
        self.exp = exp
        self.modification = modification
        self.block = block
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment, gen:Generator):
        for_env = Environment(env, "for")

        gen.label_counter += 1
        begin_for =  int(gen.label_counter)
        gen.label_counter += 1
        for_condition = int(gen.label_counter)
        gen.label_counter += 1
        if_true = int(gen.label_counter)
        gen.label_counter += 1
        end_for = int(gen.label_counter)


        gen.break_stack.insert(0, begin_for)
        gen.break_stack.insert(0, end_for)

        gen.label_queue[0].append(f"\t# Inicio de for\n")
        gen.label_queue[0].append(f"\tj begin_loop{begin_for}\n")

        gen.code = gen.code + gen.label_queue.pop(0)# gen.label_queue[0]
        # gen.label_queue = gen.label_queue[1:]

        gen.label_queue.insert(0, [])
        gen.label_queue[0].append(f"begin_loop{begin_for}:\n")
        gen.label_queue[0].append(f"\t# Declaracion de variable\n")
        self.declaration.run(ast, for_env, gen)
        gen.label_queue[0].append(f"\tj for_condition{for_condition}\n")

        gen.code = gen.code + gen.label_queue.pop(0)# gen.label_queue[0]


        gen.label_queue.insert(0, [])
        gen.label_queue[0].append(f"for_condition{for_condition}:\n")
        gen.label_queue[0].append(f"\t# Condicion de for\n")
        tmp_value = self.exp.run(ast, for_env, gen)
        ic(tmp_value)
        gen.label_queue[0].append(f"\tli t0, {tmp_value.value}\n")
        gen.label_queue[0].append(f"\tlw t0, {gen.get_offset()}(t0)\n")
        gen.label_queue[0].append(f"\tbgtz t0, if_true{if_true}\n")
        gen.label_queue[0].append(f"\tj exit{end_for}\n")

        gen.code = gen.code + gen.label_queue.pop(0)# gen.label_queue[0]

        gen.label_queue.insert(0, [])
        gen.label_queue[0].append(f"if_true{if_true}:\n")
        gen.label_queue[0].append(f"\t# Bloque de for\n")


        for_env2 = Environment(for_env, "for")
        for instruction in self.block:
            instruction.run(ast, for_env2, gen)

        gen.label_queue[0].append(f"\t# Modificacion de variable\n")

        if self.modification[1] == "++":
            self.increment(for_env, gen, self.modification[0])
        elif self.modification[1] == "--":
            self.decrement(for_env, gen, self.modification[0])
        gen.label_queue[0].append(f"\tj for_condition{for_condition}\n")

        gen.code = gen.code + gen.label_queue.pop(0)# gen.label_queue[0]


        gen.label_queue.insert(0, [])
        gen.label_queue[0].append(f"exit{end_for}:\n")

        gen.break_stack.pop(0)
        gen.break_stack.pop(0)





        # self.declaration.run(ast, for_env, gen)
        # for_env.table[self.modification[0]] = Symbol(
        #         for_env.table[self.modification[0]].line,
        #         for_env.table[self.modification[0]].col,
        #         for_env.table[self.modification[0]].value,
        #         for_env.table[self.modification[0]].type,
        # )
        # while True:
        #     for_env2 = Environment(for_env, "for")
        #     if not self.exp.run(ast, for_env, gen).value:
        #         break
        #     for instruction in self.block:
        #         instruction.run(ast, for_env2, gen)
        #     for_env.table[self.modification[0]].value = for_env.table[self.modification[0]].value + 1

        ast.symbol_table.append([env.id, for_env.table])





    def increment(self, env: Environment, gen: Generator, id):

        gen.label_queue[0].append(f"\tli t0, {env.table[id].value}\n")
        gen.label_queue[0].append(f"\tlw t1, {gen.get_offset()}(t0)\n")
        gen.label_queue[0].append(f"\taddi t1, t1, 1\n")
        gen.label_queue[0].append(f"\tsw t1, {gen.get_offset()}(t0)\n")


    def decrement(self, env: Environment, gen: Generator, id):
        gen.label_queue[0].append(f"\tli t0, {env.table[id].value}\n")
        gen.label_queue[0].append(f"\tlw t1, {gen.get_offset()}(t0)\n")
        gen.label_queue[0].append(f"\tsubi t1, t1, 1\n")
        gen.label_queue[0].append(f"\tsw t1, {gen.get_offset()}(t0)\n")

