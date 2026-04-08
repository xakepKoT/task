t = list(map(float, input().split()))

mini = t[0]
maxi=t[0]
summi = 0
for i in t:
    if i < mini:
        mini = i
    if i > maxi:
        maxi=i
    summi += i