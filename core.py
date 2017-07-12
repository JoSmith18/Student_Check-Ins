from disk import loadcheckin


def check_day(day):
    checkin = loadcheckin()
    times = []
    for item in checkin:
        if  item[0] == day:
            times.append(item)
    return times
def check_student(student):
    checkin = loadcheckin()
    times = []
    for item in checkin:
        if  item[1] == student:
            times.append(item)
    return times
 

