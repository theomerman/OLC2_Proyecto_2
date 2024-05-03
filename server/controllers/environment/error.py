class Error:
    def __init__(self, description: str, env: str, type: str, line, column):
        self.description = description
        self.env = env
        self.type = type
        self.line = line
        self.column = column
