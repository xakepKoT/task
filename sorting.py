st = input().split()
l1 = [0,0,0,0,0,0,0,0,0,0]
l2 = [0]
l3 = [4,6,3,8,5,0,8,1234,56,6598,4,6,342,374,976,4,5,7,8,1,3,0,4,245424]*999
l4 = [1,0]
l5 = [2,4,5,2,4,5,2,4,5,2,4,5,2,4,5,2,4,5,2,4,5]


def equiz(a):
    return int(a)


def sort_step(m1,m2,f):
    res = []
    a1=0
    a2=0
    for i in range(len(m1)+len(m2)):
        if a2 == len(m2) or a1 < len(m1) and f(m1[a1])<=f(m2[a2]):
            res.append(m1[a1])
            a1 += 1
        else:
            res.append(m2[a2])
            a2 += 1
    return res


def split_step(m):
    if len(m)==1:
        return m
    return sort_step(split_step(m[:len(m)//2]), split_step(m[len(m)//2:]), equiz)


u=split_step(st)
assert split_step(l1) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert split_step(l2) == [0]
o=split_step(l3)
assert all(o[i] <= o[i+1] for i in range(len(o)-1))
assert split_step(l4) == [0,1]
assert split_step(l5) == [2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
print(*u)