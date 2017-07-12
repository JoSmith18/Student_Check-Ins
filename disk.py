from datetime import datetime

def checkin(name):
    with open("checkins.txt","a") as log:
        log.write("{}, {}\n".format(datetime.today(), name))

def checklog():
    with open("checkins.txt", "r") as file:
        print(file.read())