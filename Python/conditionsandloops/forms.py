print("content-type:text/html \n\r\n\r")
a = 10
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>forms</title>
    <link rel="stylesheet" href="forms.css">
</head>
<body>
   <form method="post" action="#" target="_blank">
        <h1 style="text-align: center;">This is a form</h1>
        <label>Name:</label> <br> <input type="text" name="name" placeholder="enter your name" required><br>
        <label>password:</label> <br> <input type="password" name="password" placeholder="enter your password" required><br>
        <label>Email:</label> <br> <input type="email" name="email" placeholder="enter your Email" required><br>
        <label>Phone:</label> <br> <input type="number" name="phone" placeholder="enter your Phone number" required><br>
        <label >Adress:</label> <br> <textarea name="" id="" cols="20px" rows="3px"></textarea> <br>
        <label >Files:</label> <br> <input type="file"><br>
        <label >Time:</label> <br> <input type="time"><br>
        <label >Date:</label> <br> <input type="date"><br>
        <label >Date & Time:</label> <br> <input type="datetime-local"><br>
        <label >Color:</label> <br> <input type="color"><br>
        <label >Gender:</label> <br><label >Male</label> <input type="radio" name="gender" value="male"> <label>Female</label><input type="radio" name="gender" ><br>
        <label >Hobbies:</label><br> <label>Football</label> <input type="checkbox"><label>Movies</label> <input type="checkbox"><label>Music</label> <input type="checkbox"><br>
        <label >Select box:</label> <br>
        <select size="5">
            <option value="">option1</option>
            <option value="">option2</option>
            <option value="">option3</option>
            <option value="">option4</option>
            <option value="">option5</option>
            <option value="">option6</option>
        </select>
        <br>
        <input type="submit">
        <input type="reset" disabled>
    </form>
</body>
</html>""")
