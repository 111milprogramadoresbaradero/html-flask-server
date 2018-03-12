import psycopg2
import os
import time

#DEFAULT SCHEMA
SCHEMA =  os.getenv('DEFAULT_SCHEMA', 'public')

# SQL STATEMENTS
EXISTS_TABLE = "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = '{}' AND table_name = '{}');"
CREATE_TABLE = "CREATE TABLE personas (firstname varchar(255), lastname varchar(255), username1 varchar(255), username2 varchar(255));"
INSERT_ROW = "INSERT INTO {}.personas (firstname, lastname, username1, username2) values(%s, %s, %s, %s);".format(SCHEMA)

DSN = "dbname={} host={} port={} user={}".format(
    os.getenv('DATABASE', 'postgres'),
    os.getenv('DB_HOST', 'localhost'),
    os.getenv('DB_PORT', '5432'),
    os.getenv('DB_USER', 'postgres')
)

def createConnection():
    return psycopg2.connect(DSN)

def createTables():
    conn = createConnection()
    sql = EXISTS_TABLE.format(SCHEMA, 'personas')
    cur = conn.cursor()
    cur.execute(sql)
    created = cur.fetchone()[0]
    if not created:
        cur.execute(CREATE_TABLE)
        conn.commit()
    cur.close()
    conn.close()

def insertPersona(firstname, lastname, username1, username2):
    conn = createConnection()
    cur = conn.cursor()
    params = [firstname, lastname, username1, username2]
    cur.execute(INSERT_ROW, params)
    conn.commit()
    cur.close()
    conn.close()

def init():
    wait_time = eval(os.getenv('WAIT_DB', '0'))
    time.sleep(wait_time)
    createTables()



