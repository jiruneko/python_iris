a = [1, 2, "Hello"]
print(a)

b = [1, 2, "Hello", [3, 4]]
print(b)

c = []
print(c)

d = [1, 2, "Hello"]
print(d[0])
print(d[-1])

e = [1, 2, "Hello", "Bye"]
print(e[0:2])

b[0:2] = [5, 6]
print(b)

b.append(3)
print(b)

b.remove('Hello')
print(b)
