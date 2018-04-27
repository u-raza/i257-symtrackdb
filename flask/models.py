import sqlite3 as sql

def create_patient_table():
	# with sqlite3.connect('i257symtrack.db') as conn:
	# 	sql_stmt = '''
	# 		CREATE TABLE PATIENT (
	# 		patient_id int PRIMARY KEY,
	# 		name VARCHAR(100) NOT NULL,
	# 		date_of_birth VARCHAR(10),
	# 		sex VARCHAR(10),
	# 		city VARCHAR(100),
	# 		state VARCHAR(100),
	# 		street_address VARCHAR(100),
	# 		telephone VARCHAR(100)
	# 		'''
	# 	conn.execute(sql_stmt)
	# 	conn.commit()

	# tables are already created via createdb.sql
	pass

# Add Trial
def add_patient(name, date_of_birth, city, state, country, telephone):
    with sql.connect("i257symtrack.db") as conn:
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys = ON')

        sql_command = \
            "INSERT INTO patient (name, date_of_birth, city, state, country, telephone) VALUES (?, ?, ?, ?, ?, ?)"

        cur.execute(sql_command, (name, date_of_birth, city, state, country, telephone))
        #trip_id = cur.lastrowid
        conn.commit()
        print('done')
