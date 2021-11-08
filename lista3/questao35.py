def search(array, start, lenght, element):
    middle = int((lenght + start) / 2)
    
    if(start > lenght):
        return -1
    if array[middle] == element:
        return middle
    else:
        if(array[middle] < element):
            return search(array, middle + 1, lenght, element)
        else:
            return search(array, start, middle - 1, element)


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
index = search(array, 0, len(array), 10)
if(index == -1):
    print('Element not found')
else:
    print('The element is in the position %d of the array' % index)