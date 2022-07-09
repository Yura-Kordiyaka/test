#week3task2
def result(a):
    b = a[::-1]
    i = 0
    d = len(a)
    for j in b:
        if a == b:
            i = i + 1
    if i == d:
        print("this is palindrome")
    else:
        print("it is not a palindrome")


c = str(input("input your data : "))
result(c)
