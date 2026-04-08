from math import floor, sqrt

def check(x):
    for j in range(3,floor(sqrt(x))+1):
        if x%j == 0:
            return False
    return True

c = int(input())
if c >= 2:
    print(2, end=' ')
for i in range(3, c+1, 2):
    if check(i):
        print(i, end=' ')