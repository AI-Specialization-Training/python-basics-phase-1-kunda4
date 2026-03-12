# ============================================================================
# TODO: Simple calculator

# Write a calc function. It takes three arguments.
# The default value for the third argument is "multiply".
# The first two arguments are values that are to be combined using the operation requested by the third argument,
# a string that is one of the following `add`, `subtract`, `multiply`, `divide`, `modulo`, `int_divide` (for integer division) and `power`.
# The function returns the result.
# ============================================================================

def calc_function(num1, num2, operation="add"):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2
    elif operation == "modulo":
        return num1 % num2
    elif operation == "int_divide":
        return num1 // num2
    elif operation == "power":
        return num1 ** num2
    else:
        raise ValueError("Invalid operation")
