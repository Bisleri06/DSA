# Selection sort in Python
# time complexity O(n*n)
#sorting by finding min_index
def selectionSort(array, size):
	
	for i in range(size):
		for j in range(i + 1, size):
			# select the minimum element in every iteration
			if array[j] < array[i]:
				min_index = j
		# swapping the elements to sort the array
		(array[i], array[min_index]) = (array[min_index], array[i])

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)

#HactoberFest
