def distance(x1,y1,x2,y2):
    dx : x2-x1
    dy :y2-y1
    print'dx is', dx
    print'dy is', dy
    return 0.0
def distance(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    dsquared=dx**2+dy**2
    print 'dsquaed is':',dsquared'
    return 0.0'
def distance(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    dsquared=dx**2+dy**2
    result=math.sqrt(dsquared)
    return result
def is_divisible(x,y):
    if x%y == 0:
        return true
    else:
        return false
def is_divisible(x,y,z):
    if x<=y<=z:
        return true
    else:
        return false
def factorial(n):
    if n==0:
        return 1
    else:
        recurse=factorial(n-1)
        result=n*recurse
        return result
def fibonacci (n):
    if n=0:
    return 1
   elif n==1:
    return 1
   else:
    return fibonacci(n-1)+fibonacci(n-2)
def factorial (n):
    if not isinstance(n,int):
        print 'factorial is only defined for integers.'
        return none
    elif n<0:
        print 'factorial is not defined for negative words'
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)
def factorail(n):
    space=' '*(4 * n)
    print space,'factorial',n
    if n==0:
        print space,'returning 1'
        return 1
    else:
        recurse=factorial(n-1)
        result=n * recurse
        print space,'returnin',result
        return result
def b(z):
    prod=a(z,z)
    print z,prod
    return prod
def a(x,y):
    x=x+1
    return x*y
def c(x,y,z):
    total =x+y+z
    square =b(total)**2
    return square
x=1
y=x+1
print c(x,y+3,x+y)
def ackermann(m,n):
    """comptes the ackerman function A(m,n)n.m:non-neative integers"""
    if m==0:
        return n+1
    if n==0:
        return ackermann(m-1,1)
    return ackermann(m-1,ackermann(m,n-1))
print ackermann(3,4)
