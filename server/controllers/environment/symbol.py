from controllers.environment.types import ExpressionType


class Symbol:
    def __init__(self, line, col, value, type):
        self.line = line
        self.col = col
        self.value = value
        self.constant = False
        self.array_type = ExpressionType.NULL
        self.interface = ""
        self.type = type
