a=[1,2,3]
b=[4,6,5]
c=a+b
print(c)

t=['a','b','c','d','e','f']
t[1:3]
t[:4]
t[3:]

def only_upper(t):
    res=[]
    for s in t:
        if s.super():
            res.append(s)
            return res

t=['a','b','c']
x=t.pop(1)
print(t)
print(x)

t=['a','b','c']
del t[1]
print(t)

s='spam'
t=list(s)
print(t)

s='pining for the fjords'
t=s.split()
print(t)

s='spam-spam-spam'
delimiter='-'
s.split(delimiter)

def delete_head(t):
    del t[0]
    letters=['a','b','c']
    delete_hjead(letters)
    print(letters)

t1=[1,2]
t2=t1.append(3)
print(t1)
print(t2)
t3=t1+[4]
print(t3)

def historam(s):
    d=dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
            return d


h=histogram('parrot')
print_hist(h)

h=histogram('parrot')
k=reverse_lookup(h,2)
print(k)

def invert_dict(d):
    inverse=dict()
    for key in d:
        val=d[key]
        if val not in inverse:
            inverse[val]=[key]
        else:
            inverse[val].append(key)
            return inverse

known={0:0,1:1}
def fibonacci(n):
    if n in known:
        return known[n]
    res=fibonacci(n-1)+fibonacci(n-2)
    known[n]=res
    return res

addr='monty@python.org'
uname,domain=addr.split('@')
print(uname)
print(domain)

t=divmod(7,3)
print(t)

quot,rem=divmood(7,3)
 print()quot
 print(rem)

 t=(7,3)
 divmod(t)         #type error
 divmod(*t)

 s='a,b,c'
 t=[1,2,3]
 zip(s,t)

 t=[('a',0),('b',1),('c',2)]
 for letter,number in t:
     print(number,letter)

def has_math(t1,t2):
    for x,y in zip(t1,t2):
        if x==y:
            return True
        return False