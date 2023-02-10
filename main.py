def binary_to_decimal(number):
    decimal = 0
    
    for digit in number:
        decimal = decimal*2 + int(digit)
    
    return decimal