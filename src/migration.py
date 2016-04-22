from db import Db

class Migration(Db):
	"""docstring for Migration"""
	table_definitions = [
	'''CREATE TABLE person
       (id INTEGER PRIMARY KEY AUTOINCREMENT,
       assigned_room         CHAR(255),
       firstname         CHAR(255),
       lastname         CHAR(255),
       person_type         CHAR(25),
       living_space       INT    NOT NULL,
       allocated       INT    NOT NULL,
       date_time         CHAR(25));
    ''',

    '''CREATE TABLE room
       (id INTEGER PRIMARY KEY AUTOINCREMENT,
       name           CHAR(255),
       capacity       INT     NOT NULL,
       type           CHAR(25),
       allocated       INT     NOT NULL,
       date_time         CHAR(25));
    '''
	]

	tables = ['person','room']

	def __init__(self,dbname = 'amity'):
		super(Migration,self).__init__(dbname)

		

	def install(self):
		for index,sql in enumerate(self.table_definitions):
			try:
				if self.execute(sql):
					print self.tables[index] + ' table created'
				else:
					print self.tables[index] + ' table already exists'
			except:
				print self.tables[index] + ' table exists'

	
	def drop(self):
		for table in self.tables:
			try:
				if self.execute('DROP TABLE '+table+';'):
					print 'dropped table '+table
			except:
				print table+' does not exist'

