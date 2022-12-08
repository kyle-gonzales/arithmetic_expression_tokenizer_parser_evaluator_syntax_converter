from tree_ import BinaryTree, Node, NumberNode
from tokenizer_ import Token


"""
Evaluator for Arithmetic Expressions

- Evaluates an abstract syntax tree (initally parsed) of an expression
"""
class Evaluator:
    def __init__(self, ast : BinaryTree) -> None:
        self.__ast = ast
        self.__result = self.__evaluate(self.__ast.root)
    
    def eval(self):
        return self.__result

    def __evaluate(self, root : Node):

        if self.__ast.root is None:
            return 0
        if isinstance(root, NumberNode):
            return int(root.value.value) # ? or float?

        x = self.__evaluate(root.left_child)
        y = self.__evaluate(root.right_child)
        return self.__calculate(root.value, x, y)

    def __calculate(self, op : Token, x, y):
        if op.type == "PLUS":
            return x + y
        if op.type == "MINUS":
            return x - y
        if op.type == "TIMES":
            return x * y
        if op.type == "DIVIDES":
            try:
                return x / y
            except(ZeroDivisionError):
                raise ZeroDivisionError("Cannot divide by 0! REVIEW INPUT EXPRESSION")

