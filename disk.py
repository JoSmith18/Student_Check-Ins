from datetime import datetime, date, time

def checkin(name):
    with open("checkins.txt","a") as log:
        today = datetime.today()
        log.write("{}, {}, {}\n".format(today.date(), name, today.time()))

def loadcheckin():
    with open("checkins.txt", "r") as log:
        key_1, key_2, key_3 = log.readline().strip().split(', ')
        check_in = log.readlines()
    inventory = []
    for item in check_in:
        date, name, time = item.strip().split(', ')
        d = {key_1: date, key_2: name, key_3: time}
        inventory.append(d)
    return inventory

def load_student():
    with open("student.txt", "r") as log:
        log.readline()
        check_in = log.readlines()
    students = []
    for item in check_in:
        sub_list = item.split(', ')
        students.append(sub_list[0].strip())
    return students



 

    