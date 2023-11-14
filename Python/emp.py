#!C:/Users/angelo/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi

connection = pymysql.connect(host="localhost", user="root", password="", database="ddugky")
cur = connection.cursor()

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Registration</title>
    <link rel="stylesheet" href="./assets/css/style.css">
</head>
<body>
    <div class="container">
        <h1>Employee Registration</h1>
        <form action="#" method="get">
            <label for="name">Name:</label>
            <input type="text" name="empname" placeholder="Employee name">
            <label for="email">Email:</label>
            <input type="email" name="mail" placeholder="Employee mail">
            <label for="phone">Phone:</label>
            <input type="text" name="phone" placeholder="Employee Phone">
            <label for="password">Password:</label>
            <input type="password" name="pass">
            <label for="gen">Gender:</label> <br>
            <span class="spans">Male:</span><input type="radio" name="gen" value="male">
            <span class="spans">Female:</span><input type="radio" name="gen" value="female">
            <label for="exp">Experience:</label>
            <input type="number" name="exp">
            <label for="salary">Salary:</label>
            <input type="number" name="salary">
            <input type="submit" name="submit" class="subbutton">
        </form>
    </div>
</body>
</html>""")

f = cgi.FieldStorage()
empname = f.getvalue("empname")
empmail = f.getvalue("mail")
empphone = f.getvalue("phone")
emppass = f.getvalue("pass")
empgen = f.getvalue("gen")
empexp = f.getvalue("exp")
empsal = f.getvalue("salary")
sub = f.getvalue("submit")
if sub is not None:
    cur.execute("""insert into employee(empname,empmail,empphone,emppass,empgender,empexp,empsal) 
    values('%s','%s','%s','%s','%s','%s','%s')""" % (empname, empmail, empphone, emppass, empgen, empexp, empsal))
    connection.commit()
    print("""
        <script>
        alert("Employee Registration Successful")
        </script>
        """)

# connection = pymysql.connect(host="localhost", user="root", password="", database="ddugky")
# cur = connection.cursor()
# q = """create table employee(slno int(20)auto_increment primary key,empname varchar(50),empmail varchar(50),
# empphone varchar(50),emppass varchar(50), empgender varchar(20),empexp int(20),empsal int(30))"""
# cur.execute(q)
# connection.commit()
# print("""
# <script>
# alert("table created...")
# </script>
# """)
# connection.close()
