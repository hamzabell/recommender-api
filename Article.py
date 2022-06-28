
import sqlite3


def get_db_connection():
    conn = sqlite3.connect('database.db')

    return conn

def getArticles():
    conn = get_db_connection().cursor()
    articles = conn.execute('SELECT id, Title, Description, link FROM articles').fetchall()
    conn.close()

    result = []
    for article in articles:
        (id, Title, Description, link,) = article
        result.append({
            "index": id,
            "title": Title,
            "description": Description,
            "link": link
        })


    return result    

def addArticle(Title, Description, link):
    conn = get_db_connection()

    curr = conn.cursor()

    curr.execute("INSERT into articles (Title, Description, link) VALUES (?, ?, ?)",
                (Title, Description, link)
                )

    conn.commit()
    conn.close()