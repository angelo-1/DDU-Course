#!C:/Users/pc/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi
g = cgi.FieldStorage()
pid = g.getvalue("slo")
print(pid)


connection = pymysql.connect(host="localhost", user="root", password="", database="ddugky")
cur = connection.cursor()
cur.execute("""select * from user where slno='%s'""" % pid)
f = cur.fetchall()
# print(f)
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Showing data</title>
</head>
<body>
    <div >
        <table >
        <tr>
        <th>slno</th>
        <th>username</th>
        <th>password</th>
        </tr>""")
for r in f:
    print("""
        <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        </tr>
    </div>
</body>
</html>
""" % (r[0], r[1], r[2]))
