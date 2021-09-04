l = [1,5,2,8,5,8,3,3,10,11]

def insertion_sort(l):
	for i in range(1,len(l)):
		key = l[i]
		j = i-1
		# nove things greater than key to one positions ahead
		while j >=0 and key < l[j]:
			l[j+1] = l[j]
			j-=1
		#put key to correct place
		l[j+1] =key
			
	return l

print(insertion_sort(l)) # prints [1,2,3,4,5,6,7,8]
