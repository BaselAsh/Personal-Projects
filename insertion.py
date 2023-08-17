import sqlite3
con = sqlite3.connect("app.db")
cr = con.cursor()


cr.execute("INSERT INTO skills VALUES('CSS', 70, 1)")
cr.execute("INSERT INTO skills VALUES('Java', 30, 1)")
cr.execute("INSERT INTO skills VALUES('PHP', 80, 1)")
cr.execute("INSERT INTO skills VALUES('CSS', 90, 1)")
cr.execute("INSERT INTO skills VALUES('Python', 60, 2)")
cr.execute("INSERT INTO skills VALUES('C++', 50, 1)")
cr.execute("INSERT INTO skills VALUES('Java', 75, 3)")


con.commit()
con.close()