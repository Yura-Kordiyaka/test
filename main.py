#week3task3
def remove_coma(a):
    for j in a:
        if j == ",":
            a.remove(j)


def add_element(a, c):
    for j in range(0, len(c)):
        a.append(c[j])


t = open("test.txt", "r")
w = open("write.txt", "w")
f = t.read()
d = []
z = ()
add_element(d, f)
remove_coma(d)
z = list(z)
z = d
z = tuple(z)
print(d)
print(z)
for j in d:
    w.write(j+" ")
for j in z:
    w.write(j+" ")


