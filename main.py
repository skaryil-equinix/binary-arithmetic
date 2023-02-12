
def dec_to_binary(num):

    bin = [0 for i in range(0,32)]
    idx=31
    if (num>0):
        while(idx>=0 and num>0):
            bin[idx]=num%2
            idx-=1
            num= int(num/2)
    else:
        num=-num
        while(idx>=0 and num>0):
            bin[idx]=num%2
            idx-=1
            num= int(num/2)

        #taking 1s
        for i in range(0,32):
            if bin[i]==0:
                bin[i]=1
            else:
                bin[i]=0

        #taking 2s
        idx=31
        while(idx>=0 and bin[idx]==1):
            bin[idx]=0
            idx-=1
        if(idx>=0):
            bin[idx]=1
    return bin

def binary_to_decimal(bin):

    if(len(bin)!=32):
        print("Invalid Input\nInput should be an array of size 32")
        return
    if(bin[0]==0):
        dec = 0
        for i in range(0,32):
            dec = dec*2 + bin[i]
        
        return dec
    
    else:
        #taking 1s
        for i in range(0,32):
            if bin[i]==0:
                bin[i]=1
            else:
                bin[i]=0

        #taking 2s
        idx=31
        while(idx>=0 and bin[idx]==1):
            bin[idx]=0
            idx-=1
        if(idx>=0):
            bin[idx]=1
        
        #finding the decimal number
        dec = 0
        for i in range(0,32):
            dec = dec*2 + bin[i]
        
        return -dec

def XOR (a, b):
    if a != b:
        return 1
    else:
        return 0

def add_binary(num1, num2):

    n1 = num1[:]
    n2 = num2[:]

    tot = [0 for i in range(0,32)]
    carry = 0
    for i in range(31,-1,-1):
        tot[i] = XOR(XOR(n1[i],n2[i]), carry)
        carry = n1[i]&n2[i] or n1[i]&carry or n2[i]&carry

    return tot

def sub_binary(num1, num2):

    n1 = num1[:]
    n2 = num2[:]
    #taking 1s of n2
    for i in range(0,32):
        if n2[i]==0:
            n2[i]=1
        else:
            n2[i]=0

    #taking 2s of n2
    idx=31
    while(idx>=0 and n2[idx]==1):
        n2[idx]=0
        idx-=1
    if(idx>=0):
        n2[idx]=1

    #now same logic as adding
    tot = [0 for i in range(0,32)]
    carry = 0
    for i in range(31,-1,-1):
        tot[i] = XOR(XOR(n1[i],n2[i]), carry)
        carry = n1[i]&n2[i] or n1[i]&carry or n2[i]&carry

    return tot


def mul_binary(num1, num2):

    tot = [0 for i in range(0,32)]

    for i in range(31, -1, -1):
        
        if num2[i] == 1:
            tot = add_binary(tot, num1)
            
        num1.pop(0)
        num1.append(0)
    
    return tot

def div_binary(num1, num2):
    res = [0 for i in range(0,32)]
    
    while( binary_to_decimal(sub_binary(num1, num2)) >= 0):
        num1 = sub_binary(num1, num2)
        res = add_binary(res, dec_to_binary(1))
        
    return res
