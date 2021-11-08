def max_point(array, start, end):
    if start == end:
        return array[start]

    middle = int((end + start) / 2)
    if array[middle] < array[middle + 1]:
        return max_point(array, middle + 1, end)
    else:
        return max_point(array, start, middle)
        

array = [2, 5, 7, 18, 21, 27, 30, 31, 25, 14, 9]
point = max_point(array, 0, len(array))
print('The maximum point p of the array is: %d' %point)