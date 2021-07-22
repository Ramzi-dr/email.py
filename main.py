import smtplib
my_email = "email@gmail.com"
my_pass = "password"
with smtplib.SMTP("smtp.gmail.com") as connection
    connection.starttls()
    connection.login(user=my_email,password=my_pass)
    connection.sendmail(from_addr=my_email, to_addrs="ramzi.email@outlook.com",
                        msg="Subject:hello from python\n\nThis is my first body email from python. ")
