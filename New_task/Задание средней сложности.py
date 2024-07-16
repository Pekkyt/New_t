def four(n):
    s = ''
    while n > 0:
        s += str(n%4)
        n//=4
    return s[::-1]
sp = []
for n in range(1,201):
    n4 = four(n)
    n4 = n4.replace('1', 'a')
    n4 = n4.replace('0','1')
    n4 = n4.replace('2','b')
    n4 = n4.replace('a','2')
    n4 = n4.replace('3','c')
    n4 = n4.replace('b','3')
    n4 = n4.replace('c','0')
    n4 += '1'
    if n4[0] == '0':
        n4 = '1' + n4
    else:
        n4 = n4 + '10'
    r = n4
    if r.count('0') == 2 and r == r[::-1]:
        sp.append(r)
print(int(max(sp), 4))