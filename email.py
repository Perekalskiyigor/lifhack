import smtplib

smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
smtpObj.starttls()
smtpObj.login('perekalskiy_igor@mail.ru','Lfdybxb65436(fvsdDDS')
smtpObj.sendmail("justkiddingboat@gmail.com","michael.byrne@vice.com","go to bed!")
smtpObj.quit()