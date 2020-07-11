from banner import BANNER
from Main import Academy
import os
import platform


def banner():
    print(BANNER)
    while True:
        inData = input('-> ')
        if inData == 'clear':
            if platform.system() == 'Windows':
                os.system('cls')
                banner()
            else:
                os.system('clear')
                banner()

        if inData == 'exit':
            break

        if inData == 'help':
            print('inqury')
            print('registration')
            print('show students')
            print('update')
            print('delete')
            print('complete course')

        if inData == 'inqury':
            obj = Academy()
            data = obj.inqury()
            for i in data:
                for j in i:
                    print(j+'             ', end='')
                print()

        if inData == 'registration':
            name = input('Enter your name -> ')
            className = input('Enter your class name -> ')
            deposit = input('Enter your deposit -> ')
            installment = input('Enter your installment Y/N -> ')
            fee = input('Enter your fee -> ')
            if installment == 'Y':
                installment = 'True'
            else:
                installment = 'False'
            obj = Academy()
            obj.Registration(name, className, deposit, installment, fee)
            print('\n Registration successfull')

        if inData == 'show students':
            obj = Academy()
            data = obj.display()
            for i in data:
                for j in i:
                    print(j+'             ', end='')
                print()

        if inData == 'update':
            obj = Academy()
            studentName = input('Enter student you wanna update -> ')
            uname = input('Enter student name -> ')
            classname = input('Enter student class name -> ')
            udeposit = input('Enter student deposit -> ')

            if len(uname) > 0 and len(className) > 0 and len(deposit) > 0:
                obj.update(studentName, name=uname,
                           className=classname, deposit=udeposit)
            if len(uname) > 0:
                obj.update(studentName, name=uname)
            if len(classname) > 0:
                obj.update(studentName, name=uname)
            if len(udeposit) > 0:
                obj.update(studentName, name=uname)

        if inData == 'delete':
            obj = Academy()
            sName = input('Enter student name -> ')
            obj.delete(sName)

        if inData == 'complete course':
            obj = Academy()
            sName = input('Enter student name -> ')
            obj.completeCourse(sName)


banner()
