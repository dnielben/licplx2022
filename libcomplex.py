# Suma complejos representados como una tupla (real, imaginaria)
def sumacplx(a,b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real, img)

# Multiplica complejos representados como una tupla
def multcplx(a,b):
    real = (a[0] * b[0]) - (a[1]* b[1])
    img = (a[0] * b[1]) + (b[0]*a[1])
    return (real, img)

def prettyprinting(c):
    print( str(c[0]) + "+" + str(c[1]) + "i")

#if __name__ == '__main__':
prettyprinting(sumacplx((2,3),(4,7)))
prettyprinting(multcplx((2,3),(4,7)))


