# Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Example usage:
if __name__ == "__main__":
    print("Addition of 5 and 3:", add(5, 3))
    print("Subtraction of 5 and 3:", subtract(5, 3))
    print("Multiplication of 5 and 3:", multiply(5, 3))
    print("Division of 5 and 3:", divide(5, 3))