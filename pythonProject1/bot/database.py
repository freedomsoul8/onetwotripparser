import sqlite3

conn = sqlite3.connect('db', check_same_thread=False)
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE users(user_id int)""")
# cursor.execute("""CREATE TABLE subscriptions(user_id int, depart text, dest text, date_from text, date_back text, price_lim int)""")

def add_subscription(depart_city, dest_city, date_depart, date_back, price_lim, user_id):
    sql =  "INSERT INTO subscriptions (user_id, depart, dest, date_from, date_back, price_lim) VALUES (?,?,?,?,?,?)"
    val = (user_id, depart_city, dest_city, date_depart, date_back, price_lim)
    cursor.execute(sql, val)
    conn.commit()


# cursor.execute("INSERT INTO subscriptions VALUES (1,1,1,1,1,1)")
# conn.commit()

# cursor.execute("""CREATE TABLE cities(city_code int, city_name text)""")

def search_city_code(city_name):
    sql = """SELECT city_code FROM cities WHERE city_name=?"""
    val = (city_name,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    conn.commit()


    return result[0]

# search_city_code(city_name='Москва')
