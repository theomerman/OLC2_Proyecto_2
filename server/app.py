# import controllers.compiler.parser as parser
from controllers.compiler.parser import Parser
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast

env = Environment(None, "global")
ast = Ast()

parser = Parser()

data = '''
const a = 5
const b = 8;
'''


print("\n")
instuctions = parser.parse(data)
for intruction in instuctions:
    intruction.run(ast, env)

for error in ast.get_errors():
    print(error.description)

print(ast.get_console(), end='')

print("\n")




# tmp = 0
# def ackermann(m, n):
#     global tmp
#     tmp += 1
#     if m == 0:
#         return n + 1
#     elif n == 0:
#         return ackermann(m - 1, 1)
#     else:
#         return ackermann(m - 1, ackermann(m, n - 1))
# print(ackermann(2, 3))
# print(tmp)
