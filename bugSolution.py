def function_with_uncommon_error(data):
    try:
        result = 10 / data['value']
    except KeyError:
        return "KeyError: 'value' key not found"
    except ZeroDivisionError:
        return "ZeroDivisionError: Cannot divide by zero"
    except TypeError as e:
        return f"TypeError: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    return result

data1 = {'value': 0}
data2 = {'value': 10}
data3 = {'wrong_key': 10}
data4 = {'value': 'abc'}

print(function_with_uncommon_error(data1))  # Output: ZeroDivisionError: Cannot divide by zero
print(function_with_uncommon_error(data2))  # Output: 1.0
print(function_with_uncommon_error(data3))  # Output: KeyError: 'value' key not found
print(function_with_uncommon_error(data4)) # Output: TypeError: unsupported operand type(s) for /: 'int' and 'str' 