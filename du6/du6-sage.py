R.<x> = ZZ[]

def LM(f,g): #lagnau-mignot
    n = f.degree()
    m = g.degree()
    nsd = abs(gcd(f.coefficients()[::-1][0],g.coefficients()[::-1][0]))
    sumA = 0
    sumB = 0
    for coef in f.coefficients():
        sumA += coef*coef
    for coef in g.coefficients():
        sumB += coef*coef
    mn = min(sqrt(sumA)/abs(f.coefficients()[::-1][0]),sqrt(sumB)/abs(g.coefficients()[::-1][0]))
    return ceil(2^min(n,m)*abs(nsd)*mn)

def prevedPoly(f,p): #prevadi polynom v Zp {0,....,p-1} na {-(p-1)/2,...,0,...,(p-1)/2}
    mez = (p-1)/2
    newCoefs = list()
    for coef in f.coefficients():
        if(coef > mez):
            newCoefs.append(coef-p)
        else:
            newCoefs.append(coef)
    return R(newCoefs)
        
def ModPGCD(f,g):
    PP = Primes()
    mez = LM(f,g)
    d = gcd(f.coefficients()[::-1][0], g.coefficients()[::-1][0])
    p=1
    while(True): ## nahrada za goto 4.
        p = PP.next(p) ## nové prvočíslo
        if(d % p == 0):
            continue
        Zp = PolynomialRing(GF(p),"x")
        h = (Zp(f).gcd(Zp(g)))
        h = h*Zp(d)*Zp(inverse_mod(int(h.coefficients()[::-1][0]),int(p))) #h = h*d*lc(h)^-1 
        if(h.degree()==0):
            return R(1)
        else:
            H = h
            P = p
        while P <= 2*d*mez:
            p = PP.next(p)
            if(d % p == 0):
                continue
            Zp = PolynomialRing(GF(p),"x")
            h = (Zp(f).gcd(Zp(g)))
            h = h*Zp(d)*Zp(inverse_mod(int(h.coefficients()[::-1][0]),int(p))) #h = h*d*lc(h)^-1
            if(h.degree() < H.degree()):
                if(h.degree()==0):
                    return R(1)
                else:
                    H = h
                    P = p
                    continue
            if(h.degree() == H.degree()):
                Hdash = R(CRT(R(H),R(h),P,p))
                H = Hdash
                P *= p
        H = prevedPoly(H,P) #prevede reprezentaci čísel v Zp i na záporná
        if((f % (H/gcd(H.coefficients())) == 0) and (g % (H/gcd(H.coefficients())) == 0)): #kontrola delitelnosti
            return H
        
f = R.random_element(5) 
g = R.random_element(7)
#f = x^5 -x^4 -3*x^2 -3*x +2
#g = x^4 -2*x^3 -3*x^2 +4*x +4
f = f/gcd(f.coefficients())
g = g/gcd(g.coefficients())
print(f)
print(g)
print("gcd: " + str(ModPGCD(f,g)))