
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

def add_binary(n1, n2):

    tot = [0 for i in range(0,32)]
    carry = 0
    for i in range(31,-1,-1):
        tot[i] = XOR(XOR(n1[i],n2[i]), carry)
        carry = n1[i]&n2[i] or n1[i]&carry or n2[i]&carry

    return tot


def sub_decimal(num1, num2):

    n1 = num1
    n2 = num2

    one_s=''
    #take 1s of num2
    for i in range(len(n2)):
        if(n2[i]=='0'):
            one_s+='1'
        else:
            one_s+='0'

    two_s=''
    flag=1
    #take 2s of num2
    for i in range(len(one_s)-1, -1, -1):
        if flag==1:
            if(one_s[i]=='0'):
                two_s = '1'+two_s
                flag=0
            else:
                two_s = '0'+two_s
        else:
            two_s = one_s[i]+two_s

    n1 = n1
    n2 = two_s

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

    res = res[len(res)-32:]

    return res


def mul_decimal(num1, num2):

    arr = []
    offset = '0'
    for c in reversed(num2):

        # num1 = num1[len(num1)-32:]
        if c == '1':
            arr.append(num1)
        
        num1 = num1+offset

    tot='0'
    for ele in arr:
        tot = add_decimal(tot, ele)
    
    return tot

