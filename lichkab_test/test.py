import sqlite3

db = [
    {
        'text': 'hello',
        'name': 'J',
        'time': 0.8
    },
    {
        'text': 'hello, J',
        'name': 'N',
        'time': 0.2
    },
]

# import sqlite3
# db = sqlite3.connect("test.sqlite3")
# cur = db.cursor()
# res = cur.execute("select * from table").fetchall()
# data = dict(zip([c[0] for c in cur.description], res[0]))
#
# print(data)

with sqlite3.connect('server.db') as db3:
    cur = db3.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        text text,
        name text,
        time text
        )""")
    db3.commit()

a = cur.execute("INSERT INTO users VALUES (:text, :name, :time)", db[0])
db3.commit()

a = cur.execute("SELECT * FROM users").fetchall()
data = [dict(zip([c[0] for c in cur.description], i)) for i in a]


print(data)


# todo sql append
#    sql.execute(f"INSERT INTO users VALUES ('{text}', '{name}', '{time}')")
#    sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (text, name, time))
#    db2.commit()
#    print('создалось')


