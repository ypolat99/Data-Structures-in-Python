class TreeNode:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.val = value


class Bst:
	def __init__(self):
		self.root = None
		
	def insert(self, value):
		new_node = TreeNode(value)
		if not self.root:
			self.root = new_node
			return
		else:
			cur = self.root
			while True:
				if value < cur.val:
					if not cur.left:
						cur.left = new_node
						return
					else:
						cur = cur.left
				else:
					if not cur.right:
						cur.right = new_node
						return
					else:
						cur = cur.right 
	
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
b.insert(4)
b.insert(6)
b.insert(20)
b.insert(170)
b.insert(15)
b.insert(1)

b.print_in_order(b.root)
		
		
			
		
