#!C:/Users/pc/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql

connection = pymysql.connect(host="localhost", user="root", password="", database="ddugky")
cur = connection.cursor()

q1 = """select max(slno) from user"""
cur.execute(q1)
r = cur.fetchone()
if r[0] is not None:
    n = r[0]
else:
    n = 0
z = ""
if n < 10:
    z = "000"
elif n < 100:
    z = "00"
elif n < 1000:
    z = "0"
else:
    z = ""
regno = "EMP" + z + str(n + 1)
print("""
    <!doctype html>
        <html>
        <head>
        </head>
            <body>
                <form action="#" method="post">
                    <label for="username">User Id:</label><input type="text" value="%s">
                    <br>
                    <label for="password">Password:</label><input type="password" name='pass'>
                    <br>
                    <label for="mail">Email:</label><input type="mail" name="mailid">
                    <br>
                    <input type="submit" name='sub'>
                </form>
            </body>
        </html>
""" % regno)
import cgi
f = cgi.FieldStorage()
passw = f.getvalue("pass")
mails = f.getvalue("mailid")
sub = f.getvalue("sub")
if sub is not None:
    cur.execute("""insert into user(uname,password,email_id) values ('%s','%s','%s')""" % (regno, passw, mails))
    connection.commit()
    fromaccount = "gsolutions814@gmail.com"
    password = "njgm hplk slvq scsj"
    toaccount = mails
    msg = """This is your User Id :%s""" % regno
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(fromaccount, password)
    server.sendmail(fromaccount, toaccount, msg)
    server.quit()
    print("""
        <script>
        alert("registered successfully and your user id is send to your registered email")
        location.href="login.py;
        </script>
        """)
