l = [6,5,3,1,8,7,2,4]

def selection_sort(l):
	for i in range(len(l)):
		min_index = i
		j = i +1
		while j < len(l):
			if l[j] < l[min_index]:
				min_index = j
			j+=1
		temp = l[i]
		l[i] = l[min_index]
		l[min_index] = temp
			
	return l

print(selection_sort(l)) # prints [1,2,3,4,5,6,7,8]
