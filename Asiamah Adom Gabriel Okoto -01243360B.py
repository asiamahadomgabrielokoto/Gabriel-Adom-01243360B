import math

def add(*args):
    """Adds any number of arguments together."""
    return sum(args)

def subtract(*args):
    """Subtracts all subsequent arguments from the first argument."""
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    """Multiplies all arguments together."""
    if not args:
        return 0
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    """Divides the first argument by the product of subsequent arguments."""
    if not args:
        return 0
    if len(args) == 1:
        return args[0]
    
    denominator = 1
    for num in args[1:]:
        if num == 0:
            raise ValueError("Division by zero is not allowed")
        denominator *= num
    return args[0] / denominator

def power(*args):
    """Raises the first argument to the power of the product of subsequent arguments."""
    if not args:
        return 1
    if len(args) == 1:
        return args[0]
    
    exponent_product = 1
    for num in args[1:]:
        exponent_product *= num
    return args[0] ** exponent_product

def sqrt(*args):
    """Calculates the square root of a single argument."""
    if len(args) != 1:
        raise ValueError("sqrt requires exactly one argument")
    return math.sqrt(args[0])

# Calculator interface
def main():
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
        'power': power,
        'sqrt': sqrt
    }

    print("Simple Calculator")
    print("Available operations: add, subtract, multiply, divide, power, sqrt")
    
    while True:
        op_input = input("\nOperation (or 'quit' to exit): ").strip().lower()
        if op_input == 'quit':
            break
            
        if op_input not in operations:
            print("Invalid operation. Please try again.")
            continue
            
        try:
            num_input = input("Enter numbers separated by spaces: ").split()
            nums = [float(num) for num in num_input]
            
            if op_input == 'sqrt' and len(nums) != 1:
                print("Error: sqrt requires exactly one number")
                continue
                
            result = operations[op_input](*nums)
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Error: {str(e)}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

if '_name_' == "_main_":
    main()
