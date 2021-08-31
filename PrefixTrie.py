# This is a Trie that has insertt, search, and prefix methods as shown below. 

class TrieNode:
	def __init__(self):
		self.end = False
		self.keys = {}
	
class Trie:
	def __init__(self):
		self.root = TrieNode()
		
	def insertt(self, s=1, node = None):
		if node is None:
			 node= self.root
		if len(s) ==0:
			node.end = True
			return
		elif s[0] not in node.keys:
			node.keys[s[0]] = TrieNode()
			return self.insert(s[1:], node.keys[s[0]])
		else:
			return self.insert(s[1:], node.keys[s[0]])

	def search(s, node=None):
		if node is None:
			node= self.root
		if len(s)==0 and node.end:
			return True
		elif len(s)==0:
			return False
		elif s[0] not in node.keys:
			return False
		else:
			return self.search(s[1:], node.keys[s[0]])

	def starts_with(prefix, node = None):
		if node is None:
			node= self.root
		if len(prefix) ==0:
			return True
		elif prefix[0] in node.keys:
			return self.starts_with(prefix[1:], node.keys[prefix[0]])
		return False
			
