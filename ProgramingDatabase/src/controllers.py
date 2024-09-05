from db import connection, metadata, engine
from services import create_category, get_categories, create_categories, get_category, get_category_by_name, update_category, create_product

#metadata.drop_all(engine, checkfirst=True)
metadata.create_all(engine, checkfirst=True)

def create_category_controller():
    new_category = {
        "name": "Mikiny",
    }
    category = create_category(new_category)
    print(category.id)

def create_categories_controller():
    new_category = [
        {"name": "Čepice",},
        {"name": "Boty",},
        {"name": "Plavky",},
        {"name": "Trička",},
    ]
    result = create_categories(new_category)
    print(result)


def get_categories_controller():
    categories = get_categories()
    print(categories)

def get_category_controller():
    category = get_category(2)
    print(category)

def get_category_by_name_controller():
    category = get_category_by_name("Mikiny")
    print(category)

def upgrade_category_by_id_controller():
    category = update_category(3, {"name": "Sluníčko"})
    print(category)

def create_product_controller():
    category_id = 3

    category = get_category(category_id)

    if not category:
        raise Exception("CATEGORY_NOT_FOUND")

    new_product = {
        "name": "kšiltovka",
        "price": "50",
        "category_id": category_id,
    }
    product = create_product(new_product)
    print(product.id)


#create_category_controller()
#get_categories_controller()
#create_categories_controller()
get_category_controller()
get_category_by_name_controller()
upgrade_category_by_id_controller()
#create_product_controller()

connection.close()