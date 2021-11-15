# Insertion sort
def insertionSort(arr):
  """
  :param arr: an array to be sorted
  :returns: nothing
  """
  # Traverse through 1 to len(arr)
  for i in range(1, len(arr)):

    key = arr[i]

    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    j = i-1
    while j >=0 and key < arr[j] :
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

# pytest method to check if insertion sort method sorts correctly
def test_sortsCorrectly():
    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    testarr = [5, 6, 11, 12, 13]
    assert arr == testarr



#print ("Sorted array is:")
#for i in range(len(arr)):
#  print ("%d" %arr[i])
