# ============================================================================
# TODO: Data Type Conversion

# Create a function called data_type_conversion.
# It takes two parameters, the value and the name of the data type requested, one of float, str, or int.
# Return the converted value.
# Error handling: The function might be called with a bad parameter.
# For example, the caller might try to convert the string "nonsense" to a float.
# Catch the error that occurs in this case. If this error occurs,
# return the string You can't convert {value} into a {type}., so again you use a formatted string.

# ============================================================================

def data_type_conversion(value, data_type):
    if data_type not in ["float", "str", "int"]:
        return f"Invalid data type: {data_type}"
    try:
        if data_type == "float":
            return float(value)
        if data_type == "str":
            return str(value)
        if data_type == "int":
            return int(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."


print(data_type_conversion("nonsense", "floatiiiiSSSS"))
