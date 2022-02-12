"""
python delete_images.py
"""

import sqlite3
import os

DATABASE_NAME = 'db.sqlite3'

def clearRecords(DATABASE_NAME):
    """
    Delete all records from the database
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM main.WebApp_formmodel;",)
    print(c.fetchall())
    c.execute("DELETE FROM main.WebApp_formmodel;",)
    print('We have deleted', c.rowcount, 'records from the table.')
    conn.commit()
    conn.close()