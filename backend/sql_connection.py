cnx = mysql.connector.connect(user='root', password='riki2303',
                              host='127.0.0.1',
                              database='gs')

cursor = cnx.cursor()

queue = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
         "FROM products inner join uom on products.uom_id=uom.uom_id")
