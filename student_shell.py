from disk import checkin, load_student
from core import verifystudents
from random import choice 

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

def main():
    name = input_name()
    print(random_phrase(name))
    checkin(name)

if __name__ == '__main__':
    main()

