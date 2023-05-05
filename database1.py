import mysql.connector
from mysql.connector import Error

db_name = "voter"
def connecting_db(host_name , user_name , user_password , db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("voter's Database is connected succesfully ")
    except Error as err:
        print(f"Error : {err}")
    return connection    
def execute_query(connection,query):
    connection = connecting_db("localhost","root","root",db_name)        
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchone()[0]
        connection.commit()
        print("Query executed successfully \n" + result)
    except IndexError as err:
        result = None
    except TypeError as err:
        result = None
    return result
# validation = """select password from admin where adminID = 10556;"""
# amythiing = execute_query(None, validation)   
# print(amythiing)
# usr should be taken from pyqt
#pwd same
# connection = connecting_db("localhost","root","root",db_name)  

# execute_query(connection=connecting_db("localhost","root","root",db_name) , query=validation)
# def creating_new_user(usr,pwd):
#     creating_new_user = f"""
#     insert into user values ({userID} , {password} );""" 
#     execute_query(connection,creating_new_user)