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

A = 512342543253545463565462424545225354546356698698
B = 52423456789012345667892524234567890123456789012452543253545463565464564565465435242454522


print(A*B)

'''
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
    print(rKoef)
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
'''
def toom52(A,B):
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

    #print(splitA)
    #print(splitB)
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
    print("hodnoty: ", rHodnoty)
    #interpolace
    rKoef = list()
    '''
    rKoef.append(rHodnoty[0]) #r0
    rKoef.append(round((4/5)*rHodnoty[1] + (-4/5)*rHodnoty[2] + (-1/5)*rHodnoty[3] + (1/5)*rHodnoty[4] + (4/105)*rHodnoty[5] + (-4/105)*rHodnoty[6] + (1/280)*rHodnoty[7] + (-1/280)*rHodnoty[8])) #r1
    rKoef.append(round((-205/144)*rHodnoty[0] + (4/5)*rHodnoty[1] + (4/5)*rHodnoty[2] + (-1/10)*rHodnoty[3] + (-1/10)*rHodnoty[4] + (4/315)*rHodnoty[5] + (4/315)*rHodnoty[6] + (-1/1120)*rHodnoty[7] + (-1/1120)*rHodnoty[8]))  # r2
    rKoef.append(round((-61/180)*rHodnoty[1] + (61/180)*rHodnoty[2] + (169/720)*rHodnoty[3] + (-169/720)*rHodnoty[4] + (-1/20)*rHodnoty[5] + (1/20)*rHodnoty[6] + (-7/1440)*rHodnoty[7] + (7/1440)*rHodnoty[8]))  # r3
    rKoef.append(round((91/192)*rHodnoty[0] + (-61/180)*rHodnoty[1] + (-61/180)*rHodnoty[2] + (169/1440)*rHodnoty[3] + (169/1440)*rHodnoty[4] + (-1/60)*rHodnoty[5] + (-1/60)*rHodnoty[6] + (7/5760)*rHodnoty[7] + (7/5760)*rHodnoty[8]))  # r4
    rKoef.append(round((29/720)*rHodnoty[1] + (-29/720)*rHodnoty[2] + (-13/360)*rHodnoty[3] + (13/360)*rHodnoty[4] + (1/80)*rHodnoty[5] + (-1/80)*rHodnoty[6] + (1/720)*rHodnoty[7] + (1/-720)*rHodnoty[8]))  # r5
    rKoef.append(round((-5/96)*rHodnoty[0] + (29/720)*rHodnoty[1] + (29/720)*rHodnoty[2] + (-13/720)*rHodnoty[3] + (-13/720)*rHodnoty[4] + (1/240)*rHodnoty[5] + (1/240)*rHodnoty[6] + (-1/2880)*rHodnoty[7] +(-1/2880)*rHodnoty[8]))  # r6
    rKoef.append(round((-1/720)*rHodnoty[1] + (1/720)*rHodnoty[2] + (1/720)*rHodnoty[3] + (-1/720)*rHodnoty[4] + (-1/1680)*rHodnoty[5] + (1/1680)*rHodnoty[6] + (-1/10080)*rHodnoty[7] + (1/10080)*rHodnoty[8]))  # r7
    rKoef.append(round((1/576)*rHodnoty[0] + (-1/720)*rHodnoty[1] + (-1/720)*rHodnoty[2] + (1/1440)*rHodnoty[3] + (1/1440)*rHodnoty[4] + (-1/5040)*rHodnoty[5] + (-1/5040)*rHodnoty[6] + (1/40320)*rHodnoty[7] +(1/40320)*rHodnoty[8]))  # r8
    '''
    rKoef.append(rHodnoty[0]) #r0
    rKoef.append(round(672*rHodnoty[1] + (-672)*rHodnoty[2] + (-168)*rHodnoty[3] + (168)*rHodnoty[4] + (32)*rHodnoty[5] + (-32)*rHodnoty[6] + 3*rHodnoty[7] + (-3)*rHodnoty[8])/840) #r1
    rKoef.append(round((-205/144)*rHodnoty[0] + (4/5)*rHodnoty[1] + (4/5)*rHodnoty[2] + (-1/10)*rHodnoty[3] + (-1/10)*rHodnoty[4] + (4/315)*rHodnoty[5] + (4/315)*rHodnoty[6] + (-1/1120)*rHodnoty[7] + (-1/1120)*rHodnoty[8]))  # r2
    rKoef.append(round((-61/180)*rHodnoty[1] + (61/180)*rHodnoty[2] + (169/720)*rHodnoty[3] + (-169/720)*rHodnoty[4] + (-1/20)*rHodnoty[5] + (1/20)*rHodnoty[6] + (-7/1440)*rHodnoty[7] + (7/1440)*rHodnoty[8]))  # r3
    rKoef.append(round((91/192)*rHodnoty[0] + (-61/180)*rHodnoty[1] + (-61/180)*rHodnoty[2] + (169/1440)*rHodnoty[3] + (169/1440)*rHodnoty[4] + (-1/60)*rHodnoty[5] + (-1/60)*rHodnoty[6] + (7/5760)*rHodnoty[7] + (7/5760)*rHodnoty[8]))  # r4
    rKoef.append(round((29/720)*rHodnoty[1] + (-29/720)*rHodnoty[2] + (-13/360)*rHodnoty[3] + (13/360)*rHodnoty[4] + (1/80)*rHodnoty[5] + (-1/80)*rHodnoty[6] + (1/720)*rHodnoty[7] + (1/-720)*rHodnoty[8]))  # r5
    rKoef.append(round((-5/96)*rHodnoty[0] + (29/720)*rHodnoty[1] + (29/720)*rHodnoty[2] + (-13/720)*rHodnoty[3] + (-13/720)*rHodnoty[4] + (1/240)*rHodnoty[5] + (1/240)*rHodnoty[6] + (-1/2880)*rHodnoty[7] +(-1/2880)*rHodnoty[8]))  # r6
    rKoef.append(round((-1/720)*rHodnoty[1] + (1/720)*rHodnoty[2] + (1/720)*rHodnoty[3] + (-1/720)*rHodnoty[4] + (-1/1680)*rHodnoty[5] + (1/1680)*rHodnoty[6] + (-1/10080)*rHodnoty[7] + (1/10080)*rHodnoty[8]))  # r7
    rKoef.append(round((1/576)*rHodnoty[0] + (-1/720)*rHodnoty[1] + (-1/720)*rHodnoty[2] + (1/1440)*rHodnoty[3] + (1/1440)*rHodnoty[4] + (-1/5040)*rHodnoty[5] + (-1/5040)*rHodnoty[6] + (1/40320)*rHodnoty[7] +(1/40320)*rHodnoty[8]))  # r8

    vysledek = 0
    print("koef: ", rKoef)
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


