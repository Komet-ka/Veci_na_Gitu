from sqlalchemy import select, insert, delete, update
from db import categories, products, connection

def create_category(data):
    query = (
        insert(categories)
        .values(name=data["name"])
        .returning(categories.c.id)
    )

    result = connection.execute(query)
    connection.commit()
    return result.first()

def create_categories(data):
    query = (
        insert(categories)
        .returning(categories.c.id)
    )

    result = connection.execute(query, data)
    connection.commit()
    return result.all()

def get_category(id):
    query = (
        select(categories.c.id, categories.c.name)
        .where(categories.c.id == id)
    )
    result = connection.execute(query)
    return result.first()

def get_categories():
    query = (
        select(categories)
    )
    result = connection.execute(query)
    return result.all()

def get_category_by_name(name):
    query = (
        select(categories.c.id, categories.c.name)
        .where(categories.c.name == name)
    )
    result = connection.execute(query)
    return result.first()

def update_category(id, data):
    query = (
        update(categories)
        .values(name=data["name"])
        .where(categories.c.id == id)
        .returning(categories.c.id, categories.c.name)
    )
    result = connection.execute(query)
    connection.commit()

    return result.all()

def create_product(data):
    query = (
        insert(products)
        .values(name=data["name"], price=data["price"], category_id=data["category_id"])
        .returning(products.c.id)
    )

    result = connection.execute(query)
    connection.commit()
    return result.first()

def get_product(product_id):
    query = (
        select(products.c.id, products.c.name, products.c.price)
        .where(products.c.id == product_id)
    )
    result = connection.execute(query)
    return result.first()