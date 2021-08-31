class my_array:
	def __init__(self):
		self.len = 0
		self.data = {}
	def get(self, index):
		if index <= self.len -1:
			return self.data[index]
	def push(self, item):
		self.data[self.len] = item
		self.len+=1
		return self.len
	def pop(self):
		last_item = self.data[self.len-1]
		del self.data[self.len-1]
		self.len-=1
		return last_item
	def delete(self, index):
		item = self.data[index]
		self.shift_items(index)
		return item
		
	def shift_items(self, index):
		for i in range(index, self.len-1):
			self.data[i] = self.data[i+1]
		del self.data[self.len-1]
		self.len-=1
   
  def leng(self):
    return self.len

		
		
		

# Some Test Code			

a = my_array()
print(a.get(0)) # Prints None
a.push(0)
a.push("11")
print(a.get(1)) # Prints "11"
print(a.pop())  # Prints "11"
print(a.len)	#Prints 1
a.push(1)
a.push("2")
a.push("Three")
a.push("Cuatro")
print(a.data)
print(a.delete(2)) # Prints 2
print(a.leng()) # Prints 4
