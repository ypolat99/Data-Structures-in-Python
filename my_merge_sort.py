l = [1,5,2,8,5,8,3,3,10,11]

def merge(arr, l, mid, r):
	n1 = mid -l +1
	n2 = r - mid

	#cretae temp arrays 
	L = [0 for i in range(n1)]
	R = [0 for i in range(n2)]

	#copy data to L and R
	for i in range(0, n1):
		L[i] = arr[l+i]
		
	for i in range(0, n2):
		R[i] = arr[mid+1+i]

	# Merge temp arrays back
	i=0
	j=0
	k=l
	while i <n1 and j < n2:
		if L[i] < R[j]:
			arr[k] = L[i]
			i+=1
		else:
			arr[k] = R[j]
			j+=1
		k+=1

	# Copy the remaining elements to arr
	while i < n1:
		arr[k] = L[i]
		i+=1
		k+=1
		
	while i < n1:
		arr[k] = R[j]
		j+=1
		k+=1



def merge_sort(arr, l, r):
	if l<r:
		mid = (l+r)//2
		merge_sort(arr, l, mid)
		merge_sort(arr, mid+1, r)
		merge(arr, l, mid, r)
	return arr


		


merge_sort(l, 0, len(l)-1)
print(merge_sort(l, 0, len(l)-1)) # prints [1,2,3,3,5,5,8,8,10,11]
