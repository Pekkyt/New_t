def pyt(n):
    s = ''
    while n > 0:
        s += str(n % 5)
        n //= 5
    return s[::-1]
sp = []
for N in range(11,1000):
    n5 = pyt(N)
    n5 = n5[:-1]
    l = len(n5)
    su = sum([int(i) for i in n5])
    newch = int(su // l)
    n5 = n5 + pyt(newch)
    r = int(n5,5)
    if r % 5 == 0:
        sp.append(N)
print(max(sp))