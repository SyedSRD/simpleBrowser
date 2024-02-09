# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 21:35:52 2019

@author: SYED
"""

import sqlite3,time,sys
def create(dbname):
    
    with sqlite3.connect(dbname) as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS history(
                                           sno1 INTEGER PRIMARY KEY AUTOINCREMENT,
                                           hname text NOT NULL);
                                           ''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS bookmark(
                                           sno2 INTEGER PRIMARY KEY AUTOINCREMENT ,
                                           bname text NOT NULL);
                                           ''')
        db.commit()
        cursor.execute("SELECT * FROM history")
        print(cursor.fetchall())
        cursor.close()
    
def historycall(dbname,name):
    try:
        with sqlite3.connect(dbname) as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO history(hname) VALUES(?);",[(name)])
        db.commit()
        cursor.close()
        db.close()
    except sqlite3.OperationalError as e:
            create(dbname)
    except Exception as e:
            print(e)
    
    
def bookmarkcall(dbname,name):
    try:
        with sqlite3.connect(dbname) as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO bookmark(bname) VALUES(?);",[(name)])
        db.commit()
        cursor.close()
        db.close()
    except Exception as e:
            print(e)


def menu(dbname,name,id=0):
    try:
        if id==1:
            historycall(dbname,name)
        elif id ==2:
            bookmarkcall(dbname,name)
        else:
            pass
        
    except sqlite3.OperationalError as e:
            create(dbname)
    except Exception as e:
            print(e)
    
    
    
if __name__ == "__main__":
    menu("browserdb.db","http://www.google.com",1)