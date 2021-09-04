class Graph:
	def __init__(self):
		self.number_of_nodes = 0
		self.adjacent_list = {}

	def add_vertex(self, node):
		self.adjacent_list[node] = []
		self.number_of_nodes +=1
		

	def add_edge(self,node1, node2):
		self.adjacent_list[node1].append(node2)
		self.adjacent_list[node2].append(node1)


	def show_connections(self):
		for k,v in self.adjacent_list.items():
			vv = ""
			for val in v:
				vv+= " " + val
			print(k + " --> " + vv)


g = Graph()
g.add_vertex("0")
g.add_vertex("1")
g.add_vertex("2")
g.add_vertex("3")
g.add_vertex("4")
g.add_vertex("5")
g.add_vertex("6")

g.add_edge("3", "1")
g.add_edge("3", "4")
g.add_edge("4", "2")
g.add_edge("4", "5")
g.add_edge("1", "2")
g.add_edge("1", "0")
g.add_edge("0", "2")
g.add_edge("6", "5")

g.show_connections()
		
		
