# A detailed explanation of this question can be found in the link below:
#
# https://leetcode.com/discuss/interview-question/302164/google-phone-screen-monarchy


class Person:
	def __init__(self, name):
		self.name = name
		self.is_alive = True
		self.children = []


class Monarchy:
	def __init__(self, king):
		self.king = Person(king)
		self._persons = {
			self.king.name: self.king
		}
	def birth(self, child_name, parent_name):
		parent = self._persons[parent_name]
		child = Person(child_name)
		parent.children.append(child)
		self._persons[child_name] = child
		
	
  def death(self, name):
		died_person = self._persons[name]
		if not died_person:
			return 
		died_person.is_alive=False

	def _pre_dfs(self, person, suc_list):
		if person.is_alive:
			suc_list.append(person.name)
		for child in person.children:
				self._pre_dfs(child, suc_list)
		
		
	def get_suc(self):
		suc_list = []
		self._pre_dfs(self.king, suc_list)
		return suc_list
		

# Test Cases 
#--------------------

m1 = Monarchy("Jake")
m1.birth("Catherine", "Jake")
m1.birth("Jane","Catherine")
m1.birth("Farah", "Jane")
m1.birth("Tom", "Jake")
m1.birth("Celine", "Jake")
m1.birth("Mark","Catherine")
m1.birth("Peter", "Celine")

print(m1.get_suc())  # Correct Output --> ["Jake", "Catherine", "Jane", "Farah", "Mark", "Tom", "Celine", "Peter"]

m1.death("Jake")
m1.death("Jane")

print(m1.get_suc()) # Correct Output --> ["Catherine", "Farah", "Mark", "Tom", "Celine", "Peter"]
