# Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 20:42:06)
# [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
# Type "copyright", "credits" or "license()" for more information.

def selection_sort(arr):
    """
    Parameters
    __________
    arr : list
        Unsorted array to be sorted

    >>> unsorted_array = [64, 25, 12, 22, 11]
    >>> sorted_array = selection_sort(unsorted_array)
    >>> sorted_array
    [11, 12, 22, 25, 64]
    """
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
