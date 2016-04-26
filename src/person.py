from random import randint

from db import Db
from fileman import FileMan


class Person(Db, FileMan):
	"""This manages person entity and contains helper methods that ease content display."""

	state_dict = {0: 'NO', 1: 'YES'}
	table_name = 'person'
	date_time = ''

	def __init__(self, firstname, lastname, living_space=False):
		if type(firstname) != str or type(lastname) != str or type(living_space) != bool:
			raise ValueError

		self.firstname = firstname
		self.lastname = lastname
		self.living_space = living_space
		self.assigned_room = ''
		self.is_allocated = False
		self.uid = firstname[0:1] + lastname[0:1] + str(randint(0,9))


	def full_details(self):
		"""returns person full details as string."""

		details = self.name() + ' ' + self.person_type + ' ' + self.get_state_dict(self.living_space) 
		details += ' ' + self.get_state_dict(self.is_allocated) + ' ' + self.date_time
		return details


	def get_details_dict(self):
		"""returns person full details as dictionary."""

		return {
		'firstname':self.firstname,
		'lastname':self.lastname,
		'living_space':self.transalate(self.living_space),
		'allocated':self.transalate(self.is_allocated),
		'person_type':self.person_type,
		'assigned_room':self.assigned_room,
		'date_time':self.date_time,
		}

	def get_state_dict(self, state):
		"""returns corresponding value in state_dict."""

		try:
			return self.state_dict[state]
		except:
			return self.state_dict[0]

	def transalate(self, status):
		"""this simply converts bool to int (0 or 1)."""

		if status:
			return 1
		else:
			return 0

	def name(self):
		"""returns full name of the person."""

		return self.firstname + ' ' + self.lastname

	def allocate(self, room_name):
		self.is_allocated = True
		self.assigned_room = room_name


	def save(self):
		"""Saves person into sqlite database."""
		
		data = self.get_details_dict()
		exists = self.find_by_attr({'firstname':data['firstname'],'lastname':data['lastname'],'person_type':data['person_type']})
		if exists:
			return False
			
		return self.create(data)

	def is_fellow(self):
		return self.person_type == 'FELLOW'

	def is_staff(self):
		return self.person_type == 'STAFF'
