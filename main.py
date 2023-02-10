
def dec_to_binary(n):
    binaryNum = ""
    while (n > 0):
        binaryNum = binaryNum + str(n%2)
        n = int(n / 2)

    return "".join(binaryNum[::-1])

def binary_to_decimal(number):
    decimal = 0
    
    for digit in number:
        decimal = decimal*2 + int(digit)
    
    return decimal

def add_binary(n1, n2):
    n1 = dec_to_binary(n1)
    n2 = dec_to_binary(n2)

    max_len = max(len(n1), len(n2))

    n1 = n1.zfill(max_len)
    n2 = n2.zfill(max_len)

    res = ""
    carry = 0

    for i in range(max_len - 1, -1, -1):
        re = carry
        if n1[i] == '1':
            re = re+1
        else:
           re = re+0
        if n2[i] == '1':
          re = re+1
        else:
            re = re+0
        if re%2==1:
            res = '1' + res
        else:
            res = '0' + res
        if re<2:
            carry = 0
        else:
            carry = 1

    if carry!=0:
        res = '1' + res

    print(res)
    print(binary_to_decimal(res))