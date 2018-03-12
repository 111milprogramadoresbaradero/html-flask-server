import psycopg2
import os
import time

#DEFAULT SCHEMA
SCHEMA =  os.getenv('DEFAULT_SCHEMA', 'public')

# SQL STATEMENTS
EXISTS_TABLE = "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = '{}' AND table_name = '{}');"
<<<<<<< HEAD
CREATE_TABLE = "CREATE TABLE {}.personas (firstname varchar(255), lastname varchar(255), username1 varchar(255), username2 varchar(255));".format(SCHEMA)
INSERT_ROW = "INSERT INTO {}.personas (firstname, lastname, username1, username2) values(%s, %s, %s, %s);".format(SCHEMA)
=======
CREATE_TABLE = "CREATE TABLE personas (firstname varchar(255), lastname varchar(255), username1 varchar(255), username2 varchar(255));"
INSERT_QUERY = "INSERT INTO {}.personas (firstname, lastname, username1, username2) values(%s, %s, %s, %s);".format(SCHEMA)
SELECT_QUERY = "SELECT * FROM {}.personas;".format(SCHEMA)

>>>>>>> a2ea151... Agrega servicio para listar personas.

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
    cur = conn.cursor()
    try:  
        sql = EXISTS_TABLE.format(SCHEMA, 'personas')
        cur.execute(sql)
        created = cur.fetchone()[0]
        if not created:
            cur.execute(CREATE_TABLE)
            conn.commit()
    finally:
        cur.close()
        conn.close()

def insertPersona(firstname, lastname, username1, username2):
    conn = createConnection()
    cur = conn.cursor()
<<<<<<< HEAD
    try:
        params = [firstname, lastname, username1, username2]
        cur.execute(INSERT_ROW, params)
        conn.commit()
    finally:
        cur.close()
        conn.close()
=======
    params = [firstname, lastname, username1, username2]
    cur.execute(INSERT_QUERY, params)
    conn.commit()
    cur.close()
    conn.close()
>>>>>>> a2ea151... Agrega servicio para listar personas.

def listarPersonas():
    conn = createConnection()
    cur = conn.cursor()
    cur.execute(SELECT_QUERY)
    personas = cur.fetchall()
    cur.close()
    conn.close()
    return personas

def init():
    wait_time = eval(os.getenv('WAIT_DB', '0'))
    time.sleep(wait_time)
    createTables()



