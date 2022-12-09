from tokenizer_ import Token
from stack_ import Stack

"""
General Node Class
"""
class Node:
    def __init__(self, value, left_child = None, right_child = None) -> None:
        self.value = value
        self.left_child : Node = left_child
        self.right_child : Node = right_child
    
    def is_leaf(self):
        return (not bool(self.left_child)) and (not bool(self.right_child))

"""
LEAF in Abstract Syntax Tree

- Inherits from Node
"""
class NumberNode(Node):
    def __init__(self, token : Token) -> None:
        super().__init__(token)
        self.token = self.value
    
    def __repr__(self) -> str:
        return f"{self.token.value}"

    def __str__(self) -> str:
        return f"{self.token.value}"

"""
BRANCH in Abstract Syntax Tree for Arithmetic Expressions

- Inherits from Node
"""
class BinaryOpNode(Node):
    def __init__(self, num1_token : Node, op_token : Token, num2_token : Node) -> None:
        super().__init__(op_token, num1_token, num2_token)
        self.op = self.value
        self.num1 = self.left_child
        self.num2 = self.right_child

    def __repr__(self) -> str:
        return f"({self.num1} {self.op.value} {self.num2})"

    def __str__(self) -> str:
        return f"({self.num1} {self.op.value} {self.num2})"

"""
Generic Binary Tree Data Structure
"""
class BinaryTree:
    def __init__(self, root : Node) -> None:
        self.root = root

    def __repr__(self) -> str:
        return f"{self.root}"

    def preorder_traversal(self, root : Node, traversal = Stack()):
        if bool(root):
            traversal.push(root.value)
            traversal = self.preorder_traversal(root.left_child, traversal)
            traversal = self.preorder_traversal(root.right_child, traversal)
        return traversal

    def postorder_traversal(self, root : Node, traversal = Stack()):
        if bool(root):
            traversal = self.postorder_traversal(root.left_child, traversal)
            traversal = self.postorder_traversal(root.right_child, traversal)
            traversal.push(root.value)
        return traversal

    def inorder_traversal(self, root : Node, traversal = Stack()):
        if bool(root):
            traversal = self.inorder_traversal(root.left_child, traversal)
            traversal.push(root.value)
            traversal = self.inorder_traversal(root.right_child, traversal)
        return traversal