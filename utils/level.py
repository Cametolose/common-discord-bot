import sqlite3
import time

con = sqlite3.connect("data/data.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    id TEXT PRIMARY KEY,
    xp INTEGER DEFAULT 0,
    level INTEGER DEFAULT 0
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS deleted_messages(
    message_id TEXT PRIMARY KEY,
    deleteat 
)
""")

con.commit()



def create_user(userid):
    cur.execute(
        "INSERT OR IGNORE INTO users (id, xp, level) VALUES (?, ?, ?)",
        (str(userid), 0, 0)
    )
    con.commit()

def get_user(userid):
    create_user(userid)
    cur.execute(
        "SELECT xp, level FROM users WHERE id=?",
        (str(userid),)
    )
    return cur.fetchone()


def message_xp(userid, msglength):
    levelup = False 
    create_user(userid)

    xp_gain = int((msglength / 10) ** 1.1)

    cur.execute(
        "SELECT xp, level FROM users WHERE id=?",
        (str(userid),)
    )

    xp, level = cur.fetchone()

    xp += xp_gain

    xp_for_current_level = level * 10
    if(xp >= xp_for_current_level):
        level += 1
        levelup = True 

    cur.execute(
        "UPDATE users SET xp=?, level=? WHERE id=?",
        (xp, level, str(userid))
    )

    con.commit()

    return levelup 


def get_expired_messages():
    cur.execute(
        "SELECT message_id, deleteat FROM deleted_messages WHERE deleteat <= ?",
        (time.time(),)
    )
    return cur.fetchall()




def close_database():
    con.commit()
    con.close()