from datetime import datetime

def checkin(name):
    with open("checkins.txt","a") as log:
        log.write("{}, {}\n".format(datetime.today(), name))