topper = {}
failed = {}
unique = set()
class Stud:
    information = {}
    def __init__(self):
        self.name = ''
        self.marks = 0
        n = int(input('Enter the number of students:'))
        self.info(n)
    def info(self,n):
        sum = 0
        max = 0
        name = ''
        for i in range(n):
            self.name = input('Enter the name of student:')
            self.marks = int(input('Enter the marks:'))
            self.information[self.name] = self.marks
            sum = sum + self.marks
            if self.marks<40:
                failed[self.name] = self.marks
            if self.marks>max :
                max = self.marks
                name = self.name
            unique.add(self.marks)
        topper[name] = max
        average = sum/n
        print('Students:',self.information)
        print('Average marks of class:',average)
        print('Failed students:',failed)
        print('Topper:',topper)
obj = Stud()
print('Unique marks in class:',unique)