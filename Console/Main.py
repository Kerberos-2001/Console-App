
class Academy:
    def __init__(self):
        # self.courses = ['Python', 'JAVA', 'C++', 'C', 'Andriod', 'IOS']
        self.file = open('students.txt', 'a')

    def inqury(self):
        self.file = open('courses.txt', 'r')
        data = self.file.read()
        data = data.split('\n')
        self.courses = []
        for i in data:
            self.courses.append(i.split(','))
        return self.courses

    def Registration(self, name, className, deposit, installment, fee):
        self.name = name
        self.clasdName = className
        self.deposit = deposit
        self.installment = installment
        self.installmentFee = 0
        self.fee = fee
        if int(self.deposit) >= 20000 and self.installment == True:
            self.installmentFee = int(self.fee) - 10000
        if len(self.name) > 0 and len(self.clasdName) > 0 and len(self.deposit) > 0 and len(self.fee) > 0:
            self.file.write(self.name+' '+self.clasdName+' '+self.deposit +
                            ' '+self.deposit+' '+self.installment+' '+self.fee+' '+str(self.installmentFee)+'\n')

    def display(self):
        data = open('students.txt', 'r')
        data = data.read()
        data = data.split('\n')
        processedData = []
        for i in data:
            processedData.append(i.split(' '))

        return processedData

    def update(self, updateStudent, **kwargs):
        students = self.display()
        student = []
        for i in students:
            if updateStudent in i:
                student.append(i)
                break

        if len(student) <= 0:
            return 'No Match Found'

        for k, v in kwargs.items():
            if k == 'name':
                student[0][0] = v
            if k == 'className':
                student[0][1] = v
            if k == 'deposit':
                student[0][2]
            if k == 'fee':
                student[0][4] = v

        for i in students:
            if updateStudent in i:
                i = student[0]

        file = open('students.txt', 'w')
        for i in students:
            file.write(i[0])
            for j in range(1, len(i)):
                file.write(' '+i[j])
            file.write('\n')

    def delete(self, studentName):
        data = self.display()
        removeStudent = []
        for i in data:
            if studentName in i:
                pass
            else:
                removeStudent.append(i)

        file = open('students.txt', 'w')
        for i in removeStudent:
            file.write(i[0])
            for j in range(1, len(i)):
                file.write(' '+i[j])
            file.write('\n')

    def completeCourse(self, name):
        data = self.display()
        file = open('students.txt', 'w')
        for i in data:
            if name in i:
                i[2] = '0'
            file.write(i[0])
            for j in range(1, len(i)):
                file.write(' '+i[j])
            file.write('\n')
