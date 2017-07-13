from disk import load_student,loadcheckin
from core import check_day,check_student

def input_choice():
    decision = '''
    \t1. All check in times
    \t2. Check in times for a particular day
    \t3. Check in times for a particular student
    '''
    while True:
        choice = input(decision)
        if choice == '1'  or choice == '2' or choice == '3':
            return choice 
        else:
            print('Invalid Try Again')

def showcheckins(checkins):
    str = ''
    for item in checkins:
        str +=' - '.join(item) + '\n'
    return str

def showstudents(student):
    str = ''
    for item in student:
        str += item + '\n'
    return str

def main():
    teacher = input("Who Will Check Today?\n")
    
    print('Hello Mr.{} What Will You Be Checking Today?\n'.format(teacher))    
    
    choice = input_choice() 
    checkins = loadcheckin()
    student = load_student()

    if choice == '1':
        print(showcheckins(checkins))
    
    elif choice == '2':
        print(showcheckins(checkins))
        day = input("What Day Would You Like To Check\n")
        print(check_day(checkins, day))
    
    elif choice == '3':
        print(showstudents(student))
        student = input("Which Student Would You Like To See\n")
        print(check_student(checkins, student))

if __name__ == '__main__':
    main()
    