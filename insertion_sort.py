def insertion_sort(apple):
    for i in range (1,len(apple)):
        key = apple[i]
        j = i - 1 
        while j >= 0 and apple[j] > key:
            apple[j + 1] = apple[j]
            j -=1
            apple[j + 1] = key

    return apple


# using the insertion sort algorithm:
list = [2,4,1,7,2,8,3,7,4]
print("Before instertion sort:",list)
insertion_sort(list)
print("After insertion sort:",list)
