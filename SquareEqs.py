a, b, c = list(map(float, input('a, b, c: ').split()))
if a == 0 and b==0 and c==0:
    print('беск. решений')
elif a == 0 and b==0 and c != 0:
    print('нет решений')
elif a == 0:
    print(c/b)
else:
    D = b ** 2 - 4 * a * c
    print(*list(set([(-b-D**(0.5))/(2*a),(-b+D**(0.5))/(2*a)])))