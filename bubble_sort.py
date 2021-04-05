def bubble_sort(elements):
	size = len(elements)
	for i in range (size-1):
		swapped = False
		for j in range (size-1-i):
			if elements[j] > elements[j+1]:
				temp = elements[j]
				elements[j] = elements[j+1]
				elements[j+1] = temp
				swapped = True
		if not swapped:
			break

if __name__ == '__main__':
	elements = [3,8,1,0,81,6,87,9,29,76]
	bubble_sort(elements)
	print(elements)