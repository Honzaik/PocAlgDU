import random
import time

MAX_LENGTH = 6
BASE = 10

a = list()
b = list()

for i in range(MAX_LENGTH-1):
    a.append(random.randint(0,9))
    b.append(random.randint(0,9))

#aby posledni cislo nebylo 0 hned od zacatku
a.append(random.randint(1, 9))
b.append(random.randint(1, 9))

# -1 = x<y; 0 = x==y; 1 = x>y
def porovnej(x,y):
    if(len(x) > len(y)):
        return 1
    else:
        if(len(x) < len(y)):
            return -1
        else: #stejna delka
            i = len(x)-1
            while((i > 0) and (x[i] == y[i])):
                i = i-1

            if(i == 0):
                return 0
            else:
                if(x[i] > y[i]):
                    return 1
                else:
                    return -1

# čísla jsou v poli (můžou končit 0 nebo nemusejí) - počet cifer = index posledního nenulového čísla
# tedy čísla co končí s 0 jsou stejná jako ta bez nuly <=> [1,2,3,0] == [1,2,3] -> obě jsou 321
def secti(x,y):
    p = 0
    vysledek = list()
    delsi = x
    mensi = y
    if(porovnej(x,y) == -1):
        delsi = y
        mensi = x
    for i in range(len(delsi)):
        if(i >= len(mensi)):
            vysledek.append(delsi[i] + 0 + p)
        else:
            vysledek.append(delsi[i] + mensi[i] + p)

        if(vysledek[i] >= BASE):
            vysledek[i] = vysledek[i] - BASE
            p = 1
        else:
            p = 0
    if(p > 0):
        vysledek.append(p)
    return vysledek

#musi x=>y
def odecti(x,y):
    vysledek = list()
    porovnani = porovnej(x,y)
    if(porovnani == 0):
        return vysledek

    #ted x>y jiste
    p = 0
    for i in range(len(x)):
        if(i >= len(y)):
            temp = x[i] + p
        else:
            temp = x[i] - y[i] + p
        vysledek.append(temp % BASE)
        if(temp >= 0):
            p = 0
        else:
            p = -1
    return vysledek

#jednociferné násobení
def vynasobJednoCif(x, c):
    p = 0
    vysledek = list()
    for i in range(len(x)):
        temp = x[i]*c + p
        p = temp // BASE
        vysledek.append(temp % BASE)
    if(p > 0):
        vysledek.append(p)
    return vysledek

#nasobeni * B^n
def vynasobBase(x, n):
    for i in range(n):
        x.insert(0,0)
    return x

def vynasob(x,y):
    p = 0
    vysledek = list()
    for i in range(len(y)):
        vysledek = secti(vysledek, vynasobBase(vynasobJednoCif(x,y[i]),i))
    return vysledek

#tupé nasobení a+a+a+a+a+a+a+a+
def vynasobTupe(x,y):
    vysledek = list();
    for i in range(int(''.join(map(str,y[::-1])))):
        vysledek = secti(vysledek, x)
    return vysledek


#x/y x>y a mají stejny pocet cifer
def pomocneDeleni(x,y):
    for i in range(9,0,-1):
        mezivysledek = vynasobJednoCif(y,i)
        porovnani = porovnej(x,mezivysledek)
        if(porovnani == 1):
            return i
    return 0

def deleniZbytek(x,y):
    if(porovnej(x,y) == 0):
        return (0,1)
    delsi = x
    mensi = y
    if (len(x) < len(y)):
        delsi = y
        mensi = x
    r = delsi
    q = list()
    for i in range(len(delsi)-len(mensi), -1, -1):
        vynasobeneMensi = vynasobBase(mensi, i)
        q.insert(i, pomocneDeleni(r, vynasobeneMensi))
        r = odecti(r, vynasobJednoCif(vynasobeneMensi,q[i]))
    return q, r

print("a: " + ''.join(str(x) for x in a[::-1]))
print("b: " + ''.join(str(x) for x in b[::-1]))
t = time.time()
c = vynasob(a,b)
print("vypocet (školske násobení) trval: " + str((time.time() - t)*1000) + " ms")
t = time.time()
d = vynasobTupe(a,b)
print("vypocet (tupé) trval: " + str((time.time() - t)*1000) + " ms")
print("vysledek nasobeni: " + ''.join(str(x) for x in c[::-1]))
q, r = deleniZbytek(a,b)

print("a div b: " + ''.join(str(x) for x in q[::-1]))
print("a mod b: " + ''.join(str(x) for x in r[::-1]))