print(toom52(A,B))

hodnoty = [0, 1281704619896783055878741204645548544, 57649079395236366711526342277156136, 10198959910473636052776928718722209600, 3420876034469507758663707098085030920, 46016147067694965408160458637030422360, 18161186583685104311908601732094662880, 54386794620600318984893273046852497724, 143760160827623343093160319860704046796]
vysl1 = (4/5)*hodnoty[1] + (-4/5)*hodnoty[2] + (-1/5)*hodnoty[3] + (1/5)*hodnoty[4] + (4/105)*hodnoty[5] + (-4/105)*hodnoty[6] + (1/280)*hodnoty[7] + (-1/280)*hodnoty[8]
vysl2 = 672*hodnoty[1] + (-672)*hodnoty[2] + (-168)*hodnoty[3] + (168)*hodnoty[4] + (32)*hodnoty[5] + (-32)*hodnoty[6] + 3*hodnoty[7] + (-3)*hodnoty[8]
print(-168*hodnoty[3])
mezi = 672*hodnoty[1] + (-672)*hodnoty[2] + (-168)*hodnoty[3] + 168*hodnoty[4]+32*hodnoty[5] + (-32)*hodnoty[6]+ 3*hodnoty[7] + (-3)*hodnoty[8]
print("mezi: ", mezi)
print(round(vysl2))
print(round(round(vysl2)/840))