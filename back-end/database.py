import mysql.connector as sql
from data import Product

conn = sql.connect(
    host="localhost",
    user="root",
    password="ABCD@1234",
    database="data"
)

cur = conn.cursor()

def getData():
    products = []
    cur.execute("SELECT * FROM fastdata")
    rows = cur.fetchall()

    for i in rows:
        products.append(
            Product(
                id=i[0],
                name=i[1],
                description=i[2],
                price=i[3],
                quantity=i[4]
            )
        )

    return products
def add_data(product: Product):
    query = """
        INSERT INTO fastdata (id, name, description, price, quantity)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (
        product.id,
        product.name,
        product.description,
        product.price,
        product.quantity
    )

    cur.execute(query, values)
    conn.commit()
    return "record added successfully"

def update_data(id: int, product: Product):
    query = """
        UPDATE fastData
        SET name = %s,
            description = %s,
            price = %s,
            quantity = %s
        WHERE id = %s
    """
    values = (
        product.name,
        product.description,
        product.price,
        product.quantity,
        id
    )
    cur.execute(query, values)
    conn.commit()
    return "Data updated successfully"

def delete_data(id: int):
    query = f"delete from fastdata where id = {id};"
    cur.execute(query)
    return "record deleted suddessfully"