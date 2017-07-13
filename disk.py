from datetime import datetime, date, time

def checkin(name):
    with open("checkins.txt","a") as log:
        today = datetime.today()
        log.write("{}, {}, {}\n".format(today.date(), name, today.time()))

def checklog():
    with open("checkins.txt", "r") as file:
        return file.read()

def loadcheckin():
    with open("checkins.txt", "r") as log:
        log.readline()
        check_in = log.readlines()
    inventory = []
    for item in check_in:
        sub_list = item.split(', ')
        inventory.append([sub_list[0].strip(), sub_list[1].strip(), sub_list[2].strip()])
    return inventory

def loadstudents():
    with open("student.txt", "r") as log:
        log.readline()
        return log.readlines()

def valid_student():
    with open("student.txt", "r") as log:
        log.readline()
        check_in = log.readlines()
    students = []
    for item in check_in:
        sub_list = item.split(', ')
        students.append(sub_list[0].strip())
    return students



 

    