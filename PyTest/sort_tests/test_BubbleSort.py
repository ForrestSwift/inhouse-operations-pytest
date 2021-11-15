# Bubble Sort
def bubbleSort(arr):
    """
    :param arr: an array to be sorted
    :returns: nothing
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one
        # time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Driver code to test above

# pytest method to check if bubble sort method sorts correctly
def test_sortsCorrectly():
    # sets up array to be sorted
    arr = [54, 22, 31, 42, 60, 9, 80]
    # sorts array
    bubbleSort(arr)
    # correctly sorted array
    testarr = [9, 22, 31, 42, 54, 60, 80]
    assert arr == testarr


# print ("Sorted array is:")
# for i in range(len(arr)):
#  print ("% d" % arr[i]),
