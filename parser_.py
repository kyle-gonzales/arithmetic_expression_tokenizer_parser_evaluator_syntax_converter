from tokenizer_ import Token, Tokenizer
from tree_ import NumberNode, BinaryOpNode, BinaryTree

"""
Arithmetic Expression Parser
- Implements a recursive descent parser for the following grammar:

<expr> ::=  <term> <OP1>
<OP1> ::=  + <term> <OP1> | - <term> <OP1> | epsilon
<term> ::= <factor> <OP2> 
<OP2> ::= * <factor> <OP2> | / <factor> <OP2> | epsilon
<factor> ::= <final> | ~<final>
<final> ::= (<expr>) | <digit> 
<digit> ::= INT

- Checks if the input string is part of the language of arithmetic expressions
- Stores an abstract syntax tree of the accepted string
"""

class Parser:
    
    def __init__(self, s):
        self.s: str = s
        self.tokenizer = Tokenizer(s)
        self.valid = True
        self.look_ahead : Token
        self.ast : BinaryTree

    def is_valid(self):
        return self.valid

    def get_ast(self):
        if self.is_accepted():
            return self.ast
        return None

    def is_accepted(self):
        self.look_ahead = self.tokenizer.get_next_token()

        self.ast = BinaryTree(self.expression()) # set root node of AST

        if self.ast is None:
            self.valid = False

        if self.look_ahead.type == "END_OF_LINE":
            return self.valid

        return False

    """
    recursive descent parsing starts here
    """
    def expression(self) -> BinaryOpNode:
        t = self.look_ahead # peek at next Token
        if t.type in ("DIGIT", "OPEN_PAREN", "NEGATE"): # term can be a digit, open_paren, or negate
            term = self.term()
            if term is None:
                return None
            result = self.op1(term)
            return result
            
        self.valid = False
        return None

    def op1(self, prev) -> BinaryOpNode:
        t = self.look_ahead
        if t.type in ("PLUS", "MINUS"): # op1 can be a plus or minus operation
            operation = self.eat() #consume the operation sign
            t = self.look_ahead
            if t.type in ("DIGIT", "OPEN_PAREN", "NEGATE"): 
                next = self.term() # get next value from term
                value = BinaryOpNode(prev, operation, next)
                return self.op1(value)

            self.valid = False
            return None

        return prev # epsilon transition; return previous node

    def term(self) -> BinaryOpNode:
        t = self.look_ahead
        if t.type in ("DIGIT", "OPEN_PAREN", "NEGATE"): # factor can be a digit, open_paren, or negate
            factor = self.factor()
            if factor is None:
                return None
            return self.op2(factor)
        else:
            self.valid = False
            return None
    
    def op2(self, prev) -> BinaryOpNode:
        t = self.look_ahead
        if t.type in ("TIMES", "DIVIDES"): #op2 can be a times or divides operation
            operation = self.eat() # consume the operation sign
            t = self.look_ahead
            if t.type in ("DIGIT", "OPEN_PAREN", "NEGATE"):
                next = self.factor()
                value = BinaryOpNode(prev, operation, next)
                return self.op2(value)

            self.valid = False
            return None

        return prev # epsilon transition; return previous node

    def factor(self) -> BinaryOpNode:
        t = self.look_ahead
        if t.type in ("DIGIT", "OPEN_PAREN"): # factor can be a digit or open_paren
            return self.final()
        elif t.type == "NEGATE": # factor can be be a negation
            self.eat() # consume negative sign
            token = self.final()
            if token is None:
                return None
            token.value.value = str(-int(token.value.value))
            return token
        else:
            self.valid = False
            return None

    def final(self) -> NumberNode:
        t = self.look_ahead
        if t.type == "DIGIT": # final can be a digit
            return NumberNode(self.eat()) # consume digit
        elif t.type == "OPEN_PAREN": # final can be an open_paren
            self.eat() # consume open parenthesis
            value = self.expression()
            if value is None:
                return None
            t = self.look_ahead
            if t.type == "CLOSED_PAREN": # check for closed_paren
                self.eat() # consume closing parenthesis
                return value

            self.valid = False
            return None
        else:
            self.valid = False
            return None

    """
    helper functions
    """
    def eat(self): #* set look_ahead to the current_token 
        TOKEN = self.look_ahead

        self.look_ahead = self.tokenizer.get_next_token()
        return TOKEN
