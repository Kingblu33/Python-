from re import A


def countdown ():
    newli=[]
    for li in range (5,0,-1):
        newli.append(li)

    return newli

templi = countdown()
print(templi)

def printreturn(a,b):
    print(a)

    return b

b =printreturn(1,2)
print(b)

def firrstpluslenght():
    plusultra=[1,2,3,4,5]
    sum1= plusultra[0] + len(plusultra)

    return sum1

sum1=firrstpluslenght()
print(sum1)


def valuegreater ():
    newarr=[]
    temp=0
    plusnew =[1,2,3,4,5]
    for k in range (0,len(plusnew)):
        if plusnew[1] < plusnew[k]:
            temp = plusnew[k]
            newarr.append(temp)

    return newarr


y= valuegreater()
print(y)

def lengthvalue(size,value):
    newList = []
    for i in range(0,size):
        newList.append(value)
    return newList
print(lengthvalue(8,5))


