import math

def splitNumber(number, partSize):
    numberStringRev = str(number)[::-1]
    NParts = list()
    for i in range(5):
        part = numberStringRev[partSize * i:partSize * (i + 1)][::-1]
        if(len(part) > 0):
            NParts.append(int(part))
        else:
            NParts.append(0)
    return NParts

K = 5
A = 1234254325354546356546242454522535454635654624444444456789012345678901245254325
B = 52423456789012345667892524234567890123456789012452543253545463565464564565465435242454522


print(A*B)
#rekurze
def toom5(A,B):
    print("#########")
    print("A:" + str(A))
    print("B:" + str(B))
    if(A == 0 or B == 0):
        return 0
    if(A < 10**5 and B < 10**5):
        return A*B

    kladne = False
    if ((A > 0 and B > 0) or (A < 0 and B < 0)):
        kladne = True
    A = abs(A)
    B = abs(B)
    print("vypocet delky")
    delkaBloku = max(math.floor(math.log(A, 10) / 5), math.floor(math.log(B, 10) / 5)) + 1
    print("delka:" + str(delkaBloku))
    splitA = splitNumber(A, delkaBloku)
    splitB = splitNumber(B, delkaBloku)

    print(splitA)
    print(splitB)
    splitP = list()
    splitP.append(splitA[0]) #p(0) = m0
    splitP.append(splitA[4] + splitA[3] + splitA[2] + splitA[1] + splitA[0]) #p(1) = m4 + m3 + m2 + m1 + m0
    splitP.append(splitA[4] - splitA[3] + splitA[2] - splitA[1] + splitA[0]) #p(-1) = m4 - m3 + m2 - m1 + m0
    splitP.append(16*splitA[4] + 8*splitA[3] + 4*splitA[2] + 2*splitA[1] + splitA[0]) #p(2) = 16m4 + 8m3 + 4m2 + 2m1 + m0
    splitP.append(16*splitA[4] - 8*splitA[3] + 4*splitA[2] - 2*splitA[1] + splitA[0]) #p(-2) = = 16m4 - 8m3 + 4m2 - 2m1 + m0
    splitP.append(81*splitA[4] + 27*splitA[3] + 9*splitA[2] + 3*splitA[1] + splitA[0]) #p(3) = 81m4 + 27m3 + 9m2 + 3m1 + m0
    splitP.append(81*splitA[4] - 27*splitA[3] + 9*splitA[2] - 3*splitA[1] + splitA[0]) #p(-3) = 81m4 - 27m3 + 9m2 - 3m1 + m0
    splitP.append(256*splitA[4] - 64*splitA[3] + 16*splitA[2] - 4*splitA[1] + splitA[0]) #p(-4) = 256m4 - 64m3 + 16m2 - 4m1 + m0
    splitP.append(splitA[4]) #p(inf) = m4


    splitQ = list()
    splitQ.append(splitB[0]) #q(0) = n0
    splitQ.append(splitB[4] + splitB[3] + splitB[2] + splitB[1] + splitB[0]) #q(1) = n4 + n3 + n2 + n1 + n0
    splitQ.append(splitB[4] - splitB[3] + splitB[2] - splitB[1] + splitB[0]) #q(-1) = n4 - n3 + n2 - n1 + n0
    splitQ.append(16*splitB[4] + 8*splitB[3] + 4*splitB[2] + 2*splitB[1] + splitB[0]) #q(2) = 16n4 + 8n3 + 4n2 + 2n1 + n0
    splitQ.append(16*splitB[4] - 8*splitB[3] + 4*splitB[2] - 2*splitB[1] + splitB[0]) #q(-2) = = 16n4 - 8n3 + 4n2 - 2n1 + n0
    splitQ.append(81*splitB[4] + 27*splitB[3] + 9*splitB[2] + 3*splitB[1] + splitB[0]) #q(3) = 81n4 + 27n3 + 9n2 + 3n1 + n0
    splitQ.append(81*splitB[4] - 27*splitB[3] + 9*splitB[2] - 3*splitB[1] + splitB[0]) #q(-3) = 81n4 - 27n3 + 9n2 - 3n1 + n0
    splitQ.append(256*splitB[4] - 64*splitB[3] + 16*splitB[2] - 4*splitB[1] + splitB[0]) #q(-4) = 256n4 - 64n3 + 16n2 - 4n1 + n0
    splitQ.append(splitB[4]) #q(inf) = n4

    rHodnoty = list()
    for i in range(9):
        rHodnoty.append(toom5(splitP[i], splitQ[i])) #nasobeni r(i) = p(i)*q(i)

    #interpolace
    rKoef = list()
    rKoef.append(rHodnoty[0]) #r0
    rKoef.append(round((1/4)*rHodnoty[0] + (3/5)*rHodnoty[1] + (-1)*rHodnoty[2] + (-1/10)*rHodnoty[3] + (3/10)*rHodnoty[4] + (1/105)*rHodnoty[5] + (-1/15)*rHodnoty[6] + (1/140)*rHodnoty[7] + (-144)*rHodnoty[8])) #r1
    rKoef.append(round((-49/36)*rHodnoty[0] + (3/4)*rHodnoty[1] + (3/4)*rHodnoty[2] + (-3/40)*rHodnoty[3] + (-3/40)*rHodnoty[4] + (1/180)*rHodnoty[5] + (1/180)*rHodnoty[6] + (-36)*rHodnoty[8]))  # r2
    rKoef.append(round((-49/144)*rHodnoty[0] + (-1/15)*rHodnoty[1] + (11/18)*rHodnoty[2] + (71/720)*rHodnoty[3] + (-89/240)*rHodnoty[4] + (-1/90)*rHodnoty[5] + (4/45)*rHodnoty[6] + (-7/720)*rHodnoty[7] + (196)*rHodnoty[8]))  # r3
    rKoef.append(round((7/18)*rHodnoty[0] + (-13/48)*rHodnoty[1] + (-13/48)*rHodnoty[2] + (1/12)*rHodnoty[3] + (1/12)*rHodnoty[4] + (-1/144)*rHodnoty[5] + (-1/144)*rHodnoty[6] + (49)*rHodnoty[8]))  # r4
    rKoef.append(round((7/72)*rHodnoty[0] + (-3/80)*rHodnoty[1] + (-17/144)*rHodnoty[2] + (1/360)*rHodnoty[3] + (3/40)*rHodnoty[4] + (1/720)*rHodnoty[5] + (-17/720)*rHodnoty[6] + (1/360)*rHodnoty[7] + (-56)*rHodnoty[8]))  # r5
    rKoef.append(round((-1/36)*rHodnoty[0] + (1/48)*rHodnoty[1] + (1/48)*rHodnoty[2] + (-1/120)*rHodnoty[3] + (-1/120)*rHodnoty[4] + (1/720)*rHodnoty[5] + (1/720)*rHodnoty[6] + (-14)*rHodnoty[8]))  # r6
    rKoef.append(round((-1/144)*rHodnoty[0] + (1/240)*rHodnoty[1] + (1/144)*rHodnoty[2] + (-1/720)*rHodnoty[3] + (-1/240)*rHodnoty[4] + (1/5040)*rHodnoty[5] + (1/720)*rHodnoty[6] + (-1/5040)*rHodnoty[7] + (4)*rHodnoty[8]))  # r7
    rKoef.append(rHodnoty[8]) #r8
    vysledek = 0
    baze = 10**delkaBloku
    for i in range(len(rKoef)-1, -1, -1):
        vysledek = rKoef[i] + (baze)*vysledek

    if(not kladne):
        vysledek = -1*vysledek
    print("------------------")
    print("VYSLEDEK " + str(A) + " x " +str(B) )
    print(vysledek)
    print("------------------")
    return vysledek


print(toom5(A,B))