lis = [11, 2, 23, 4, 33, 5]

print(lis)

for i in range(len(lis)):
    count = 0
    for j in range(i):

        if lis[i] < lis[j]:
            lis[i], lis[j] = lis[j], lis[i]
            count += 1

print(lis)
print(count)

print(lis[:2])
print(lis[:-1])
print(lis[:])
print(lis[-1:])
print(lis[::-1])

a = 10
b = 20
s = a if a > b else b
print(s)
