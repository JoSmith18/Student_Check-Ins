from disk import load_student, loadcheckin, checkin
from core import check_day, check_student, verifystudents
from random import choice


def input_choice():
    decision = '''
    \t1. All check in times
    \t2. Check in times for a particular day
    \t3. Check in times for a particular student
    '''
    while True:
        choice = input(decision)
        if choice == '1' or choice == '2' or choice == '3':
            return choice
        else:
            print('Invalid Try Again')


def showcheckins(checkins):
    """
    >>> showcheckins([{"Name": "Jo'Tavious", "Date": "2017-07-12", "Time" : "asf"}])
    "Jo'Tavious, 2017-07-12, asf"
    """
    max_l = max(map(lambda d: len(d.get('Name', "")), checkins))
    check_in_str = ''
    for items in checkins:
        padding = ' ' * (max_l - len(items['Name']))
        check_in_str += '{}, {}, {}\n'.format(
            items['Name'], padding + items['Date'], items['Time'])
    return check_in_str.strip()


def showstudents(student):
    str = ''
    for item in student:
        str += item + '\n'
    return str


def dates(checkins):
    res = []
    for items in checkins:
        if items["Date"] not in res:
            res.append(items["Date"])
    return res


def input_name():
    instructors = ['Nate', 'Sean']
    while True:
        teacher = input("Who Will Check Today?\n").strip()
        if teacher in instructors:
            return teacher
        else:
            print('Invalid name')


ran_phrase = [
    lambda name: "Hello Welcome To BCCA {}".format(name),
    lambda name: "Let's Get Started",
    lambda name: "Friday At BaseCamp This Going To Be A Breeze",
    lambda name: "Hey there {}".format(name),
    lambda name: "Goodmorning {}".format(name),
    lambda name: "Let's Have a good and productive day",
    lambda name: "Look At The Time {}".format(name),
    lambda name: "Now Tell Me What You Learned Yesterday {}".format(name)
]


def random_phrase(name):
    return choice(ran_phrase)(name)


def input_name():
    while True:
        name = input("Log In With First and Last Name\n").title()
        valid = load_student()
        if verifystudents(valid, name):
            return name
        else:
            print('Invalid name')


def check_password():
    return '1234' == input('What is the password?\n')


def teacher_main():
    teacher = input("Which admin are you?\n")
    print('Hello Mr.{} What Will You Be Checking Today?\n'.format(teacher))
    choice = input_choice()
    checkins = loadcheckin()
    student = load_student()
    if choice == '1':
        print(showcheckins(checkins))
    elif choice == '2':
        print(dates(checkins))
        day = input("What Day Would You Like To Check\n")
        print(check_day(checkins, day))
    elif choice == '3':
        print(showstudents(student))
        student = input("Which Student Would You Like To See\n")
        print(check_student(checkins, student))
    else:
        print("Sorry We Have To Start Over")


def student_main():
    name = input_name()
    print(random_phrase(name))
    checkin(name)


def main():
    while True:
        choice = input("Are you a student or administrator?\n").title()
        if choice.title() == "Administrator":
            teacher_main()
            break
        elif choice.title() == "Student":
            student_main()
            break
        else:
            print("Invalid Choice!!!\n")
            continue


if __name__ == '__main__':
    main()
