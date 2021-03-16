import sqlite3
con = sqlite3.connect('test.db')
cur = con.cursor()
'''
def creerbdd():
    cur = con.cursor()
    con.execute(
        "CREATE TABLE evenements (Temps	REAL,particule1	INTEGER,particule2	INTEGER,px	REAL,py	REAL   ")

'''

def remisea0 ():

    cur.execute("delete from evenements")
    con.commit()



def enregistrement(t,p1,p2,x,y):
    cur.execute("insert into evenements values ({},{},{},{},{})".format(t,p1,p2,x,y))
    con.commit()

