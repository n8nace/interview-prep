def move_duplicates(arr, m)
    new_arr = []
    countM = 0
    for num in arr:
        if num == m:
            countM +=0
        else:
            new_arr.append(num)
#    for u in unique:
#        new_arr.append(u)
    for i in range(countM):
        new_arr.append(m)
    return new_arr
