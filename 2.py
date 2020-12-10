n = int(input('Enter n = '))
a = [[0 if (j + i) % 2 == 1 else 1 for j in range(n)]for i in range(n)]
for el in a:
    print(el)