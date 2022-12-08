"""
Generic Stack Data Structure
"""
class Stack:

    def __init__(self) -> None:
        self.__s = []

    def push(self, value):
        self.__s.append(value)

    def pop(self):
        return self.__s.pop()

    def peek(self):
        if self.is_not_empty():
            return self.__s[len(self.__s) - 1]
        return None

    def is_empty(self):
        return len(self.__s) == 0

    def is_not_empty(self):
        return not self.is_empty()

    def __repr__(self):
        return str(self.__s)

    def __str__(self):
        return str(self.__s)