import sqlite3

# def create_db():
#     con=sqlite3.connect(database=r"register.db")
#     cur=con.cursor()
#     cur.execute("CREATE TABLE register(username,password,email)")
#     con.commit()


# import sqlite3

def run_sql(db_name,sql): #database name and paranthesis passed in
    with sqlite3.connect(db_name) as db: #connects the database with the provided name
        cursor = db.cursor() #creates cursor
        cursor.execute(sql)
        db.commit()

# def create_player():
#     sql="""create table Player
#             (PlayerID integer,
#             Name text,
#             Surname text,
#             Password text,
#             primary key(PlayerID))"""
#     run_sql(db_name,sql)

def create_game():
    sql="""create table Game
            (GameID integer,
            Time Taken text,
            Winner interger,
            primary key(GameID))"""
    run_sql(db_name,sql)

def create_PlayerGame():
    sql = """create table PlayerGame
             (PlayerGameID integer,
             GameID integer,
             PlayerID integer,
             primary key(PlayerGameID)
             foreign key(GameID) references Game(GameID)
             foreign key(PlayerID) references Player(PlayerID)
             on update cascade on delete cascade)"""
    run_sql(db_name,sql)


def query(sql,data):
    with sqlite3.connect("Tic Tac Toe DB.db")as db:
        cursor = db.cursor()
        cursor.execute("pragma foreign_keys = on")
        cursor.execute(sql,data)
        db.commit()

# def insert_product_type_data(records):
#     sql="insert into producttype(description)values(?)"
#     for record in records:
#         query(sql,record)
#
# def insert_product_data(records):
#     sql="insert into product(name, price, producttypeid)values(?,?,?)"
#     for record in records:
#         query(sql,record)
#
# def insert_customer_data(records):
#     sql = "insert into customer(firstname, lastname, street, town, postcode, telephone, email)values(?,?,?,?,?,?,?)"
#     for record in records:
#         query(sql,record)
#
# def insert_customer_order_data(records):
#     sql = "insert into customerorder(date,time)values(?,?)"
#     for record in records:
#         query(sql,record)
#
# def select_all_products():
#     with sqlite3.connect("coffee_shop_relational.db") as db:
#         cursor = db.cursor()
#         cursor.execute("select * from product")
#         products = cursor.fetchall()
#         return products
#         db.commit()
#
# def select_product(id):
#     with sqlite3.connect("coffee_shop_relational.db")as db:
#         cursor = db.cursor()
#         cursor.execute("select * from product where productid=?",(id,))
#         product = cursor.fetchone()
#         return product
#
if __name__ == "__main__": #call to main
    
    db_name = "Tic _Tac_Toe.db"
    # create_player()
    # create_game()
    create_PlayerGame()

