
def dec_to_binary(n):
    binaryNum = [0] * n
    i = 0
    while (n > 0):
        binaryNum[i] = n % 2
        n = int(n / 2)
        i += 1

    binaryNum.reverse()

    return binaryNum

def binary_to_decimal(number):
    decimal = 0
    
    for digit in number:
        decimal = decimal*2 + int(digit)
    
    return decimal