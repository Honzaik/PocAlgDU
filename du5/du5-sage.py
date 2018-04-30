R.<x> = QQ[]

def inv(poly, n):
    g = 1/poly.coefficients()[0][0]
    for i in range(1, ceil(log(n,2))+1, 1):
        g = (g * (2 - poly*g)) % (x^(2^i))    
    return g % (x^n)

f = 5*x^5 + 6*x^4 + (1/10)*x + 1/200
print(inv(f,6)) #-630600000*x^5 + 31760000*x^4 - 1600000*x^3 + 80000*x^2 - 4000*x + 200