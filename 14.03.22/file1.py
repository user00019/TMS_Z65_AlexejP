from sqlalchemy import create_engine

e = create_engine('sqlite:///sqlite1.db')
e.execute("""
    create table sample (
        id integer primary key autoincrement,
        firstname varchar(255),
        age integer
    )
""")
conn = e.connect()
trans = conn.begin()

conn.execute(
    "INSERT INTO SAMPLE (firstname, age) VALUES (:firstname, :age)",
    firstname="Alex", age=16)

conn.execute(
    "INSERT INTO SAMPLE (firstname, age) VALUES (:firstname, :age)",
    firstname="Alex", age=25)

conn.execute(
    "INSERT INTO SAMPLE (firstname, age) VALUES (:firstname, :age)",
    firstname="Mike", age=18)

conn.execute(
    "INSERT INTO SAMPLE (firstname, age) VALUES (:firstname, :age)",
    firstname="Bob", age=28)

conn.execute(
    "INSERT INTO SAMPLE (firstname, age) VALUES (:firstname, :age)",
    firstname="Alex", age=40)

trans.commit()
conn.close()


a = e.execute("""select * from sample where firstname = 'Alex'""")
for x in a:
    print(x)
b = e.execute("""select * from sample where age < 25""")
for x in b:
    print(x)
c = e.execute("""select * from sample where age > 15 and age < 25""")
for x in c:
    print(x)
