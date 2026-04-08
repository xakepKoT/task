f = int(input())
def func(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return func(n-1)+func(n-2)

print(func(f))

q1,q2 = 0,1
fib = 0
for i in range(f):
    fib = q1+q2
    q1=q2
    q2=fib
print(q1)