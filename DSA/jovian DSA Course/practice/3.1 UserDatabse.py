class User:
	def __init__(self, username, name, email):
		self.username = username
		self.name = name
		self.email = email 

	def __repr__(self):
		return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

	def __str__(self):
		return self.__repr__()


class UserDatabase:
	def __init__(self,users=[]):
		self.users = users

	def insert(self,user):
		i=0
		while i<len(self.users):
			if self.users[i].username > user.username:
				break
			i+=1
		self.users.insert(i,user)

	def find(self,username):
		for user in self.users:
			if user.username==username:
				return user

	def update(self,user):
		target=self.find(user.username)
		if target is not None:
			target.username,target.name,target.email=user.username,user.name,user.email

	def delete(self,username):
		target=self.find(user.username)
		if target is not None:
			self.users.remove(target)

	def list_all(self):
		return self.users


aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
users = UserDatabase([aakash, biraj, hemanth, jadhesh, siddhant, sonaksh])
users.insert(vishal)
vishal2 = User('vishal', 'Vishal Goel*', 'vishal@example.com*')
print(users.find('vishal'),'\n')
users.update(vishal2)
print(users.list_all())
