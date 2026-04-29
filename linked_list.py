class slist:
    pass

def append(el:slist, new):
    l = slist()
    while el.next != None:
        el = el.next
    el.next = l
    l.data=new
    l.next=None

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

def len(el:slist):
    ans=0
    while el.next!=None:
        ans+=1
    return ans

def prepend(el: slist, new):
    l = slist()
    l.data = new
    l.next = el

def get_last(el:slist):
    while el.next != None:
        el = el.next
    return el.data

def find(el:slist, needle):
    ind = 0
    while el.data != needle and el!=None:
        el = el.next
    if el.data == needle:
        return ind
    else:
        return -1

def remove_first(el:slist, needle):
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
    old = None
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
    pass