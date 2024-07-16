import string
alf = string.ascii_uppercase
print(alf)
fift_alf = '0123456789ABCDE'
def fift(n):
    s = ''
    while n > 0:
        s += str(fift_alf[n%15])
        n //= 15
    return s[::-1]
c = []
for N in range(1401, 4000):
    n15 = fift(N)
    if '8' in n15:
        n15 = n15.replace('8', 'D')
    n2 = bin(int(n15, 15))[2:]
    if n2[0] != '0':
        if len(n2) < 10:
            n2 = n2.ljust(10,'0')
        else:
            n2 = '1' + n2
    r = int(n2,2)
    if str(r).count('8') == 2 and str(r).count('2') == 1:
        c.append(N)
print(min(c))
