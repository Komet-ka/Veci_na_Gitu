from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase, declarative_base, relationship

db_user = config("DB_USER")
db_password = config("DB_PASSWORD")
db_host = config("DB_HOST")
db_port = config("DB_PORT")
db_name = config("DB_NAME")

engine = create_engine(
    f"postgresql+psycopg://{db_user}:password@{db_host}:{db_port}/{db_name}?password={db_password}",
    echo=True)


# declarative base
# Session

class Base(DeclarativeBase):
    pass


from sqlalchemy import Column, Integer, Text, ForeignKey


class Kategorie(Base):
    __tablename__ = "kategorie"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)

    products = relationship("Produkt", back_populates="category", lazy="joined")

class Produkt(Base):
    __tablename__ = "produkt"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    category_id = Column(Integer, ForeignKey(Kategorie.id), nullable=False)

    category = relationship("Kategorie", back_populates="products", lazy="joined")

#Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine, checkfirst=True)

with (Session(engine) as session):
    #vytvoření záznamu

    #category = Kategorie(name="Uzeniny")
    #session.add(category)
    #session.commit()

    #načtení záznamu
    result = session.get(Kategorie, 1)
    print(result.id, result.name)

    #načtení více záznamů
    result = session.query(Kategorie.id, Kategorie.name).where(Kategorie.id == 1)
    print(result.first())

    #úprava dat
    #category = session.get(Kategorie,1)
    #category.name = "Lihoviny"
    #session.commit()

    # vytvoreni vice zaznamu
    #categories = [
    #    Kategorie(name="Hracky"),
    #    Kategorie(name="Pocitace"),
    #    Kategorie(name="Telefony"),
    #]

    #session.add_all(categories)
    #session.commit()

    #mazání záznamu
    #category = session.get(Kategorie, 1)
    #session.delete(category)
    #session.commit()

    #vytvoř kategorii a produkt
    #category = Kategorie(name="Uzeniny")
    #session.add(category)
    #session.commit()

    #product = Produkt(name="Klobáska", category_id=category.id)
    #session.add(product)
    #session.commit()

    #category1 = Kategorie(name="Syry")
    # category2 = Category(name="Kategorie 2")

    #product1 = Produkt(name="Emental")
    #product2 = Produkt(name="Gouda")
    #product3 = Produkt(name="Krolewski")

    #category1.products = [
    #    product1,
    #    product2,
    #    product3,
    #]
    #session.add(category1)
    #session.commit()

    #získávání dat
    result = (
        session.query(Produkt)
        .where(Produkt.name == "Gouda")
    )

    gouda = result.first()
    print(gouda.id, gouda.name)


    result = (
        session.query(Produkt.id.label("product_id"), Kategorie.id.label("category_id"))
        .join(Kategorie)
        .where(Produkt.name == "Gouda")
    )

    gouda = result.first()
    print(gouda.product_id, gouda.category_id)


    result = (
        session.query(Produkt)
        .where(Produkt.name == "Gouda")
    )

    gouda = result.first()
    print(gouda.category.name)