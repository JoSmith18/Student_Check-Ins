from disk import checkin
from core import verifystudents

def input_name():
    while True:
        name = input("Log In With First and Last Name\n").title()
        if verifystudents(name):
            return name
        else:
            print('Invalid name')

def main():
    name = input_name()
    checkin(name)

if __name__ == '__main__':
    main()

