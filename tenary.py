nilai = 70
hasil = 'A' if nilai > 75 else 'B' if nilai > 60 else 'C'
print(hasil)

a = True
b = False
print(10*"=")
print(a and b, " ", a or b, " ", not a, " ", not b)

c = 5
d = 5
e = [1, 2, 3]
f = e
g = e.copy()
h = (1, 2, 3) #tuple
i = (1, 2, 3)
j = {"name":"doe","age":30}
print(c is d, e is f, e is g, h is i, 1 in e)
print(j.keys)