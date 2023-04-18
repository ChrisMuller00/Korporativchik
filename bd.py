import sqlite3 as sql

con = sql.connect("users.db")
cur = con.cursor()
statement = "SELECT username, password FROM users"
cur.execute(statement)
print(cur.fetchall())



with open('schema.sql') as f:
    con.executescript(f.read())

cur = con.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

con.commit()
con.close()
