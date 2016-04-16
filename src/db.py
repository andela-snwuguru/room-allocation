import sqlite3

class Db(object):
	"""Database manipulation"""
	name = 'amity'
	table_name = 'table_name'

	def __init__(self,dbname = 'amity',table_name = 'table_name'):
		self.name = dbname
		self.table_name = table_name
		self.connection = sqlite3.connect(self.name+'.db')


	def execute(self,sql):
		try:
			return self.connection.execute(sql)
		except:
			return False

	def find(self,id):
		try:
			return self.execute("SELECT *  from "+table_name+' WHERE id = '+id)
		except:
			return False

	def findall(self):
		try:
			return self.execute("SELECT *  from "+table_name)
		except:
			return False

	def findbyattr(self,attributes):
		pass

	def create(self,data):
		resolved = self.prepare(data)
		sql = 'INSERT INTO '+self.table_name+' ('+resolved['column']+') VALUES (1,'+resolved['value']+')'
		return self.execute(sql)
		
      

	def prepare(self,data):
		columns = 'id,'
		values = ''
		columnvalue = {}
		for key,value in data.items():
			columns += key + ','
			values += "'" + str(value) + "',"
		columnvalue['column'] = columns[:-1]
		columnvalue['value'] = values[:-1]
		return columnvalue

	def update(self,data):
		pass