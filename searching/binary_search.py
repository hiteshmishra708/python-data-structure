def binary_search(arr, min, max, element):
    mid = (min + max) // 2
    if max >= min:
        if (arr[mid] == element):
            return mid
        elif (arr[mid] > element):
            return binary_search(arr, min, mid - 1, element)
        else:
            return binary_search(arr, mid + 1, max, element)
    else:
        print('Element is not in list')
        return -1
arr = [1, 20, 33, 44, 78, 99]
print(binary_search(arr, 0, len(arr), 44))
