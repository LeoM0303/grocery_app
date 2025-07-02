from http.client import responses

import mysql.connector

def get_all_prod(connection):
   cursor = connection.cursor

    cursor.execute(queue)

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

    cnx.close()
    return response
if __name__ == '__main__':
    print(get_all_prod())