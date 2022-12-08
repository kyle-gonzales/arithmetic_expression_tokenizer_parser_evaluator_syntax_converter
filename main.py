from parser_ import Parser
from syntax_converter import *
from evaluator_ import Evaluator

# Input your expression here!

s = "   ~123/ (11 + 32 / 23) + ((11/237+(169-36))*42) - ~92     "
# s =  "(2+3*2)+((~2*5+8)*1)"

parser = Parser(s)
ast = parser.get_ast()
interpreter = Evaluator(ast)

if bool(ast):
    # print(infix_to_prefix(s))
    print(to_prefix(ast))
    # print(infix_to_postfix(s))
    print(to_postfix(ast))
    print(interpreter.eval())

else:
    print("Invalid Expression")

# print(eval(str(ast)))