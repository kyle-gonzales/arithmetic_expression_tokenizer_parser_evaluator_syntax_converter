from tokenizer_ import Tokenizer
from stack_ import Stack
from tree_ import BinaryTree

# Converts an infix arithmetic expression to its prefix notation using an postorder traversal
def to_prefix(ast: BinaryTree):
    tokens : Stack = ast.preorder_traversal(ast.root)
    prefix = ""
    while (tokens.is_not_empty()):
        prefix = tokens.pop().value + " " + prefix
    return prefix.strip()

# Converts an infix arithmetic expression to its postfix notation using an postorder traversal
def to_postfix(ast: BinaryTree):
    tokens : Stack = ast.postorder_traversal(ast.root)
    postfix = ""
    while (tokens.is_not_empty()):
        postfix = tokens.pop().value + " " + postfix 
    return postfix.strip()

# Returns an inorder traversal of the abstract syntax tree
def infix_t(ast: BinaryTree):
    tokens : Stack = ast.inorder_traversal(ast.root)
    infix = ""
    while (tokens.is_not_empty()):
        infix = tokens.pop().value + " " + infix 
    return infix.strip()
"""
alternate solutions
"""

OPERANDS = ("PLUS", "MINUS", "TIMES", "DIVIDES")

# Converts an infix arithmetic expression to its postfix notation using a stack
def infix_to_postfix(s : str):
    operator_stack = Stack()
    tokenizer = Tokenizer(s)
    postfix_exp = ""

    while (tokenizer.has_more_tokens()):
        input_token = tokenizer.get_next_token()
        # print(input_token)
        # print(operator_stack)

        if input_token.type == "DIGIT":
            postfix_exp += input_token.value + " "
        elif input_token.type == "OPEN_PAREN":
            operator_stack.push(input_token.value)
        elif input_token.type == "CLOSED_PAREN":
            while operator_stack.peek() != "(":
                postfix_exp += operator_stack.pop() + " "
            operator_stack.pop() 
        else:
            
            while (operator_stack.is_not_empty() and __get_precedence(input_token.value) <= __get_precedence(operator_stack.peek())):
                postfix_exp += operator_stack.pop() + " "

            operator_stack.push(input_token.value)
        
    while (operator_stack.is_not_empty()):
        postfix_exp += operator_stack.pop() + " "

    return postfix_exp.strip()

# Converts an infix arithmetic expression to its postfix notation using a stack
def infix_to_prefix(s : str):
    operator_stack = Stack()
    reverse = s[::-1]
    tokenizer = Tokenizer(reverse)
    prefix_exp = ""

    while (tokenizer.has_more_tokens()):
        input_token = tokenizer.get_next_token()
        # print(input_token)
        # print(operator_stack)

        if input_token.type == "DIGIT":
            prefix_exp += input_token.value + " "
        elif input_token.type == "CLOSED_PAREN":
            operator_stack.push(input_token.value)
        elif input_token.type == "OPEN_PAREN":
            while operator_stack.peek() != ")":
                prefix_exp += operator_stack.pop() + " "
            operator_stack.pop()
        else:
            
            while (operator_stack.is_not_empty() and __get_precedence(input_token.value) < __get_precedence(operator_stack.peek())):
                prefix_exp += operator_stack.pop() + " "
            operator_stack.push(input_token.value)
        
    while (operator_stack.is_not_empty()):
        prefix_exp += operator_stack.pop() + " "

    return prefix_exp[::-1].strip()

"""
helper functions for the notation converters
"""
def __get_precedence(op : str) -> int:
    precedence = {"*": 2, "/": 2, "+": 1, "-":1}

    if op in precedence.keys():
        return precedence[op]
    return -1

