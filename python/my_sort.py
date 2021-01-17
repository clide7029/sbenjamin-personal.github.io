def sort(list):
    for n in range(len(list)):
        min = n
        for m in range(n+1, len(list)):
            if(list[m] < list[min]):
                min = m
        list[min], list[n] = list[n], list[min]
    return list

print(sort([4,3,2,1]))