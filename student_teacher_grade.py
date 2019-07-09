import sys
from collections import Counter

class Person(object):

    def __init__(self,grade):
        self.grade = grade

    def get_grade(self):
        return self.grade

class Student(Person):

    def __init__(self,grade):
        Person.__init__(self,grade)

    def get_grade(self):
        x = Counter(self.grade)
        return "Pass: {},　Fail: {}".format(len(self.grade)-x['D'],x['D'])

class Teacher(Person):

    def __init__(self,grade):
        Person.__init__(self,grade)
    
    def get_grade(self):
        result = []
        grades = Counter(self.grade).most_common(4)
        for key, value in grades:
            s = key + ": "+ str(value)
            result.append(s)
        return ",".join(result)

if __name__ == '__main__':
    if sys.argv[1] == 'Student':
        student = Student(sys.argv[2])
        print(student.get_grade())
    else:
        teacher = Teacher(sys.argv[2])
        print(teacher.get_grade())



