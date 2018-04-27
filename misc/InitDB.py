# Run this module to generate DB file

import csv
import sqlite3


def init_patient(conn):
    query = """ INSERT INTO
patient(patient_id, name, date_of_birth, city, state, country, street_address, telephone)
VALUES(?, ?, ?, ?, ?, ?, ?, ?) """
    init_table(conn, "patient", query)


def init_localization(conn):
    query = """ INSERT INTO
localization(locale_id, name)
VALUES(?, ?) """
    init_table(conn, "localization", query)


def init_disease(conn):
    query = """ INSERT INTO
disease(icd_code, name, description)
VALUES(?, ?, ?) """
    init_table(conn, "disease", query)


def init_symptom(conn):
    query = """ INSERT INTO
symptom(symptom_id, name, description, has_duration, has_bodypart, has_severity, has_character)
VALUES(?, ?, ?, ?, ?, ?, ?) """
    init_table(conn, "symptom", query)


def init_diseasepatients(conn):
    query = """ INSERT INTO
diseasepatients(icd_code, patient_id)
VALUES(?, ?) """
    init_table(conn, "diseasepatients", query)


def init_diseasesymptoms(conn):
    query = """ INSERT INTO
diseasesymptoms(icd_code, symptom_id)
VALUES(?, ?) """
    init_table(conn, "diseasesymptoms", query)


def init_observation(conn):
    query = """ INSERT INTO
observation(observation_id, patient_id, symptom_id, symptom_start_time, 
duration, severity, description, character, timing, locale_id, log_time)
VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
    init_table(conn, "observation", query)


def init_table(conn, table_name, insert_query):
    data = read_csv(table_name + ".csv")
    cur = conn.cursor()
    query = "DELETE FROM " + table_name
    cur.execute(query)
    print("Deleted %d rows from '%s' table." % (cur.rowcount, table_name))
    query = insert_query
    count = 0
    for row in data[1:]:
        #if row[0].isdigit():
        cur.execute(query, tuple(row))
        #print("Writing:", row)
        count += 1
    print("Inserted %d rows into '%s' table.\n" % (count, table_name))

def read_csv(path):
    csv_file = open(path, 'r', encoding='utf-8')
    raw_data = csv.reader(csv_file)
    data = []
    for line in raw_data:
        data.append(line)
    csv_file.close()
    return data


def main():
    conn = sqlite3.connect('i257symtrack.db')
    init_patient(conn)
    init_localization(conn)
    #init_disease(conn)
    init_symptom(conn)
    #init_diseasepatients(conn)
    #init_diseasesymptoms(conn)
    init_observation(conn)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()