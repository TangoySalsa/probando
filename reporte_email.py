import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("tangobugnot@gmail.com", "Success2018")

msg = "YOUR MESSAGE!"
server.sendmail("YOUR EMAIL ADDRESS", "THE EMAIL ADDRESS TO SEND TO", msg)
server.quit()
