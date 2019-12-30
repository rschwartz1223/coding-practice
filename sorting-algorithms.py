# Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 20:42:06)
# [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
# Type "copyright", "credits" or "license()" for more information.

def selection_sort(arr):
    """
    Selection sort traverses an unsorted array and switches the minimum element
    with the first element of the array. It then traverses the remaining
    unsorted portion and repeats this process.

    Time complexity: O(n^2)
    Space complexity: O(1)

    Parameters
    __________
    arr : list
        Unsorted array to be sorted

    >>> unsorted_array = [64, 25, 12, 22, 11]
    >>> sorted_array = selection_sort(unsorted_array)
    >>> sorted_array
    [11, 12, 22, 25, 64]
    """
    if len(arr) == 1:
        return arr
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def bubble_sort(arr):
    """
    Bubble sort repeatedly swaps the adjacent elements of an array if they are
    in the wrong order.

    Time complexity: O(n^2)
    Space complexity: O(1)

    Parameters
    __________
    arr : list
        Unsorted array to be sorted

    >>> unsorted_array = [64, 25, 12, 22, 11]
    >>> sorted_array = bubble_sort(unsorted_array)
    >>> sorted_array
    [11, 12, 22, 25, 64]
    """
    if len(arr) == 1:
        return arr
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
    return arr

def merge_sort(arr):
    """
    Merge sort divides unsorted array into two halves, recursively calls itself
    on the two halves, and merges the two sorted halves.

    Time complexity: O(n*log(n))
    Space complexity: O(n)

    Parameters
    __________
    arr : list
        Unsorted array to be sorted

    >>> unsorted_array = [64, 25, 12, 22, 11]
    >>> sorted_array = merge_sort(unsorted_array)
    >>> sorted_array
    [11, 12, 22, 25, 64]
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

if __name__ == '__main__':
    import doctest
    arr = [64, 25, 12, 22, 11]
    doctest.testmod()
