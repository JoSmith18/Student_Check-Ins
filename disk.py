from datetime import datetime, date, time

def checkin(name):
    with open("checkins.txt","a") as log:
        today = datetime.today()
        log.write("{}, {}, {}\n".format(today.date(), name, today.time()))

def checklog():
    with open("checkins.txt", "r") as file:
        print(file.read())