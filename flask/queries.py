import sqlite3


def get_sql(query_name):
    filename = "../query/"+query_name+".sql"
    fd = open(filename, 'r')
    sql = fd.read()
    fd.close()
    return sql
"""
    conn = sqlite3.connect('i257symtrack.db')
    c = conn.cursor()
    data = []
    for db_row in c.execute(query):
        data_row = {}
        data_row["patient_id"] = db_row[0]
        data_row["name"] = db_row[1]
        data_row["date_of_birth"] = db_row[2]
        data_row["street_address"] = db_row[3]
        data_row["city"] = db_row[4]
        data_row["state"] = db_row[5]
        data_row["country"] = db_row[6]
        data_row["telephone"] = db_row[7]
        data.append(data_row)
    conn.close()
    """


def runquery(patient_id, date_from, date_to, query_name):
    #data = patient_id + start_date.strftime('%Y-%m-%d') + end_date.strftime('%Y-%m-%d') + query_type
    conn = sqlite3.connect('i257symtrack.db')
    c = conn.cursor()
    sql = get_sql(query_name)
    if query_name=="sql1" or query_name == "sql2"  or query_name == "sql5":
        query_result = c.execute(sql, (patient_id, date_from, date_to)).fetchall()
    elif query_name == "sql3" or query_name == "sql4":
        query_result = c.execute(sql,\
            (patient_id, date_from, date_to \
            , patient_id, date_from, date_to, date_from, date_from
            )).fetchall()
    else:
        return "Error: invalid query"

    ret = ""
    for row in query_result:
        for col in row:
            ret = ret  + str(col)
        ret = ret + "\n"
    return ret



