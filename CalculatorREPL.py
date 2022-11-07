# package calculator
from Calculator import eval_expr


#   A command line interface for the Calculator
#   REPL = Read Eval Print Loop

def program():
    preamble()
    repl_loop()
    goodbye()


def repl_loop():
    while True:
        command = get_input()
        if command == "bye":
            break
        evaluate_command(command)


def evaluate_command(command):
    try:
        result = eval_expr(command)
        print(result)
    except ValueError as ex:
        print(ex)


def get_input():
    command = input("> ")
    return command


def preamble():
    print("Calculator v 1.0. To exit input bye")


def goodbye():
    print("Have a nice day!")


if __name__ == "__main__":
    program()
