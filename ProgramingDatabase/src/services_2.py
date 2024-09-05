from db import categories, products, connection
from sqlalchemy import select, update, delete, insert, asc, desc

#vytvořit kategorii

def create_category(data):
    query = (
        insert(categories)
        .values(name=data["name"])
        .returning(categories.c.id)
    )

    result = connection.execute(query)
    connection.commit()
    return result.first()

data = {
    "name": "Zmrzlina",
}

#create_category(data)

def create_categories(category_list):
    for data in category_list:
        create_category(data)

categ = [
    {"name": "Zahradní náčiní"},
    {"name": "Auta"},
    {"name": "Svítidla"},
    {"name": "Postele"},
]

#create_categories(categ)

def create_categories(data):
    query = (
        insert(categories)
        .values(data)
        .returning(categories.c.id)
    )

    result = connection.execute(query)
    connection.commit()
    return result.all()

def get_category(id):
    query = (
        select(categories)
        .where(categories.c.id == id)
    )
    result = connection.execute(query)
    return result.first()

def get_categories(page, per_page, direction): # chci 10 zaznamu a jsem an druhe strance
    query = (
        select(categories.c.id, categories.c.name)
        .limit(per_page)
        .offset(page * per_page)
        .order_by(asc(categories.c.id))
    )
    if direction == "asc":
        query = query.order_by(asc(categories.c.id))
    else:
        query = query.order_by(desc(categories.c.id))

    result = connection.execute(query)
    return result.all()

cat = get_categories(0,10, "asc")
print(cat)