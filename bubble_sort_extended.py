def bubble_sort(elements,key=None):
	size = len(elements)
	for i in range (size-1):
		swapped = False
		for j in range(size-1):
			if elements[j][key] > elements[j+1][key] :
				temp = elements[j]
				elements[j] = elements[j+1]
				elements[j+1] = temp
				swapped = True
		if not swapped:
			break
if __name__ == '__main__':
    elements = [
        { 'name': 'vishal',   'transaction_amount': 1110, 'device': 'iphone-10'},
        { 'name': 'vinayak', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'renuka',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'karur',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    bubble_sort(elements, key='transaction_amount')
    print(elements)