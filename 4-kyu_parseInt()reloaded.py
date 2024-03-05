def parse_int(string):
    numbers = {"zero":0, "one":1, "two":2,"three":3,"four":4,"five":5,
           "six":6, "seven":7, "eight":8, "nine":9, "ten":10,
           "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15,
           "sixteen":16, "seventeen":17, "eighteen":18, "nineteen": 19, "twenty":20,
           "thirty":30, "forty":40, "fifty":50,"sixty":60, "seventy":70,
           "eighty":80, "ninety":90}
    multiplier = {"hundred":100, "thousand":1000, "million":1000000}
    temp = 0
    result = 0
    for number in string.split(" "):
        if number in multiplier:
            temp *= multiplier[number]
            if temp >= 1000:
                result = temp
                temp = 0
        elif number != "and":
            nos = number.split("-")
            if len(nos)> 1:
                temp += numbers[nos[0]] + numbers[nos[1]]
            else: temp += numbers[nos[0]]         
    return result + temp
#really simple loops for this somewhat hard kata
