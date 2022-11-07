# package calculator


from math import nan
from enum import Enum
from Stack import *

# A calculator for rather simple arithmetic expressions.
# Your task is to implement the missing functions so the
# expressions evaluate correctly. Your program should be
# able to correctly handle precedence (including parentheses)
# and associativity - see helper functions.
# The easiest way to evaluate infix expressions is to transform
# them into postfix expressions, using a stack structure.
# For example, the expression 2*(3+4)^5 is first transformed
# to [ 3 -> 4 -> + -> 5 -> ^ -> 2 -> * ] and then evaluated
# left to right. This is known as Reverse Polish Notation,
# see: https://en.wikipedia.org/wiki/Reverse_Polish_notation
#
# NOTE:
# - You do not need to implement negative numbers
#
# To run the program, run either CalculatorREPL or CalculatorGUI

MISSING_OPERAND: str = "Missing operand(s)"
DIV_BY_ZERO: str = "Division with 0"
MISSING_PARENTHESIS: str = "Missing parenthesis"
OP_NOT_FOUND: str = "Operator not found"

OPERATORS: str = "+-*/^"
ALL_NUMBERS = "0123456789"


def infix_to_postfix(tokens):
    output_queue = []
    stack = Stack()
    for token in tokens:
        if token.isdigit():
            output_queue.append(token)
        elif token in OPERATORS:
            if stack.is_empty():
                stack.push(token)
            else:
                if stack.peek() in "()":
                    stack.push(token)
                else:
                    current_precedence = get_precedence(token)
                    while (not stack.is_empty()) \
                            and (get_precedence(stack.peek()) > current_precedence
                                 or (get_precedence(stack.peek()) == current_precedence
                                     and get_associativity(token) == Assoc.LEFT)):
                        output_queue.append(stack.pop())
                    stack.push(token)
        elif token == "(":
            stack.push(token)
        elif token == ")":
            while not stack.is_empty() and stack.peek() != "(":
                output_queue.append(stack.pop())
            stack.pop()  # Remove parenthesis
        else:
            output_queue.append(token)
    while not stack.is_empty():
        output_queue.append(stack.pop())
    return output_queue


# Test code: 4^2+5*(2+1)/2

# -----  Evaluate RPN expression -------------------
def eval_postfix(postfix_tokens):
    stack = Stack()
    for token in postfix_tokens:
        if token.isdigit():
            stack.push(int(token))
        elif token in OPERATORS:
            d1 = stack.pop()
            d2 = stack.pop()
            result = apply_operator(token, d1, d2)
            stack.push(result)
        else:
            stack.push(float(token))
    final_result = stack.pop()
    return final_result


# Method used in REPL
def eval_expr(expr: str):
    if len(expr) == 0:
        return ValueError("Missing input")
    tokens = tokenize(expr)
    expr_checked = valid_expr(tokens)
    postfix_tokens = infix_to_postfix(expr_checked)
    return eval_postfix(postfix_tokens)


def apply_operator(op: str, d1: float, d2: float):
    op_switcher = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: y - x,
        "*": lambda x, y: x * y,
        "/": lambda x, y: ZeroDivisionError(DIV_BY_ZERO) if x == 0 else y / x,
        "^": lambda x, y: y ** x
    }
    fun_to_apply = op_switcher.get(op, ValueError(OP_NOT_FOUND))
    return fun_to_apply(d1, d2)


def get_precedence(op: str):
    op_switcher = {
        "+": 2,
        "-": 2,
        "*": 3,
        "/": 3,
        "^": 4
    }
    return op_switcher.get(op, ValueError(OP_NOT_FOUND))


class Assoc(Enum):
    LEFT = 1
    RIGHT = 2


def get_associativity(op: str):
    if op in "+-*/":
        return Assoc.LEFT
    elif op in "^":
        return Assoc.RIGHT
    else:
        return ValueError(OP_NOT_FOUND)


# ---------- Tokenize -----------------------
def tokenize(expr: str):
    empty_string = ""
    empty_list = []
    operators_incl_parenthesis = "()*/+-^"
    for char in expr:
        if char in ALL_NUMBERS + ".":
            empty_string += char
        elif char in operators_incl_parenthesis:
            if empty_string != "":
                empty_list.append(empty_string)
            empty_string = ""
            empty_list.append(char)
        else:
            raise ValueError(f"Encountered: {char}, operand/operator not allowed")
    if empty_string != "":
        empty_list.append(empty_string)
    return empty_list


def valid_expr(expr):
    op_list = []
    num_list = []
    left_paren_list = []
    right_paren_list = []
    for char in expr:
        if char in OPERATORS:
            op_list.append(char)
            continue
        if char.isdigit():
            num_list.append(char)
            continue
        if char == "(":
            left_paren_list.append(char)
            continue
        if char == ")":
            right_paren_list.append(char)
            continue
        else:
            num_list.append(char)
    if len(op_list) >= len(num_list):
        raise ValueError(MISSING_OPERAND)
    if not len(left_paren_list) == len(right_paren_list):
        raise ValueError(MISSING_PARENTHESIS)
    return expr
