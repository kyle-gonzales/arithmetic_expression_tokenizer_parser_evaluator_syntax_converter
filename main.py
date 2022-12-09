from parser_ import Parser
from syntax_converter import *
from evaluator_ import Evaluator


def main():
    # Input your expression here!

    # s = " (11 + 32 / -(-23+1))+ (-(11/237+(169-36))*42) - -92     "
    # s = "-(-1)"
    s =  "(2+3*2)+((-2*5+8)*1)"

    parser = Parser(s)
    ast = parser.get_ast()
    print(ast)

    if bool(ast):
        # print(infix_to_prefix(s))
        print(to_prefix(ast))
        # print(infix_to_postfix(s))
        print(to_postfix(ast))

        interpreter = Evaluator(ast)
        print(interpreter.eval())

    else:
        print("Invalid Expression")

    print(eval(str(s)))

if __name__ == "__main__":
    main()