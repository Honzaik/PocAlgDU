import time

#vrátí a^b mod n
def binMocneni(a,b,n):
    bBinary = bin(b)[2:]
    c = 1
    t = a
    for i in range(len(bBinary)-1, -1, -1):
        if(bBinary[i] == '1'):
            c = (c*t) % n
        t = (t*t) % n
    return c

#spočítá bezout koeficienty a,b
def eGCD(a, b):
    posledniZb = a if a>b else b
    zb = b if a>b else a
    posledniU = 1
    posledniV = 0
    u = 0
    v = 1
    while zb != 0:
        q = posledniZb // zb
        temp = zb
        zb = posledniZb - q * temp
        posledniZb = temp
        temp = u
        u = posledniU - q*temp
        posledniU = temp
        temp = v
        v = posledniV - q * temp
        posledniV = temp

    return (posledniU, posledniV) if a>b else (posledniV, posledniU)

#inverz čísla a v tělese Z_p
def invEuklid(a,p):
    uKoef = eGCD(a,p)[0]
    return uKoef%p

def invBinMoc(a,p):
    return binMocneni(a,p-2,p)

a = 2523153559648721617104534282427629713082205297585986280524461663705232364614806981444657429677886260
b = 494901490148656294989256362522144030353584406332617683778164975245050440202271922970241194284433452
p = 13592615101577432121899174150191209286449325968474600456048437312563244755078161538439914289147727277
t = time.time()
print(invEuklid(a,p))
print("vypocet (euklid) trval: " + str((time.time() - t)*1000) + " ms")

t = time.time()
print(invBinMoc(a,p))
print("vypocet (fermat) trval: " + str((time.time() - t)*1000) + " ms")