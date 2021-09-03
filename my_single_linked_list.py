class Node:
	def __init__(self, value = None):
		self.val = value
		self.next = None

class LinkedList:
	def __init__(self, value):
		self.head = Node(value)
		self.tail = self.head
		self.len=1
		
	def insert_start(self, value):
		new_node = Node(value)
		new_node.next = self.head
		self.head = new_node
		self.len += 1

	def insert_end(self, value):
		new_node = Node(value)
		self.tail.next = new_node
		self.tail = new_node
		self.len+=1

	def print_list(self):
		cur = self.head
		while cur:
			print(cur.val)
			cur = cur.next

	def insert(self, index, value):
		if index == 0:
			self.insert_start(value)
			return
		elif index >= self.len:
			self.insert_end(value)
			return
		cur = self.head
		count =0
		while count <index-1:  #insert 2
			cur = cur.next # cur idx 1
			count+=1

		new_node = Node(value)
		new_node.next = cur.next
		cur.next = new_node
		self.len+=1

	def remove(self, index):
		count = 0
		cur = self.head
		while count < index -1: #remove 2
			count+=1  # count 1
			cur = cur.next  # 5 
		to_delete = cur.next
		cur.next = to_delete.next
		to_delete.next = None
		self.len -=1
				
	def get_len(self):
		return self.len
		
		
		

# Test Cases

l = LinkedList(5)
print(l.head.val) #prints 5
print(l.tail.val) #prints 5
print("----")
l.insert_start(4) 
print(l.head.val) #prints 4
print(l.tail.val) #prints 5
print("----")
l.insert_end(6) 
l.insert_end(7) 
print(l.tail.val) #prints 7
print("----")

l.insert(2,5.5)
l.print_list() #prints 4,5,5.5,6,7

print("----")
l.remove(2)
l.print_list() #prints 4,5,6,7
