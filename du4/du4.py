from cmath import exp, pi
from math import log2

def vratLiche(a):
    oddA = list();
    for i in range(len(a)):
        if(i % 2 == 1):
            oddA.append(a[i])
    return oddA

def vratSude(a):
    evenA = list()
    for i in range(len(a)):
        if(i % 2 == 0):
            evenA.append(a[i])
    return evenA

def roundComplex(vysl): #zaokrouhlování 
    newVysl = list()
    for v in vysl:
        a = round(v.real,5)
        b = round(v.imag,5)
        newVysl.append(complex(a,b))
    return newVysl

def recursiveComplexFFT(n, prim, a):
        if(n == 1):
            return [a[0]]
        else:
            nHalf = int(n/2)
            newPrim = prim*prim
            b = recursiveComplexFFT(nHalf, newPrim, vratSude(a))
            c = recursiveComplexFFT(nHalf, newPrim, vratLiche(a))
            result = [0]*int(n)
            for i in range(nHalf):
                tempPrim = prim**i
                result[i] = b[i]+(tempPrim)*c[i]
                result[nHalf+i] = b[i]-(tempPrim)*c[i]
            return roundComplex(result)

def rev(i,k): #rev funkce
    mask = '{0:0' + str(k) + 'b}'
    return int(mask.format(i)[::-1],2)

def iterativeComplexFFT(n, prim, a):
    k = int(log2(n))
    A = [0]*n
    for i in range(n):
        A[i] = a[rev(i,k)]
    prims = [0]*k
    prims[k-1] = prim
    for i in range(k-2,-1,-1):
        prims[i] = prims[i+1]*prims[i+1]
    for u in range(1,k+1,1):
        m = 2**u
        for i in range(0, n-m+1, m):
            for j in range(0,int(m/2),1):
                temp = (prims[u-1]**j)*A[i+j+int(m/2)]
                v1 = A[i+j] + temp
                v2 = A[i+j] - temp
                A[i+j] = v1
                A[i+j+int(m/2)] = v2
    return roundComplex(A)

vektor = [1,1,2,2,5,2,4,7] #pocitani vektor
n = len(vektor)
myPrim = exp((2j*pi)/n) #primitivni odmocnina
res = recursiveComplexFFT(n, myPrim, vektor) #rekurzivni fft
print(res)
myPrim = exp((2j*pi)/n)
res2 = iterativeComplexFFT(n, myPrim, vektor) #iterativni fft
print(res2)