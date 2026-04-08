from datetime import datetime as dt



ip = input()
a = ip.split()
b = ip.split('.')
d,m,y = (a if len(a) == 3 else b)
d,m,y = list(map(lambda x: int(x[1:]) if x[0] =='0' else int(x), [d,m,y]))

try:
    n = dt.timestamp(dt(2000, m, d))
    s = dt.timestamp(dt(2000, 1, 1))
except ValueError:
    print('WRONG!')
else:
    print(round((n-s)/3600//24+1, 0))