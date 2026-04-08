def ke(x):
    return int(x)

def sortStep(s, f):
    lim = len(s)
    if lim<=1:
        return s
    chosen = s[0]
    i = 1
    j = 1
    while i+j <= lim:
        if f(s[i])>=f(chosen):
            if f(s[lim-j]) <= f(chosen):
                s[i], s[lim-j] = s[lim-j], s[i]
                i+=1
            j+=1
        else:
            i+=1
    s[0], s[i-1] = s[i-1], s[0]
    return [sortStep(s[:i-1], f)]+[s[i-1]]+[sortStep(s[i:],f)]


res=[]
def readr(t):
    if type(t) == tuple or type(t) == list:
        return [readr(i) for i in t]
    else:
        res.append(t)
        #print(t, end=' ')
        return t


def do(l,k):
    res.clear()
    readr(sortStep(l, k))
    return res


def start():
    li = list(map(int, input().split()))
    return do(li, ke)