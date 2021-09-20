def linear_search(arr, element):
    found = False
    pos = 0
    max_pos = len(arr)

    if max_pos == 0:
        print('List is empty')
    else:
        while(pos < max_pos):
            if arr[pos] == element:
                found = True
                break
            pos += 1
        if found:
            return pos
    return -1

print(linear_search([1, 5, 2, 3, 6, 8, 20], 20))