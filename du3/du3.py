import math

def splitNumber(number, partSize):
    numberStringRev = str(number)[::-1]
    NParts = list()
    for i in range(5):
        NParts.append(int(numberStringRev[partSize * i:partSize * (i + 1)]))
    return NParts

K = 5
A = 1234567890123456789012452543253545463565464564565465435242454522
B = 524234567890123456789012452543253545463565464564565465435242454522
delkaBloku = max(math.floor(math.log(A,10)/5), math.floor(math.log(B,10)/5))+1

print(delkaBloku)

#rekurze
splitA = splitNumber(A, delkaBloku)
splitB = splitNumber(B, delkaBloku)
print(splitA)
print(splitB)

splitP = list()
splitP.append(splitA[0]) #p(0)
splitP.append(splitA[0]) #p(1)
splitP.append(splitA[0]) #p(-1)
splitP.append(splitA[0]) #p(2)
splitP.append(splitA[0]) #p(-2)
splitP.append(splitA[0]) #p(3)
splitP.append(splitA[0]) #p(-3)
splitP.append(splitA[0]) #p(-4)
splitP.append(splitA[4]) #p(inf)


