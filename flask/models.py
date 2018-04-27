import sqlite3 as sql

def create_patient_table():
	with sqlite3.connect('i257symtrack.db') as conn:
		sql_stmt = '''
			CREATE TABLE PATIENT (
			patient_id int PRIMARY KEY,
			name VARCHAR(100) NOT NULL,
			date_of_birth VARCHAR(10),
			sex VARCHAR(10),
			city VARCHAR(100),
			state VARCHAR(100),
			street_address VARCHAR(100),
			telephone VARCHAR(100)
			'''
		conn.execute(sql_stmt)
		conn.commit()