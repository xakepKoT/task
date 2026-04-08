t = input()
qu = [0]
ab = '({[]})'
a = '[{('
b = ']})'
for i in t:
    if i in a:
        qu.append(i)
    elif i in b:
        if a.find(qu[-1]) == b.find(i):
            qu.pop(-1)
        else:
            print('Wrong')
            break
if qu == [0]:
    print('Right')