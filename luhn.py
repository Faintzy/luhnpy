#############################################
#                                           #
#            Luhn Validator                 #
#                                           #
#     Coded by https://github.com/Faintz    #
#                                           #
#              22/11/2020                   #
#                                           #
#############################################

def ispar(n):

    if n % 2 == 0: 
        return True
    else:
        return False

def getlastn(list):

    leng = len(list)
    
    return list[leng - 1]

number = str(input("Insert the number: "))

while len(number) < 1:

    number = str(input("Insert the number: "))

nlist = list(number) # 0 ~ 15
nintlist = [int(i) for i in nlist]
nrev = [int(i) for i in nlist[::-1]]
lastn = getlastn(nlist)
parlst = []
renlst = []

i = 0

while i < len(nrev):

    currentn = nrev[i + 1]
    newn = currentn * 2

    if newn > 9:
        strlst = list(str(newn))
        intlst = [int(i) for i in strlst]
        intrv = sum(intlst)

        parlst.append(intrv)
    
    else:
        parlst.append(newn)

    i += 2

j = 0

while j < len(nrev):

    renlst.append(nrev[j])

    j += 2

if (sum(parlst) + sum(renlst)) % 10 == 0:

    print('is valid')

else:

    print('invalid')
