#!C:/Users/pc/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi

connection = pymysql.connect(host="localhost", user="root", password="", database="ddugky")
cur = connection.cursor()
import pymysql
import cgi

connection = pymysql.connect(host="localhost", user="root", password="", database="ddugky")
cur = connection.cursor()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Form</title>
    <link rel="stylesheet" href="./assets/css/login.css">
</head>
<body>
    <div>
        <div class="div1"></div>
        <div class="lform">
            <form method="post" action="#">
                <h2 style="text-align: center;">Login Here!</h2>
                <label>UserName:</label> <br> <input type="text" name="username" required> <br>
                <label>Password:</label> <br> <input type="password" name="password" required> <br>

                <input type="submit" value="Login" name="log">
                <p style="text-align: end;">Not a member? <a href="./userregister.py">Create Account</a></p>
                <p style="text-align: start; margin-top: -55px;"><a href="#">Forget Password</a></p>

            </form>
        </div>
    </div>
</body>
</html>
""")
a = cgi.FieldStorage()
uname = a.getvalue("username")
passw = a.getvalue("password")
sub = a.getvalue("log")

if sub is not None:
    q = """select slno from user where uname='%s' and password='%s'""" % (uname, passw)
    cur.execute(q)
    r = cur.fetchone()
    if r is not None:
        print("""
        <script>
        alert("login successful");
        location.href="slctdtasql.py?slo=%s";
        </script>
        """ % r)
    else:
        print("""
        <script>
        alert("Wrong password or username");
        </script>
        """)
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Form</title>
    <link rel="stylesheet" href="./assets/css/login.css">
</head>
<body>
    <div>
        <div class="div1"></div>
        <div class="lform">
            <form method="post" action="#">
                <h2 style="text-align: center;">Login Here!</h2>
                <label>UserName:</label> <br> <input type="text" name="username" required> <br>
                <label>Password:</label> <br> <input type="password" name="password" required> <br>

                <input type="submit" value="Login" name="log">
                <p style="text-align: end;">Not a member? <a href="./userregister.py">Create Account</a></p>
                <p style="text-align: start; margin-top: -55px;"><a href="#">Forget Password</a></p>
                
            </form>
        </div>
    </div>
</body>
</html>
""")
a = cgi.FieldStorage()
uname = a.getvalue("username")
passw = a.getvalue("password")
sub = a.getvalue("log")

if sub is not None:
    q = """select slno from user where uname='%s' and password='%s'""" % (uname, passw)
    cur.execute(q)
    r=cur.fetchone()
    if r is not None:
        print("""
        <script>
        alert("login successful");
        location.href="slctdtasql.py?slo=%s";
        </script>
        """ % r)
    else:
        print("""
        <script>
        alert("Wrong password or username");
        </script>
        """)

