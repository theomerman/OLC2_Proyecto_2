# from controllers.environment.environment.error import Error


class Ast:
    def __init__(self):
        self.instructions = []
        self.console = ''
        self.errors = []
        self.symbol_table = []

    def set_console(self, content):
        self.console += content + '\n'

    def get_console(self):
        return self.console

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def get_instructions(self):
        return self.instructions

    def add_error(self, error):
        self.errors.append(error)

    def get_errors(self):
        return self.errors
