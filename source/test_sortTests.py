# Python program for PyTest testing of bubblesort,
# insertionsort, and quicksort python functions

# These functions create an unsorted array, then
# sort them through their respective sort functions.
# It then checks against a properly sorted array
# of the same contents.

# Imports the sort functions from the other Py files
from BubbleSort import bubbleSort
from InsertionSort import insertionSort
from QuickSort import quickSort

# PyTest to check if bubble sort works properly
def test_bubbleSort():
    # sets up array to be sorted
    arr = [7, 5, 1, 3, 4, 8, 2, 6]
    # sorts array
    bubbleSort(arr)
    # correctly sorted array
    testarr = [1, 2, 3, 4, 5, 6, 7, 8]
    # checks if they are equal
    assert arr == testarr

# PyTest to check if insertion sort works properly
def test_insertionSort():
    # sets up array to be sorted
    arr = [7, 5, 1, 3, 4, 8, 2, 6]
    # sorts array
    insertionSort(arr)
    # correctly sorted array
    testarr = [1, 2, 3, 4, 5, 6, 7, 8]
    # checks if they are equal
    assert arr == testarr

# PyTest to check if quick sort works properly
def test_quickSort():
    # sets up array to be sorted
    arr = [7, 5, 1, 3, 4, 8, 2, 6]
    # sorts array
    n = len(arr)
    quickSort(arr, 0, n - 1)
    # correctly sorted array
    testarr = [1, 2, 3, 4, 5, 6, 7, 8]
    # checks if they are equal
    assert arr == testarr