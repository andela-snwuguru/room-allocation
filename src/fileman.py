import os
import os.path
import pickle


class FileMan(object):
	"""FileMan reads and write to file"""

	def __init__(self, file_name):
		if type(file_name) != str:
			raise ValueError
		
		self.base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))	
		self.set_file_location(file_name)


	def set_file_location(self, file_name):
		self.file_location = self.base + '/data/' + file_name


	def read(self):
		"""reads a file and return content in a list.
		returns False if path is not a file."""

		if not self.validate():
			return False

		data = []
		with open(self.file_location,'r') as file:
			for line in file:
				data.append(line[:-1])
			return data

	def write(self, data):
		"""appends content to a file."""

		if type(data) != str:
			raise ValueError

		with open(self.file_location,'a+') as file:
			file.read()
			file.write(data+'\n')

	def replace(self, data):
		"""replaces content of a file."""

		if type(data) != str:
			raise ValueError
			
		with open(self.file_location,'w') as file:
			file.write(data+'\n')

	def remove(self):
		"""deletes file."""

		if not self.validate():
			return False

		return os.remove(self.file_location)

	def validate(self):
		"""validates the existence of a give file location."""

		if not self.is_file(self.file_location):
			return False
		return True

	def is_file(self, file_path):
		return os.path.isfile(file_path) 

	def pickle_dump(self, data):
		"""dumps data structure into a file."""

		with open(self.file_location,'wb') as file:
			pickle.dump(data, file)
		return True

	def pickle_load(self):
		"""load data structure from a file."""

		if not self.validate():
			return False

		with open(self.file_location,'rb') as file:
			return pickle.load(file)
