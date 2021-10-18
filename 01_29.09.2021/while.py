def even_num(n):
    i = 2
    array = list()
    while i <= n:
        array.append(i)
        i += 2
    return array

print(even_num(50))