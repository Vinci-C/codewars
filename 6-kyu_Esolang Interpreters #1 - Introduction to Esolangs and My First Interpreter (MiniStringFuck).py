def my_first_interpreter(code):
    cell, output = 0, ""
    for i in code:
        if i == "+":
            cell = (cell + 1) % 256
        if i == ".":
            output += chr(cell)
    return output
