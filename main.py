# x = int(input("input your first number ="))
# y = int(input("input second number = "))
# print("your answer ", x + y)
#

name = str(input("input your data : "))
for j in range(0, len(name)):
    print(name[j] * 2,end='')
# a = []
# k = 0
# while k < 4:
#     a.append(int(input("input your number : ")))
#     k = k + 1
# b = a[0]
# c = a[0]
# for x in range(1, len(a)):
#     if b < a[x]:
#         b = a[x]
#     elif c > a[x]:
#         c = a[x]
#
# print("max = ", b, "min = ", c)
# print(max(a))
# print(min(a))
f = str(input("input your data : "))
print(f[::-1])
