arr = [8, 3, 5, 6, 1, 0, 4]


def insertionSort(arr):

    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


insertionSort(arr)
print(arr)
