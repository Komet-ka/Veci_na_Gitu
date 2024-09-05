from decouple import config
from sqlalchemy import create_engine, MetaData, Table, Column


db_user = config("DB_USER")
db_password = config("DB_PASSWORD")
db_host = config("DB_HOST")
db_port = config("DB_PORT")
db_name = config("DB_NAME")

engine = create_engine(
    f"postgresql+psycopg://{db_user}:password@{db_host}:{db_port}/{db_name}?password={db_password}",
    echo=True)

metadata = MetaData()

from sqlalchemy import Integer, Text, insert, select

todos_2 = Table(
    "todos_2",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("label", Text, nullable=False),
    Column("description", Text, nullable=False),
)

#metadata.drop_all(engine, checkfirst=True)
#metadata.create_all(engine, checkfirst=True)

todos_data = [
    {"label": "Koupit kečup", "description": "Večer budou hranolky"},
    {"label": "Vyvenčit psa", "description": "2x každý den"},
    {"label": "Zajet na chatu", "description": "posbírat jahody"},
    {"label": "Koupit teplaky synovi", "description": "Rval se sousedem a roztrhl si je"},
    {"label": "Vyluxovat auto", "description": "na chalupě"},
]

#with engine.connect() as connection:
    # connection.execute(text("DEALLOCATE _pg3_0;"))
#    def create_todo(todo):
#        query = (
#            insert(todos_2)
#            .values(label=todo["label"], description=todo["description"])


#            connection.execute(query)
#            connection.commit()


#        create_todo({"label": "Koupit tatarku", "description": "Vecer budou krokety"})
#        )

#    connection.execute(insert(todos_2), todos_data)
#    connection.commit()
    #print(connection)

with engine.connect() as connection:
    query = (
#        select(todos_2)
        select(todos_2.c.id, todos_2.c.label)
        .where(todos_2.c.id == 1)
    )
    result = connection.execute(query)

    for row in result:
#        print(row.id, row.label, row.description)
        print(row.id, row.label)

# Pristup c.1

    query = (
        select(todos_2.c.id, todos_2.c.label)  # SELECT id, label FROM todos;
        .where(todos_2.c.id == 1)  # WHERE id = 1;
    )

    result = connection.execute(query)
    data = result.all()
    # tady muze byt cokoliv
    print(data)

# Pristup c.2

    query = (
        select(todos_2.c.id, todos_2.c.label)  # SELECT id, label FROM todos;
        .where(todos_2.c.id == 1)  # WHERE id = 1;
    )

    result = connection.execute(query)
    for row in result:  # mam v planu s temi daty neco delat ihned
        print(row)

# Pristup c.3 - Funkce

    def get_todo_by_id(id):
        query = (
            select(todos_2.c.id, todos_2.c.label)  # SELECT id, label FROM todos;
            .where(todos_2.c.id == id)  # WHERE id = 1;
        )

        result = connection.execute(query)
        return result.all()