class slist:
    next=None
    data=None

def append(el:slist, new):
    ans=el
    l = slist()
    while el.next != None:
        el = el.next
    l.data=new
    l.next=None
    el.next = l
    return ans

def get(el:slist, num:int):
    for i in range(num):
        el = el.next
    return el.data

def remove(el:slist, num):
    for i in range(num-1):
        el = el.next
    t = el.next
    if t!=None:
        el=t
    return el

def length(el:slist):
    ans=0
    while el!=None:
        ans+=1
        el=el.next
    return ans

def prepend(el: slist, new):
    l = slist()
    l.data = new
    l.next = el
    return l

def get_last(el:slist):
    if el == None:
        return None
    while el.next != None:
        el = el.next
    return el.data

def find(el:slist, needle):
    if el == None:
        return -1
    ind = 0
    while el.data != needle and el!=None:
        el = el.next
        ind+=1
    if el.data == needle:
        return ind
    else:
        return -1

def remove_first(el:slist, needle):
    if el == None:
        return el
    start = el
    old = None
    while el.data != needle and el!=None:
        old = el
        el = el.next
    if el.data == needle:
        old.next = el.next
    return start

def remove_all(el:slist, needle):
    start = el
    while el != None:
        old = el
        el = el.next
        if el.data == needle:
            old.next = el.next
    return start

def copy(el: slist):
    start = slist()
    start.data = el.data
    start.next = el.next
    while el != None:
        el=el.next
        middle = slist()
        middle.data = el.data
        middle.next=el.next
    return start

def concat(el1:slist, el2:slist):
    if el1 == None:
        return el2
    ans=el1
    while el1.next != None:
        el1=el1.next
    el1.next = el2
    return ans


def foreach(el:slist, f):
    while el != None:
        f(el.data)
        el=el.next

def find_custom(el, f):
    ind=0
    while el != None:
        if f(el):
            return el.data, ind
        el = el.next
        ind+=1
    return None, -1

def from_list(l):
    ans = None
    old=slist()
    for i in range(len(l)-1):
        el=old
        el.data = l[i]
        old=slist()
        old.data = l[i+1]
        el.next=old
        if i == 0:
            ans = el
    return ans

def to_list(el):
    ans=[]
    while el != None:
        ans.append(el.data)
        el=el.next
    return ans