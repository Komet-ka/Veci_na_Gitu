import psycopg
from decouple import config

db_user = config("DB_USER")
db_password = config("DB_PASSWORD")
db_host = config("DB_HOST")
db_port = config("DB_PORT")
db_name = config("DB_NAME")

database_url = f"user={db_user} password={db_password} host={db_host} port={db_port} dbname={db_name}"

with psycopg.connect(database_url) as conn:
    with conn.cursor() as cur:
        cur.execute("""
        DROP TABLE IF EXISTS todos;
        
        CREATE TABLE IF NOT EXISTS todos (
            id SERIAL PRIMARY KEY,
            label TEXT NOT NULL,
            status TEXT NOT NULl
            );
            """)

        query = """
            INSERT INTO todos (label, status)
            VALUES (%s, %s)
            RETURNING id;
        """
        data = [
            ("Kup rohliky", "urgentni"),
            ("Kup chleba", "zitra"),
            ("Zajed do mycky", "do konce tydne")
                ]

        result = cur.executemany(query, data, returning = True)
        ids = []

        while True:
            result = cur.fetchone()
            print(result[0])
            ids.append((result[0]))
            if not cur.nextset():
                break

        def get_todo_by_id(id):
            query = """
                SELECT id, label FROM todos
                WHERE id = %(id)s;
            """

            result = cur.execute(query, {"id": id})
            return result.fetchone()

        todo = get_todo_by_id(21)
        print(todo[0], todo[1])