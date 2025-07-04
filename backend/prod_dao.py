from itertools import product

from sql_connection import get_sql_connection

def get_all_prod(connection):
    cursor = connection.cursor()

    query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
             "FROM products inner join uom on products.uom_id=uom.uom_id")

    cursor.execute(query)

    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
       response.append(
           {
               'product_id': product_id,
               'name': name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name,
           }
       )

    return response

def insert_new_prod(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products (name, uom_id, price_per_unit) "
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], int(product['uom_id']), float(product['price_per_unit']))
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 11))