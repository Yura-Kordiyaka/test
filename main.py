def result(my_list):
    for j in range(0, len(my_list)):
        if my_list[j] < 5:
            print(my_list[j])


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
result(a)
