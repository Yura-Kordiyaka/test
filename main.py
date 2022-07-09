# week 3 task 1
def result(a, b):
    x = 0
    i = 0
    suma = 0
    if a > b:
        x = b
        i = b
        while i <= a:
            suma = suma + x
            x = x + 1
            i = i + 1
    if b > a:
        x = a
        i = a
        while i <= b:
            suma = suma + x
            x = x + 1
            i = i + 1
    return suma


c = int(input("input your data : "))
x = int(input("input your data : "))
print(result(x, c))
