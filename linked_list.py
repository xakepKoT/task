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