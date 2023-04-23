def numberArrangement(numarr):
    result = 0
    greaterNo = 0
    smallerNo=0
    for k in range(len(numarr),0,-1 ):
        num=numarr[k-1]
        i=0
        while(num>0):
            if i==0:
                smallerNo = num % 10
                if greaterNo<smallerNo:
                    greaterNo = smallerNo
                i=i+1 
            else:
                rem = num%10
                if smallerNo>rem:
                    smallerNo = rem

                if greaterNo<rem:
                    greaterNo = rem
            num = num//10
        result = result*10+smallerNo
    return greaterNo *10**len(numarr) + result


numarr = [953,407,248]
print(numberArrangement(numarr))