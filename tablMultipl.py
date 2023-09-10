def tabl_multipl(n):
    if not isinstance(n, int) or n < 1 or  n > 9:
        print("Ошибка: переменная должна быть от 1 до 9")
    else:
        for i in range(n+1):
            for j in range(1, 10):
                print(i,"*",j,"=",i*j)
            print()    


tabl_multipl(8)