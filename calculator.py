import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")

        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(root, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '- ',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(self.root, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                expression = self.result_var.get()
                result = eval(expression)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current = self.result_var.get()
            self.result_var.set(current + char)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()