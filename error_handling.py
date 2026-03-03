balance = 5000
try:
    amount = int(input("enter a number"))
    if amount > 5000:
        raise ValueError("insuficent balance")
        
except ValueError as e:
            print(e)

else:
       balance -= amount
       print(balance)

finally:
       print("completed")


# ValueError → Correct type, wrong value

# TypeError → Wrong data type

# ZeroDivisionError → Division by zero

# IndexError → List index out of range

# KeyError → Dictionary key not found

# NameError → Variable not defined

# FileNotFoundError → File does not exist

# AttributeError → Object has no attribute

# ImportError → Module not found

# ModuleNotFoundError → Specific import issue

# OverflowError → Number too large

# IndentationError → Wrong indentation

# EOFError → Input ended unexpectedly