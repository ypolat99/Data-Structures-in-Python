class Node:
	def __init__(self, value):
		self.val = value
		self.next = None
		

class Queue:
	def __init__(self):
		self.first = None
		self.last = None
		self.len = 0
		
	def peek(self):
		#returns the value of the first item in if empty returns None
		if self.len == 0:
			return
		return self.first.val

	def enqueue(self, value):
		new_node = Node(value)
		if self.len == 0:
			self.first = new_node
			self.last = new_node
		else:
			self.last.next = new_node 
			self.last = new_node 
			
		self.len+=1
		return self.len

	def dequeue(self):
		if self.len == 0:
			return None
		elif self.len ==1:
			self.last = None
		item = self.first.val
		self.first = self.first.next
		self.len-=1
		return item



# Test Cases

q = Queue()
print(q.enqueue(10)) #prints 1
print(q.enqueue(20)) #prints 2
print(q.enqueue(30)) #prints 3 
print(q.enqueue(40)) #prints 4
 
print(q.peek()) #prints 10
print(q.dequeue()) #prints 10
print(q.len) #prints 3


