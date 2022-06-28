
import sqlite3


def get_db_connection():
    conn = sqlite3.connect('database.db')

    return conn

def getUpdates():
    conn = get_db_connection().cursor()
    updates = conn.execute('SELECT update_id FROM updates').fetchall()
    conn.close()

    result = []

    for upd in updates:
        (idx,) = upd
        result.append(idx)
        
    return result    

def addUpdateID(update_id):
    conn = get_db_connection()

    curr = conn.cursor()

    curr.execute("INSERT into updates (update_id) VALUES (?)",
                (update_id)
                )

    conn.commit()
    conn.close()