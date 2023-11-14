#!C:/Users/angelo/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi

connection = pymysql.connect(host="localhost", user="root", password="", database="ddugky")
cur = connection.cursor()

print("""
    <!doctype html>
        <html>
            <body>
                <form action="#" method="post">
                    <label for="username">Username:</label><input type="text" name='uname'>
                    <br>
                    <label for="password">Password:</label><input type="password" name='pass'>
                    <br>
                    <input type="submit" name='sub'>
                </form>
            </body>
        </html>
""")
f = cgi.FieldStorage()
usname = f.getvalue("uname")
passw = f.getvalue("pass")
sub = f.getvalue("sub")
if sub is not None:
    cur.execute("""insert into user(uname,password) values ('%s','%s')""" % (usname, passw))
    connection.commit()
    print("""
    <script>
    alert("registered succesfully...")
    </script>
    """)
