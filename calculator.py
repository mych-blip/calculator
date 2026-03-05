import tkinter as tk
from tkinter import font
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Configure style
        self.root.configure(bg="#f0f0f0")
        
        self.expression = ""
        
        # Create display
        self.create_display()
        
        # Create buttons
        self.create_buttons()
    
    def create_display(self):
        display_frame = tk.Frame(self.root, bg="#333333", height=100)
        display_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        
        self.display_var = tk.StringVar(value="0")
        
        display = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 32, "bold"),
            bg="#333333",
            fg="#00ff00",
            anchor="e",
            padx=20,
            pady=20
        )
        display.pack(fill=tk.BOTH, expand=True)
    
    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        buttons = [
            ["C", "←", "÷", "×"],
            ["7", "8", "9", "−"],
            ["4", "5", "6", "+"],
            ["1", "2", "3", "="],
            ["0", ".", "+/−", ""]
        ]
        
        for row_idx, row in enumerate(buttons):
            for col_idx, button_text in enumerate(row):
                if button_text == "":
                    continue
                
                btn = self.create_button(button_frame, button_text)
                btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=5, pady=5)
        
        # Configure grid weights
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
    
    def create_button(self, parent, text):
        if text == "C":
            btn = tk.Button(
                parent,
                text=text,
                font=("Arial", 16, "bold"),
                bg="#f56565",
                fg="white",
                command=self.clear,
                activebackground="#e53e3e"
            )
        elif text == "←":
            btn = tk.Button(
                parent,
                text=text,
                font=("Arial", 16, "bold"),
                bg="#f56565",
                fg="white",
                command=self.backspace,
                activebackground="#e53e3e"
            )
        elif text == "=":
            btn = tk.Button(
                parent,
                text=text,
                font=("Arial", 16, "bold"),
                bg="#48bb78",
                fg="white",
                command=self.calculate,
                activebackground="#38a169"
            )
        elif text in ["÷", "×", "−", "+"]:
            btn = tk.Button(
                parent,
                text=text,
                font=("Arial", 16, "bold"),
                bg="#667eea",
                fg="white",
                command=lambda: self.append_operator(text),
                activebackground="#5568d3"
            )
        elif text == "+/−":
            btn = tk.Button(
                parent,
                text=text,
                font=("Arial", 14, "bold"),
                bg="#ed8936",
                fg="white",
                command=self.toggle_sign,
                activebackground="#dd6b20"
            )
        else:
            btn = tk.Button(
                parent,
                text=text,
                font=("Arial", 16, "bold"),
                bg="#e0e0e0",
                fg="#333333",
                command=lambda: self.append_number(text),
                activebackground="#d0d0d0"
            )
        
        return btn
    
    def append_number(self, number):
        if self.display_var.get() == "0":
            self.expression = number
        else:
            self.expression += number
        
        self.display_var.set(self.expression)
    
    def append_operator(self, op):
        # Convert display operators to standard ones
        operator_map = {"÷": "/", "×": "*", "−": "-"}
        standard_op = operator_map.get(op, op)
        
        if self.expression and self.expression[-1] not in "+-/*":
            self.expression += standard_op
            self.display_var.set(self.expression)
    
    def calculate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.display_var.set(self.expression)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
            self.clear()
        except Exception:
            messagebox.showerror("Error", "Invalid expression!")
            self.clear()
    
    def clear(self):
        self.expression = ""
        self.display_var.set("0")
    
    def backspace(self):
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression if self.expression else "0")
    
    def toggle_sign(self):
        try:
            if self.expression:
                result = -float(self.expression)
                self.expression = str(result)
                self.display_var.set(self.expression)
        except:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()