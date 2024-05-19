import requests

import psycopg2
url = 'https://dummyjson.com/products/1'

r = requests.get(url)

print(r.json())


conn = psycopg2.connect(dbname='n47',
                        user='postgres',
                        password='0123',
                        host='localhost',
                        port=5432)


create_table_products_query = """create table products(
        id serial primary key ,
        title varchar(255) ,
        description text ,
        price int,
        discountPercentage float,
        rating float ,
        stock int,
        brand varchar(255),
        category varchar(200),
        thumbnail varchar(255),
        images jsonb
);"""

cur = conn.cursor()
# cur.execute(create_table_products_query)
# conn.commit()

insert_into_query = """insert into products (title, description, price, discountPercentage, rating, stock, brand, category, thumbnail,images)

    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);

"""

for product in r.json()['products']:
    cur.execute(insert_into_query, (
        product['title'], product['description'], product['price'], product['discountPercentage'], product['rating'],
        product['stock'], product['brand'], product['category'], product['thumbnail'], str(product['images'])))
    conn.commit()