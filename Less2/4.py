a = 14 # 140732770231624
b = 14
c = a

print(id(a))
print(id(b))
print(id(c))

d = 8845 # 2264896943024
e = 8845

print(id(d))
print(id(e))

if d is e:
    print("")
if id(d) == id(e):
    print("")

a = 1235 ** 404
print(a)