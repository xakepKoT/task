from random import random

ans = 0
counter = 999999
for i in range(counter):
    x = random()
    y = random()
    if x**2+y**2 <= 1:
        ans+=1
print(ans/counter*4)