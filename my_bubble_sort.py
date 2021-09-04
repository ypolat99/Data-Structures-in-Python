l = [6,5,3,1,8,7,2,4]

def bubble_sort(l):
	for i in range(len(l)):
		for j in range(len(l)-1):
			if l[j] > l[j+1]:
				temp = l[j]
				l[j] = l[j+1]
				l[j+1] = temp
	return l

print(bubble_sort(l)) # prints [1,2,3,4,5,6,7,8]
