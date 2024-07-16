def sum_strings(x, y):
    x, y = x.lstrip("0"), y.lstrip("0")
    if not x and not y:
        return ("0")
    if not x:
        return y
    if not y:
        return x
    x = x[::-1]
    y = y[::-1]
    carry, result = 0, []
    for i in range(max(len(x),len(y))):
        digit_x = int(x[i]) if i < len(x) else 0
        digit_y = int(y[i]) if i < len(y) else 0
        total = digit_x + digit_y + carry
        result.append(str(total%10))
        carry = total // 10
    if carry: 
        result.append(str(carry))
    return ''.join(result[::-1]).lstrip("0")

#Given the string representations of two integers, return the string representation of the sum of those integers.

# For example:

# sumStrings('1','2') // => '3'
# A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

# I have removed the use of BigInteger and BigDecimal in java

# Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.
