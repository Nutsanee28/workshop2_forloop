table = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for table in table:
    print("[", table, "]")
    for num in number:
        print(table, " * ", num, " : ", table * num)
    print("------------")
