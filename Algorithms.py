def bubbleSort(array):
    n = len(array)
    for i in range(len(array)):
        swapped = False

        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

        if swapped == False:
            break

    return array


print('This is from bubble sort')
arr = [64, 34, 25, 12, 22, 11, 90]

print(bubbleSort(arr))


def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i] 

        j = i - 1 

        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


print('This is from insertion sort')
arr = [64, 34, 25, 12, 22, 11, 90]
print(insertionSort(arr))
