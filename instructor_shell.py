from disk import checklog, loadstudents
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

def main():
    teacher = input("Which Instructor Will Check Today\n")

    print('Hello Mr.{} What Will You Be Checking Today?\n'.format(teacher))

    
    choice = input_choice() 

    if choice == '1':
        checklog()
    elif choice == '2':
        checklog()
        day = input("What Day Would You Like To Check\n")
        print(check_day(day))
    elif choice == '3':
        print(loadstudents())
        student = input("Which Student Would You Like To See\n")
        print(check_student(student))
    else:
        print("Invalid Start Over")


if __name__ == '__main__':
    main()