import smtplib

smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
smtpObj.starttls()
smtpObj.login('perekalskiy_igor@mail.ru','Lfdybxb65436(fvsdDDS')
smtpObj.sendmail("justkiddingboat@gmail.com","perekalskiy_igor@mail.ru","go to bed!")
smtpObj.quit()