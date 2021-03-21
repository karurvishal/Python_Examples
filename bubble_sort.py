def bubble(my_list):
	size = len(my_list)
	print(f"size of list is {size}")
	for j in range(size-1):
		Swapped = False
		for i in range(size-1):
			if my_list[i]>my_list[i+1] :
				temp = my_list[i]
				my_list[i] = my_list[i+1]
				my_list[i+1] = temp
				Swapped = True
		if Swapped == False:
			break
	print(my_list)
			
if __name__ == '__main__':
	my_list = [1,2,3,4,5,6,9,1]
	bubble(my_list)