def col_from_number(number):
    number = int(number)
    col = ""
    while number > 0:
        number -= 1
        ind = 65 + (number % 26)
        col = chr(ind) + col
        number = int(number/26)
    return col

print(col_from_number(27))
