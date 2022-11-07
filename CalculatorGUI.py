# package calculator

from tkinter import *

from Calculator import *

# A graphical user interface for the Calculator


class CalculatorGUI:
    @staticmethod
    def calculator_program():
        gui = CalculatorGUI()
        gui.start()

    def __init__(self):
        # create a GUI window
        self.__gui = Tk()
        self.__equation = StringVar()

    def start(self):
        self.__setup_gui_window()
        self.__setup_expression_field()
        self.__create_and_attach_buttons()
        # start the GUI
        self.__gui.mainloop()

    # ----- Shhh, here be private methods ----
    def __setup_expression_field(self):
        expression_field = Entry(self.__gui, textvariable=self.__equation)
        expression_field.grid(columnspan=5, ipadx=70)

    def __setup_gui_window(self):
        self.__gui.configure(background="cyan")
        self.__gui.title("Simple Calculator")
        self.__gui.geometry("290x130")

    def __create_and_attach_buttons(self):
        buttons = ["123+C", "456-^", "789*.", "(0)/="]
        for row in range(len(buttons)):
            for col in range(len(buttons[row])):
                self.__create_and_attach_button(buttons[row][col], row, col)

    def __create_and_attach_button(self, text, row, col):
        button = self.__create_button(text)
        button.grid(row=row+2, column=col)

    def __create_button(self, text):
        return Button(self.__gui, text=text, fg='black', bg='white',
                      command=lambda: self.__handle_command(text), height=1, width=7)

    # ---- Callback handlers for button presses ----
    def __handle_command(self, button_pressed):
        switcher = {
            "C": self.__clear_equation,
            "=": self.__evaluate_equation
        }
        cmd = switcher.get(button_pressed, lambda: self.__press(button_pressed))
        cmd()

    # Handle any button press that extends the current equation
    def __press(self, txt):
        new_txt = self.__equation.get() + txt
        self.__equation.set(new_txt)

    # Handle reset (C)
    def __clear_equation(self):
        self.__equation.set("")

    # Handle evaluate (=)
    def __evaluate_equation(self):
        expression = self.__equation.get()
        try:
            result = eval_expr(expression)
            self.__equation.set(str(result))
        except ValueError as ve:
            self.__equation.set(ve)


if __name__ == "__main__":
    CalculatorGUI.calculator_program()
