#had to turn off Python in the Manage App Execution Aliases place to get below to run.  See this website:  https://stackoverflow.com/questions/65348890/python-was-not-found-run-without-arguments-to-install-from-the-microsoft-store


import psycopg2

#Connect to an existing database
conn = psycopg2.connect(
    database="exampledb",
    user="docker",
    password="docker",
    host='0.0.0.0'
)


#Open cursor to perform database operations
cur = conn.cursor()

# Query the database
cur.execute("SELECT * FROM student")
rows = cur.fetchall()

if not len(rows):
    print('Empty')

else:
    for row in rows:
        print(row)

# Close communication with database
cur.close()
conn.close()