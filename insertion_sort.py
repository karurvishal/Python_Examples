def insertion_sort(list):
    for index in range (1,len(list)): #not taking first element 
        value = list[index]   # now 1 is value
        i = index -1 #to push the previoue element
        while i >=0:
            if value < list[i]:
                list[i+1] = list[i]
                list [i] = value
                i = i-1
            else:
                break


a = [9,1,3,8,6,10,26,4]
insertion_sort(a)
print(a)