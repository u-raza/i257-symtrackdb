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

# Add Patient
def add_patient(name, date_of_birth, street_address, city, state, country, telephone):
    with sql.connect("i257symtrack.db") as conn:
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys = ON')

        sql_stmt = \
            "INSERT INTO patient (name, date_of_birth, street_address, city, state, country, telephone) VALUES (?, ?, ?, ?, ?, ?, ?)"

        cur.execute(sql_stmt, (name, date_of_birth, street_address, city, state, country, telephone))
        #trip_id = cur.lastrowid
        conn.commit()
        print('done')

# Update Patient
def update_patient(patient_id, name, date_of_birth, street_address, city, state, country, telephone):
    with sql.connect("i257symtrack.db") as conn:
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys = ON')

        sql_stmt = \
            "UPDATE PATIENT\
            	SET name = ?, date_of_birth = ?, street_address = ?, city = ?, state = ?, country = ?, telephone = ?\
            	WHERE patient_id = ?"

        cur.execute(sql_stmt, (name, date_of_birth, street_address, city, state, country, telephone, patient_id))
        conn.commit()

# Get Patient
def get_patient(patient_id):
    with sql.connect("i257symtrack.db") as conn:
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys = ON')

        sql_stmt = \
            "SELECT name, date_of_birth, street_address, city, state, country, telephone FROM PATIENT\
            	WHERE patient_id = ?"

        result = [dict(name=row[0], date_of_birth=row[1],
                    street_address=row[2],
                    city=row[3],
                    state=row[4],
                    country=row[5],
                    telephone=row[6]) for row in cur.execute(sql_stmt, (patient_id)).fetchall()]
        return result

# add symptom
def add_symptom(sym_id, name, description, has_duration, has_bodypart, has_severity, has_character):
	    with sql.connect("i257symtrack.db") as conn:
	        conn.row_factory = sql.Row
	        cur = conn.cursor()
	        cur.execute('PRAGMA foreign_keys = ON')

	        sql_stmt = \
	            "INSERT INTO symptom (symptom_id, name, description, has_duration, has_bodypart, has_severity, has_character) VALUES (?, ?, ?, ?, ?, ?, ?)"

	        cur.execute(sql_stmt, (sym_id, name, description, has_duration, has_bodypart, has_severity, has_character))
	        #trip_id = cur.lastrowid
	        #conn.commit()

	        