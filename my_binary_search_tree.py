import queue
class TreeNode:
	def __init__(self, value):
		self.right = None
		self.left = None
		self.val = value
		

class Bst:
	def __init__(self):
		self.root = None
	def insert(self, value):
		new_node = TreeNode(value)
		if self.root is None:
			self.root = new_node
			return 
		else:
			cur = self.root
			while True:
				if value < cur.val:
					if cur.left is None:
						cur.left = new_node
						return 
					else:
						cur = cur.left
				else:
					if cur.right is None:
						cur.right = new_node
						return 
					else:
						cur = cur.right

	def lookup(self, value):
		if self.root is None:
			return False
		cur = self.root
		while cur:
			if value < cur.val:
				cur = cur.left
			elif value > cur.val:
				cur = cur.right
			elif value == cur.val:
				return True
		return False

	def remove(self, value):
		if not self.lookup(value):
			return False
		# go to the right then left of what you want to delte
		cur = self.root
		parent = None
		while cur:
			if value < cur.val:
				parent = cur
				cur = cur.left
			elif value > cur.val:
				parent = cur
				cur = cur.right
			else:
				#if there is no right child
				if cur.right is None:
					if not parent: # we are deleting root
						self.root = cur.left
					else:
						if cur.val < parent.val:
							parent.left = cur.left
						else:
							parent.right = cur.left
							
				elif cur.right.left is None:
					if parent is None:
						self.root = cur.left
					else:
						cur.right.left = cur.left
						if parent.val > cur.val:
							parent.left = cur.right
						else:
							parent.right = cur.right
				else:
					#find rights left most child
					leftmost = cur.right.left
					leftmost_parent = cur.rigt
					while leftmost.left is not None:
						leftmost_parent = leftmost
						leftmost = leftmost.right

					leftmost_parent.left = leftmost.right
					leftmost.left = cur.left
					leftmost.right = cur.right

					if parent is None:
						self.root = leftmost
					else:
						if parent.val > cur.val:
							parent.left = leftmost
						else: 
							parent.right = leftmost
		return True
							
	def bfs(self):
		q= queue.Queue()
		q.put(self.root)
		while not q.empty():
			n = q.get()
			if n.left:
				q.put(n.left)
			if n.right:
				q.put(n.right)
			print(n.val)
				
		
	def print_in_order(self, root):
		if root:
			self.print_in_order(root.left)
			print(root.val)
			self.print_in_order(root.right)

	

	def print_pre_order(self, root):
		if root:
			print(root.val)
			self.print_pre_order(root.left)
			self.print_pre_order(root.right)
			
	def print_post_order(self, root):
		if root:
			self.print_post_order(root.left)
			self.print_ost_order(root.right)
			print(root.val)
		





# Test Cases 
b = Bst()		
b.insert(9)
b.insert(6)
b.insert(12)
b.insert(1)
b.insert(4)
b.insert(34)
b.insert(35)

b.print_in_order(b.root) # prints: 1,4,6,9,15,20,170
print(b.lookup(170)) # print True
print(b.lookup(171)) # print False
print(b.lookup(12)) # print False
print(b.lookup(1)) # print True
print("------------")
b.bfs()
