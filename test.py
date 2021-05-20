"""
a=list(range(0,10,2))
print(a)
b=list(range(9,0,-1))
print(b)

stack=[1,2,3]
stack.append(4)
print(stack)
stack.pop()
stack.remove(1)
print(stack)
"""

a=list(range(0,20,2))
print(a[:6])
b=a[:]
b[1]=5
b[5:]=[40,41,42,43,44]
a[:0]=[-1]
a.insert(0,7)
c=[1,b,9]
print(a)
print(c)
t=1,2,3
print(t)

def isPrim(nr):
    div=2
    while div<nr and nr % div>0:
        div=div+1
    return div>=nr
print(isPrim(7))

def Funk(a):
    print('Locals',locals())
    print('before a=',str(a))
    a=4
    print('after a=', str(a))

Funk(0)



