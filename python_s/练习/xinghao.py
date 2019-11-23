line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

a, *bs, c, d, e = line.split(":")
print(a)
print(bs)
print(c)
print(d)
print(e)
s=line.split(":")
print(s)
