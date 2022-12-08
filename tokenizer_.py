"""
Arithmetic Expression Tokenizer

- Checks for the next input in the input stream
- Returns the next token in the input stream
"""
from dataclasses import dataclass


@dataclass
class Token:
    type : str
    value : str

class Tokenizer:

    def __init__(self, s):
        self.s : str = s.strip()
        self.cursor : int = 0
    
    def get_next_token(self):
        if not self.has_more_tokens():
            return Token("END_OF_LINE", None)

        STRING: str= self.s[self.cursor:]
        if STRING[0].isspace():
            self.cursor += 1
            return self.get_next_token()
        if STRING[0].isdecimal():
            number = ""
            for char in STRING: #? maybe check if there is a next token
                if not char.isdecimal():
                    break
                number += char
                self.cursor += 1
            return Token("DIGIT", number)
        if STRING[0] == "~":
            self.cursor += 1
            return Token("NEGATE", STRING[0])   
        if self.is_minus(STRING[0]):
            minus = STRING[0]
            self.cursor += 1
            return Token("MINUS", minus)
        if self.is_plus(STRING[0]):
            plus = STRING[0]
            self.cursor += 1
            return Token("PLUS", plus)
        if self.is_times(STRING[0]):
            times = STRING[0]
            self.cursor += 1
            return Token("TIMES", times)
        if self.is_divides(STRING[0]):
            divides = STRING[0]
            self.cursor += 1
            return Token("DIVIDES", divides)
        if self.is_open_paren(STRING[0]):
            open_paren = STRING[0]
            self.cursor += 1
            return Token("OPEN_PAREN", open_paren)
        if self.is_closed_paren(STRING[0]):
            closed_paren = STRING[0]
            self.cursor += 1
            return Token("CLOSED_PAREN", closed_paren)
        else:
            raise SyntaxError(f"Invalid Token: '{STRING[0]}'")

    def has_more_tokens(self):
        return self.cursor < len(self.s)

    """
    Helper Functions
    """
    def is_digit(self, s):
        return s == '0' or s == '1' or s == '2' or s == '3'
    def is_plus(self, s):
        return s == "+"
    def is_minus(self, s):
        return s == "-"
    def is_times(self, s):
        return s == "*"
    def is_divides(self, s):
        return s == "/"
    def is_open_paren(self, s):
        return s == "("
    def is_closed_paren(self, s):
        return s == ")"
