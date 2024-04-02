def square_digits(num):
    result = ""
    for i in str(num):
        result = result + str(int(i)*int(i))
    return(int(result))
