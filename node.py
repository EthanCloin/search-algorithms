class Node():
# node constructor
	def __init__(self, parent, position):
		self.parent = parent
		self.position = position
		self.obstacle = False
		
		self.f_score = 0
		self.g_score = 0
		self.h_score = 0
		self.u_score = 0


# override equals to compare nodes by position attribute
	def __eq__(self, other):
		return self.position == other.position

	def __lt__(self, other):
		return self.u_score < other.u_score

	def __gt__(self, other):
		return self.u_score > other.u_score

# set to obstacle status
	def make_obstacle(self):
		self.obstacle = True
