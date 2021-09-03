class Node:
	def __init__(self, value):
		self.val = value
		self.next = None

class Stack:
	def __init__(self):
		self.top = None
		self.bottom = None
		self.len = 0
		
	def peek(self):
		#returns the value of the top item
		return self.top.val
		
	def push(self, value):
		#pushes value and returns the new stack lenght
		new_node = Node(value)
		if self.len == 0:
			self.top = new_node
			self.bottom = new_node
		else:
			old_top = self.top
			self.top = new_node
			self.top.next = old_top
			
		self.len +=1
		return self.len

	def pop(self):
		#pops the last element from the stack and return its value
		if self.len == 0:
			return None
		old_top = self.top
		self.top = self.top.next
		self.len +=1
		return old_top.val
		
	def is_empty(self):
		#returns true if the stack is empty
		return self.lenn == 0


#Test Cases

s = Stack()
print(s.push(10)) #prints 1
print(s.top.val) #prints 10
print(s.bottom.val) #prints 10
print(s.push(20)) #prints 2
print(s.top.val) #prints 20
print(s.bottom.val) #prints 10
print(s.peek()) #prints 20
print(s.push(30)) #prints 3
print(s.pop()) #prints 30


		
