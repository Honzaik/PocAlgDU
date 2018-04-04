import math
from fractions import Fraction

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

def toom52(A,B):
    if(A == 0 or B == 0):
        return 0
    if(A < 10**5 and B < 10**5):
        return A*B

    kladne = False
    if ((A > 0 and B > 0) or (A < 0 and B < 0)):
        kladne = True
    A = abs(A)
    B = abs(B)
    delkaBloku = max(math.floor(math.log(A, 10) / 5), math.floor(math.log(B, 10) / 5)) + 1
    splitA = splitNumber(A, delkaBloku)
    splitB = splitNumber(B, delkaBloku)

    splitP = list()
    splitP.append(splitA[0]) #p(0) = m0
    splitP.append(splitA[4] + splitA[3] + splitA[2] + splitA[1] + splitA[0]) #p(1) = m4 + m3 + m2 + m1 + m0
    splitP.append(splitA[4] - splitA[3] + splitA[2] - splitA[1] + splitA[0]) #p(-1) = m4 - m3 + m2 - m1 + m0
    splitP.append(16*splitA[4] + 8*splitA[3] + 4*splitA[2] + 2*splitA[1] + splitA[0]) #p(2) = 16m4 + 8m3 + 4m2 + 2m1 + m0
    splitP.append(16*splitA[4] - 8*splitA[3] + 4*splitA[2] - 2*splitA[1] + splitA[0]) #p(-2) = = 16m4 - 8m3 + 4m2 - 2m1 + m0
    splitP.append(81*splitA[4] + 27*splitA[3] + 9*splitA[2] + 3*splitA[1] + splitA[0]) #p(3) = 81m4 + 27m3 + 9m2 + 3m1 + m0
    splitP.append(81*splitA[4] - 27*splitA[3] + 9*splitA[2] - 3*splitA[1] + splitA[0]) #p(-3) = 81m4 - 27m3 + 9m2 - 3m1 + m0
    splitP.append(256*splitA[4] - 64*splitA[3] + 16*splitA[2] - 4*splitA[1] + splitA[0]) #p(-4) = 256m4 - 64m3 + 16m2 - 4m1 + m0
    splitP.append(256*splitA[4] + 64*splitA[3] + 16*splitA[2] + 4*splitA[1] + splitA[0]) #p(4) = 256m4 + 64m3 + 16m2 + 4m1 + m0


    splitQ = list()
    splitQ.append(splitB[0]) #q(0) = n0
    splitQ.append(splitB[4] + splitB[3] + splitB[2] + splitB[1] + splitB[0]) #q(1) = n4 + n3 + n2 + n1 + n0
    splitQ.append(splitB[4] - splitB[3] + splitB[2] - splitB[1] + splitB[0]) #q(-1) = n4 - n3 + n2 - n1 + n0
    splitQ.append(16*splitB[4] + 8*splitB[3] + 4*splitB[2] + 2*splitB[1] + splitB[0]) #q(2) = 16n4 + 8n3 + 4n2 + 2n1 + n0
    splitQ.append(16*splitB[4] - 8*splitB[3] + 4*splitB[2] - 2*splitB[1] + splitB[0]) #q(-2) = = 16n4 - 8n3 + 4n2 - 2n1 + n0
    splitQ.append(81*splitB[4] + 27*splitB[3] + 9*splitB[2] + 3*splitB[1] + splitB[0]) #q(3) = 81n4 + 27n3 + 9n2 + 3n1 + n0
    splitQ.append(81*splitB[4] - 27*splitB[3] + 9*splitB[2] - 3*splitB[1] + splitB[0]) #q(-3) = 81n4 - 27n3 + 9n2 - 3n1 + n0
    splitQ.append(256*splitB[4] - 64*splitB[3] + 16*splitB[2] - 4*splitB[1] + splitB[0]) #q(-4) = 256n4 - 64n3 + 16n2 - 4n1 + n0
    splitQ.append(256*splitB[4] + 64*splitB[3] + 16*splitB[2] + 4*splitB[1] + splitB[0]) #q(4) = 256n4 + 64n3 + 16n2 + 4n1 + n0

    rHodnoty = list()
    for i in range(9):
        rHodnoty.append(round(toom52(splitP[i], splitQ[i]))) #nasobeni r(i) = p(i)*q(i)


    #interpolace
    rKoef = list()
    #pouziti tridy fraction, protoze python nepresne delil velka cisla
    rKoef.append(rHodnoty[0]) #r0
    rKoef.append(int(Fraction(round(672*rHodnoty[1] + (-672)*rHodnoty[2] + (-168)*rHodnoty[3] + (168)*rHodnoty[4] + (32)*rHodnoty[5] + (-32)*rHodnoty[6] + 3*rHodnoty[7] + (-3)*rHodnoty[8]),840))) #r1
    rKoef.append(int(Fraction(round((-14350)*rHodnoty[0] + (8064)*rHodnoty[1] + (8064)*rHodnoty[2] + (-1008)*rHodnoty[3] + (-1008)*rHodnoty[4] + (128)*rHodnoty[5] + (128)*rHodnoty[6] + (-9)*rHodnoty[7] + (-9)*rHodnoty[8]),10080)))  # r2
    rKoef.append(int(Fraction(round((-488)*rHodnoty[1] + (488)*rHodnoty[2] + (338)*rHodnoty[3] + (-338)*rHodnoty[4] + (-72)*rHodnoty[5] + (72)*rHodnoty[6] + (-7)*rHodnoty[7] + (7)*rHodnoty[8]),1440)))  # r3
    rKoef.append(int(Fraction(round((2730)*rHodnoty[0] + (-1952)*rHodnoty[1] + (-1952)*rHodnoty[2] + (676)*rHodnoty[3] + (676)*rHodnoty[4] + (-96)*rHodnoty[5] + (-96)*rHodnoty[6] + (7)*rHodnoty[7] + (7)*rHodnoty[8]),5760)))  # r4
    rKoef.append(int(Fraction(round((29)*rHodnoty[1] + (-29)*rHodnoty[2] + (-26)*rHodnoty[3] + (26)*rHodnoty[4] + (9)*rHodnoty[5] + (-9)*rHodnoty[6] + (1)*rHodnoty[7] + (-1)*rHodnoty[8]),720)))  # r5
    rKoef.append(int(Fraction(round((-150)*rHodnoty[0] + (116)*rHodnoty[1] + (116)*rHodnoty[2] + (-52)*rHodnoty[3] + (-52)*rHodnoty[4] + (12)*rHodnoty[5] + (12)*rHodnoty[6] + (-1)*rHodnoty[7] +(-1)*rHodnoty[8]),2880)))  # r6
    rKoef.append(int(Fraction(round((-14)*rHodnoty[1] + (14)*rHodnoty[2] + (14)*rHodnoty[3] + (-14)*rHodnoty[4] + (-6)*rHodnoty[5] + (6)*rHodnoty[6] + (-1)*rHodnoty[7] + (1)*rHodnoty[8]), 10080)))  # r7
    rKoef.append(int(Fraction(round((70)*rHodnoty[0] + (-56)*rHodnoty[1] + (-56)*rHodnoty[2] + (28)*rHodnoty[3] + (28)*rHodnoty[4] + (-8)*rHodnoty[5] + (-8)*rHodnoty[6] + (1)*rHodnoty[7] +(1)*rHodnoty[8]), 40320)))  # r8

    vysledek = 0
    baze = 10**delkaBloku
    for i in range(len(rKoef)-1, -1, -1): #dosazeni
        vysledek = rKoef[i] + (baze)*vysledek

    if(not kladne):
        vysledek = -1*vysledek
    return vysledek

A = 512342543423456789012345678901245423456789012345678901245423456789012345678901245
B = 52423456789012345667892524234567890123456789012452543253545463565464564565465435242454522


print(A*B) #spravny vysledek
print(toom52(A,B)) #vysledek algoritmu
