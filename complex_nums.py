from math import atan, cos, sin, pi

class complex_num:
    pass


def to_e_show(c,i):
    r,f = (c**2+i**2)**0.5, atan(i/c) if c!=0 else pi/2
    return [r, f, f'{c}+{i}i'+f'  {r}*e^({f}i)' if i>=0 else f'{c}{i}i'+f'  {r}*e^({f}i)']

def to_norm_show(r,f):
    c, i = round(r*cos(f),10), round(r*sin(f),10)
    if c ==0.0:
        c=0.0
    if i == 0.0:
        i=0.0
    k=('+' if i >= 0 else '')
    return [c, i, f'{c}{k}{i}i'+f'  {r}*e^({f}i)' if i>=0 else f'{c}{i}i'+f'  {r}*e^(i{f}i)' if r!=0 else '0.0']

def read(x):
    ans = complex_num()
    if '-' in x or '+' in x:
        p=max(x.rfind('+'), x.rfind('-'))
        minu = ('-' if x[p]=='-' else '+')
        #t=(x.split('-') if '-' in x else x.split('+'))
        t=[x[:p], minu+x[p+1:]]
    elif 'i' in x:
        t=['0',x]
    else:
        t= [x,'0']
    t[1] = t[1].replace('i','',1)
    ans.c = int(t[0]) #целое
    ans.i = int(t[1]) #комплексное
    func = to_e_show(ans.c,ans.i)
    ans.r = func[0] #модуль
    ans.f = func[1] #угол
    ans.show = func[2]
    return ans



def summ(a: list):
    ans = complex_num()
    ans.c=0
    ans.i=0
    for j in a:
        if type(j) == list:
            j=j[0]
        ans.c += j.c
        ans.i += j.i
    func = to_e_show(ans.c,ans.i)
    ans.r = func[0]
    ans.f = func[1]
    ans.show = func[2]
    return ans

def mult(a:list):
    ans = complex_num()
    ans.r=1
    ans.f=0
    for j in a:
        if type(j) == list:
            j=j[0]
        ans.r *= j.r
        ans.f += j.f
    func = to_norm_show(ans.r, ans.f)
    ans.c=func[0]
    ans.i=func[1]
    ans.show = func[2]
    return ans

def pow(a:complex_num, st:float):
    ans = complex_num()
    ans.r = a.r**st
    ans.f = a.f * st
    func = to_norm_show(ans.r, ans.f)
    ans.c = func[0]
    ans.i = func[1]
    ans.show = func[2]
    return ans

def demult(a:complex_num, b:complex_num):
    ans = complex_num()
    if b.r == 0:
        return 'BAD INPUT'
    ans.r = a.r / b.r
    ans.f = a.f-b.f
    func = to_norm_show(ans.r, ans.f)
    ans.c = func[0]
    ans.i = func[1]
    ans.show = func[2]
    return ans