from db import Db
from fileman import FileMan
from random import randint

class Person(Db,FileMan):
	""" this will manage people creation"""
	is_allocated = False
	person_type = None
	state_dict = {0:'NO',1:'YES'}
	table_name = 'person'
	assigned_room = ''



	def __init__(self,firstname,lastname,living_space = False):
		if type(firstname) != str or type(lastname) != str or type(living_space) != bool:
			raise ValueError

		self.firstname = firstname
		self.lastname = lastname
		self.living_space = living_space
		self.uid = firstname[0:1] + lastname[0:1] + str(randint(0,9))


	def full_details(self):
		return self.name() + ' ' + self.person_type + ' ' + self.get_state_dict(self.living_space) + ' ' + self.get_state_dict(self.is_allocated)


	def get_details_dict(self):
		return {
		'firstname':self.firstname,
		'lastname':self.lastname,
		'allocation':self.transalate(self.living_space),
		'allocated':self.transalate(self.is_allocated),
		'person_type':self.person_type,
		}

	def get_state_dict(self,state):
		"""returns corresponding value in state_dict """
		try:
			return self.state_dict[state]
		except:
			return self.state_dict[0]

	def transalate(self,status):
		if status:
			return 1
		else:
			return 0

	def name(self):
		return self.firstname + ' ' + self.lastname

	def allocate(self):
		file = FileMan('rooms.pkl')
		rooms = file.pickle_load()
		if not rooms:
			print 'No room available'
			return False
		for room in rooms:
			if room.allocate(self):
				print 'Person allocated to '+ room.name
				return True
		else:
			print 'No room available'
			return False


	def save(self):
		data = {
		'firstname':self.firstname,
		'lastname':self.lastname,
		'person_type':self.person_type,
		'allocated':self.transalate(self.is_allocated),
		'living_space':self.transalate(self.living_space),
		'assigned_room':self.assigned_room,
		}
		return self.create(data)
