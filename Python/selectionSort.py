arr = [8, 3, 5, 6, 1, 0, 4]


def selectionSort(arr):
    for i in range(len(arr) - 1):
        minidx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minidx]:
                minidx = j

        # print("*"*50, "\nSwapping", arr[i], arr[minidx])
        arr[i], arr[minidx] = arr[minidx], arr[i]
        # print("arr:", arr)


selectionSort(arr)
print(arr)
