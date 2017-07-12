from disk import checklog
from core import check_day,check_student
teacher = input("Which Instructor Will Check Today\n")

print('Hello Mr.{} What Will You Be Checking Today?\n'.format(teacher))

decision = '''
\t1. All check in times
\t2. Check in times for a particular day
\t3. Check in times for a particular student
'''
choice = input(decision) 

if choice == '1':
    checklog()
elif choice == '2':
    day = input("What Day Would You Like To Check\n")
    print(check_day(day))
elif choice == '3':
    student = input("Which Student Would You Like To See\n")
    print(check_student(student))

