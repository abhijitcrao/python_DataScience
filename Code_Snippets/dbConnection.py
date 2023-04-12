import cx_Oracle

try:
    con = cx_Oracle.connect('tiger/scott@localhost:1521/xe')
# format is userid/pass@hostname:port/servicename

except cx_Oracle.DatabaseError as er:
    print('There is an error in the Oracle database:', er)

else:
    try:
        cur = con.cursor()

        # fetchall() is used to fetch all records from result set
        cur.execute('select * from employee')
        rows = cur.fetchall()
        print(rows)

        cur.execute('select * from employee')
        rows = cur.fetchmany(3)
        print(rows)

        # fetchall() : The fetchall() is used to fetch all records.
        # fetchmany(int) : The fetchmany(int) is used to fetch the limited number of records.
        #		fetchone() : The fetchone() is used to fetch one record from the top of the result set.
        # fetchone() is used fetch one record from top of the result set
        cur.execute('select * from employee')
        rows = cur.fetchone()
        print(rows)

    except cx_Oracle.DatabaseError as er:
        print('There is an error in the Oracle database:', er)

    except Exception as er:
        print('Error:' + str(er))

    finally:
        if cur:
            cur.close()

finally:
    if con:
        con.close()
