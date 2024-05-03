from enum import Enum


class ExpressionType(Enum):
    NUMBER = 0
    FLOAT = 1
    STRING = 2
    BOOLEAN = 3
    CHAR = 4
    NULL = 5
    ARRAY = 6
    INTERFACE = 7
