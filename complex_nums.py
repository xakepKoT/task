from math import atan, cos, sin

class complex_num:
    pass


def read(x):
    t=None
    if '-' in x or '+' in x:
        t=x.split('-') if '-' in x else x.split('+')
    elif 'i' in x:
        t=['0',x]
    else:
        t= [x,'0']
    t[1] = t[1].replace('i','',1)
    return [int(t[0]), int(t[1])]


def parts(x:complex_num):
    return [x[0], x[1]]


def to_norm(r,f):
    return [r*cos(f),r*sin(f)]


def to_e(x:complex_num):
    p=parts(x)
    r = ((p[0])**2+(p[1])**2)**0.5
    f = atan(p[0]/p[1])
    return [r, f]


def summ(a: list):
    return

print(read('8+9i'))