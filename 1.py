n = list(input('введіть число:'))
length = int(len(n) / 2)
p = 0
for i in range(length):
    if n[i] != n[-(i+1)]:
        p = 1
if p == 0:
    print('число паліндром')
else:
    print('число не є паліндромом')