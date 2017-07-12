from disk import checklog, check_for_day, check_for_student

def action():
        checklog()
def check_day(day):
    check_for_day(day)
    times = []
    for item in check_in:
        if  item[0] == day:
            return item
def check_student(student):
    check_for_student(student)
    times = []
    for item in check_in:
        if  item[1] == day:
            return item
 

