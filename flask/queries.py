import sqlite3


def get_sql(query_name):
    filename = "../query/"+query_name+".sql"
    fd = open(filename, 'r')
    sql = fd.read()
    fd.close()
    return sql


def run_query(patient_id, date_from, date_to, query_type):
    conn = sqlite3.connect('i257symtrack.db')
    c = conn.cursor()
    sql = get_sql(query_type)
    if query_type=="q1" or query_type == "q2" or query_type == "q5":
        query_param = (patient_id, date_from, date_to)
    elif query_type == "q3" or query_type == "q4":
        query_param = (patient_id, date_from, date_to,
                       patient_id, date_from, date_to, date_from, date_from)
    else:
        return "Error: invalid query"

    query_result = c.execute(sql, query_param).fetchall()
    
    # rounding off numerical results
    query_result_rounded = []
    for r in query_result:
        lst = list(r)
        for s in range(len(lst)):
            if type(lst[s]) != str:
                lst[s] = round(lst[s], 2)

        query_result_rounded.append(tuple(lst))
        
    query_result_rounded.insert(0, tuple(i[0] for i in c.description))  # Insert column names

    return query_result_rounded



