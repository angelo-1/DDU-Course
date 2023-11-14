#!C:/Users/pc/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
#
# # Creating Database
#
# connection = pymysql.connect(host="localhost", user="root", password="", database="")
# cur = connection.cursor()
# q = """create database ddugky"""
# cur.execute(q)
# connection.commit()
# print("""
# <script>
# alert("database created...")
# </script>
# """)
# connection.close()

# Creating Table

# connection = pymysql.connect(host="localhost", user="root", password="", database="ddugky")
# cur = connection.cursor()
# q = """create table user(slno int(20)auto_increment primary key,uname varchar(50),password varchar(50))"""
# cur.execute(q)
# connection.commit()
# print("""
# <script>
# alert("table created...")
# </script>
# """)
# connection.close()

# Inserting Values

# connection = pymysql.connect(host="localhost", user="root", password="", database="ddugky")
# cur = connection.cursor()
# cur.execute("""insert into user(uname,password) values ('angelo','Ang@1')""")
# connection.commit()
# print("""
# <script>
# alert("values imported...")
# </script>
# """)
# connection.close()
