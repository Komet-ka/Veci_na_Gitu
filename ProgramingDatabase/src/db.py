from decouple import config
from sqlalchemy import create_engine, MetaData, Table, Column, Numeric, ForeignKey
from sqlalchemy import Integer, Text, insert, select

db_user = config("DB_USER")
db_password = config("DB_PASSWORD")
db_host = config("DB_HOST")
db_port = config("DB_PORT")
db_name = config("DB_NAME")

engine = create_engine(
    f"postgresql+psycopg://{db_user}:password@{db_host}:{db_port}/{db_name}?password={db_password}",
    echo=True)

metadata = MetaData()

connection = engine.connect()

categories =Table(
    "categories",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", Text, nullable=False),
)

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", Text, nullable=False),
    Column("price", Numeric, nullable=False),
    Column("category_id", ForeignKey(categories.c.id, ondelete="CASCADE"), nullable=False),
)

#metadata.drop_all(engine, checkfirst=True)
#metadata.create_all(engine, checkfirst=True)