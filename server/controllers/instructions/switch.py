from icecream import ic
from controllers.interfaces.instruction import Instruction
from controllers.interfaces.expression import Expression
from controllers.environment.environment import Environment
from controllers.instructions.break_statement import BreakException
from controllers.environment.ast import Ast
from controllers.environment.error import Error
from controllers.environment.generator import Generator


class Switch(Instruction):
    def __init__(self, exp: Expression, cases: list, line, column):
        self.exp = exp
        self.cases = cases
        self.line = line
        self.column = column

    def run(self, ast: Ast, env: Environment, gen:Generator):
        exp = self.exp.run(ast, env, gen).value

        default_case = []
        for case in self.cases:
            if case[0] is None:
                default_case.append(case[1])
        if len(default_case) > 1:
            ast.add_error(Error(
                "No puede haber mas de un caso default",
                env.id,
                "Semantico",
                self.line,
                self.column
            ))
            return

        gen.label_counter += 1
        begin_switch = gen.get_label_counter()
        gen.label_counter += 1
        end_switch = gen.get_label_counter()
        gen.break_stack.insert(0, end_switch)

        cases_counter = int(gen.label_counter)
        gen.label_counter += len(self.cases)

        gen.label_queue[0].append(f"\tj begin_switch{begin_switch}\n")
        gen.code = gen.code + gen.label_queue.pop(0)

        gen.label_queue.insert(0,[])
        gen.label_queue[0].append(f"begin_switch{begin_switch}:\n")


        for _ in self.cases:
            cases_counter += 1
            gen.label_queue[0].append(f"\tjal case{cases_counter}\n")

        gen.label_queue[0].append(f"\tj exit{end_switch}\n")
        gen.code = gen.code + gen.label_queue.pop(0)


        cases_counter = cases_counter - len(self.cases)


        for case in self.cases:
            if case[0] is None:
                continue
            gen.label_queue.insert(0,[])
            cases_counter += 1
            gen.label_queue[0].append(f"case{cases_counter}:\n")
            tmp_value = case[0].run(ast, env, gen)
            gen.label_queue[0].append(f"\tli t0, {tmp_value.value}\n")
            gen.label_queue[0].append(f"\tlw t0, {gen.get_offset()}(t0)\n")
            gen.label_queue[0].append(f"\tli t1, {exp}\n")
            gen.label_queue[0].append(f"\tlw t1, {gen.get_offset()}(t1)\n")
            gen.label_queue[0].append(f"\tbeq t0, t1, case{cases_counter}_true\n")
            gen.label_queue[0].append(f"\tjalr ra\n")

            gen.code = gen.code + gen.label_queue.pop(0)


            gen.label_queue.insert(0,[])
            gen.label_queue[0].append(f"case{cases_counter}_true:\n")
            switch_env = Environment(env, "switch")
            for inst in case[1]:
                inst.run(ast, switch_env, gen)
            gen.label_queue[0].append(f"\tjalr ra\n")
            gen.code = gen.code + gen.label_queue.pop(0)


        cases_counter += 1
        for default in default_case:
            gen.label_queue.insert(0,[])
            gen.label_queue[0].append(f"case{cases_counter}:\n")
            switch_env = Environment(env, "switch")
            for inst in default:
                inst.run(ast, switch_env, gen)
            gen.label_queue[0].append(f"\tjalr ra\n")
            gen.code = gen.code + gen.label_queue.pop(0)
            





        gen.label_queue.insert(0,[])
        gen.label_queue[0].append(f"exit{end_switch}:\n")
        gen.break_stack.pop(0)



        # for case in self.cases:
        #     cases_counter += 1
        #     if case[0] is None:
        #         continue
        #     gen.label_queue.insert(0,[])
        #     gen.label_queue[0].append(f"case{cases_counter}:\n")
        #
        #     gen.label_queue[0].append(f"\tli t0, {exp}\n")
        #     gen.label_queue[0].append(f"\tlw t0, {gen.get_offset()}(t0)\n")
        #
        #     tmp_value = case[0].run(ast, env, gen)
        #     ic(tmp_value)
        #
        #     gen.label_queue[0].append(f"\tli t1, {tmp_value.value}\n")
        #     gen.label_queue[0].append(f"\tlw t1, {gen.get_offset()}(t1)\n")
        #     gen.label_queue[0].append(f"\tbeq t0, t1, case{cases_counter}_true\n")
        #     gen.label_queue[0].append(f"\tjalr ra\n")
        #
        #     gen.code = gen.code + gen.label_queue.pop(0)
        #
        #     gen.label_queue.insert(0,[])
        #     gen.label_queue[0].append(f"case{cases_counter}_true:\n")
        #     for inst in case[1]:
        #         switch_env = Environment(env, "switch")
        #         inst.run(ast, switch_env, gen)
        #
        #     gen.label_queue[0].append(f"\tjalr ra\n")
        #
        #     gen.code = gen.code + gen.label_queue.pop(0)
        #
        # gen.label_queue.insert(0,[])
        # gen.label_queue[0].append(f"exit{end_switch}:\n")





















            # gen.code = gen.code + gen.label_queue.pop(0)
            # for inst in case[1]:
            #     try:
            #         switch_env = Environment(env, "switch")
            #         inst.run(ast, switch_env, gen)
            #     except BreakException:
            #         break
            # gen.code.append(f"\tj exit{end_switch}\n")

















        # for case in self.cases:
        #     if case[0] is None:
        #         if len(self.cases) == 1:
        #             self.cases.clear()
        #         else:
        #             self.cases = self.cases[1:]
        #     elif case[0].run(ast, env, gen).value != exp:
        #         if len(self.cases) == 1:
        #             self.cases.clear()
        #         else:
        #             self.cases = self.cases[1:]
        #     elif case[0].run(ast, env, gen).value == exp:
        #         break
        # # print(len(self.cases))
        # if len(self.cases) == 0:
        #     if len(default_case) == 0:
        #         return
        #     for inst in default_case[0]:
        #         try:
        #             switch_env = Environment(env, "switch")
        #             inst.run(ast, switch_env)
        #         except BreakException:
        #             break
        # else:
        #     for case in self.cases:
        #         try:
        #             for inst in case[1]:
        #                 switch_env = Environment(env, "switch")
        #                 inst.run(ast, switch_env)
        #         except BreakException:
        #             break
