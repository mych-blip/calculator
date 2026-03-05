import tkinter as tk
import math
from scipy.linalg import inv

class AdvancedCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Scientific Calculator")

        # Create a display
        self.display = tk.Entry(master, width=40)
        self.display.grid(row=0, column=0, columnspan=4)

        # Create buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 'sqrt',
            '4', '5', '6', '*', 'pow',
            '1', '2', '3', '-', 'sin',
            '0', '.', '=', '+', 'cos',
            'tan', 'log', 'fact', 'inv', 'solve'
        ]

        row = 1
        col = 0
        for button in buttons:
            tk.Button(self.master, text=button, command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 4:
                col = 0
                row += 1

    def on_button_click(self, button):
        if button == '=':
            self.calculate()
        else:
            current_text = self.display.get()
            new_text = current_text + button
            self.display.delete(0, tk.END)
            self.display.insert(0, new_text)

    def calculate(self):
        try:
            expression = self.display.get()
            if "sqrt" in expression:
                expression = expression.replace("sqrt", "math.sqrt")
            if "pow" in expression:
                expression = expression.replace("pow", "**")
            if "fact" in expression:
                num = int(expression.replace("fact", ""))
                result = math.factorial(num)
            elif "sin" in expression:
                angle = float(expression.replace("sin", ""))
                result = math.sin(math.radians(angle))
            elif "cos" in expression:
                angle = float(expression.replace("cos", ""))
                result = math.cos(math.radians(angle))
            elif "tan" in expression:
                angle = float(expression.replace("tan", ""))
                result = math.tan(math.radians(angle))
            elif "log" in expression:
                num = float(expression.replace("log", ""))
                result = math.log(num)
            elif "inv" in expression:
                matrix = eval(expression.replace("inv", ""))
                result = inv(matrix).tolist()
            elif "solve" in expression:
                # Placeholder for equation solving functionality
                result = 'Equation solving not implemented'
            else:
                result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, 'Error')

if __name__ == '__main__':
    root = tk.Tk()
    calculator = AdvancedCalculator(root)
    root.mainloop()