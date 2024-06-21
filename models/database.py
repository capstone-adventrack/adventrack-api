from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    with app.app_context():
        db.init_app(app)
        db.create_all()


# import mysql.connector
# from mysql.connector import Error
# from dotenv import load_dotenv
# import os

# load_dotenv()

# def create_connection():
#     try:
#         connection = mysql.connector.connect(
#             host=os.getenv('DB_HOST'),
#             user=os.getenv('DB_USER'),
#             password=os.getenv('DB_PASSWORD'),
#             database=os.getenv('DB_NAME'),
#             unix_socket=os.getenv('DB_SOCKET')
#         )
#         if connection.is_connected():
#             print("Connected to MySQL database")
#             return connection
#     except Error as e:
#         print(f"Error while connecting to MySQL: {e}")
#     return None

# def close_connection(connection):
#     if connection and connection.is_connected():
#         connection.close()
#         print("MySQL connection is closed")
