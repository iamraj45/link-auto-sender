from script import send, send1, send2, send3
import schedule
import time

#TAFL
schedule.every().monday.at("03:40").do(send)
schedule.every().tuesday.at("08:30").do(send)
schedule.every().wednesday.at("04:40").do(send)

#Maths
schedule.every().monday.at("04:40").do(send1)
schedule.every().tuesday.at("05:45").do(send1)
schedule.every().thursday.at("08:30").do(send1)
schedule.every().friday.at("06:45").do(send1)

#Microprocessor
schedule.every().monday.at("05:45").do(send2)
schedule.every().tuesday.at("03:40").do(send2)
schedule.every().wednesday.at("06:45").do(send2)
schedule.every().thursday.at("05:45").do(send2)
schedule.every().friday.at("03:40").do(send2)

#Mentoring
schedule.every().friday.at("05:45").do(send3)

while True:
    schedule.run_pending()
    time.sleep(1)
