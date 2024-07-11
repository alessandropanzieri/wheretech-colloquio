from psycopg2 import connect

def get_connection():

    return connect(
        port = 5432,
        user = "candidato3",
        password = "candidato3",
        database = "candidato3",
        host = "postgresql01.wheretech.lan"
    )