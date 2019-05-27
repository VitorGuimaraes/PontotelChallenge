import psycopg2

conn = psycopg2.connect(database = "postgres", user = "postgres", 
                        password = "postgres", host = "127.0.0.1", port = "5432")

cur = conn.cursor()

def create_tables():
    cur.execute('''
        CREATE TABLE COMPANY (
            ID INT PRIMARY KEY    NOT NULL,
            NAME           TEXT    NOT NULL,
            OPEN           REAL    NOT NULL,
            HIGH           REAL    NOT NULL,
            LOW            REAL    NOT NULL, 
            CLOSE          REAL    NOT NULL,
            VOLUME         REAL    NOT NULL
        ); ''')

    cur.execute('''
        CREATE TABLE USER (
            ID INT PRIMARY KEY NOT NULL,
            NAME     TEXT NOT NULL;
            LOGIN    TEXT NOT NULL;
            PASSWORD TEXT NOT NULL
        ); ''')

create_tables()

conn.commit()
conn.close()