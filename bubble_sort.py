def bubble_sort(arr):
    for i in range (0,len(arr)):
        for j in range(0,len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j + 1] = arr[j + 1],arr[j]

    return arr


list = [2,4,1,7,2,8,3,7,4]
print("Before bubble sort:",list)
bubble_sort(list)
print("After bubble sort:",list)

