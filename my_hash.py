#import numpy as np
from numpy import ndarray, empty

a = ndarray((5),int)
b = empty(4, dtype=object)

class my_hash:
	def __init__(self, size):
		self.data = empty(size, dtype=object)
		
	def _hash(self, key):
		hash=0
		for idx, chr in enumerate(key):
			hash = (hash + ord(chr)*idx) % len(self.data)
		return hash

	def set(self, key, value):
		index = self._hash(key)
		if not self.data[index]:
			self.data[index] = []
		self.data[index].append([key,value])
		
	def get(self, key):
		index = self._hash(key)
		cur_bucket = self.data[index]
		if len(cur_bucket) >0:
			for k, v in cur_bucket:
				if k == key:
					return v
		return 

		
			
	def keys(self):
		keys_arr = [k for bucket in filter(lambda x: x is not None, self.data) for k,v in bucket ] 
		return keys_arr
		#result = filter(lambda x: x % 2 != 0, seq)
			
		
#Test Cases 

h = my_hash(4)
print(h.data) # prints [None, None, None, None]
h.set("grapes", 100)
h.set("apples", 200)
h.set("oranges", 300)
print(h.data) # prints [None, None, None, list([["grapes", 100]])]
print(h.get("grapes")) # prints 100
print(h.keys()) # prints ["oranges", "grapes", "apples"]

