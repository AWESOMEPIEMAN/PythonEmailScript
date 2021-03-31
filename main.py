import smtplib, ssl

sender_email = ' '
receiver_email = ' '

passw = input('Please input your password : ')

#Email section
email_html = open('email_y.html')
email_Body = email_html.read()
print('Sending email....')

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)

    context = ssl.create_default_context()
    server.starttls(context=context)

    server.login(sender_email,passw)

    server.sendmail(sender_email,receiver_email,email_Body)
    print('The Email has been sent')
except Exception as e:
    print(f"Oh looks like something went wrong {e}")
finally:
    print('Closing the server client..')
    server.quit()
