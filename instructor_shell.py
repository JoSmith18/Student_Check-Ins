from disk import checklog
from core import action
teacher = input("Which Instructor Will Check Today\n")

print('Hello Mr.{} What Will You Be Checking Today?\n'.format(teacher))

decision = '''
\t1. All check in times
\t2. Check in times for a particular day
\t3. Check in times for a particular student
'''
choice = input(decision) 
action(choice)