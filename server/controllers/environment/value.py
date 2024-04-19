from controllers.environment.types import ExpressionType


class Value:
    def __init__(self, value, type: ExpressionType, line, column):
        self.value = value
        self.line = line
        self.column = column
        # self.isTemp = isTemp
        self.type = type
        # self.truelvl = truelvl
        # self.falselvl = falselvl
        # self.outlvl = outlvl
