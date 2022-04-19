class Student:
    def __init__(self,sid,name,m) -> None:
        self.sid = sid
        self.name = name
        self.m = m

    def calResult(self,m):
        total = sum(m)
        percentage = total/4
        return total,percentage

    def calGrade(self,p):
        (total,p1) = p
        print(p1)
        if p1 >= 90:
            print('Distinction')
            return 'Distinction'
        elif p1 < 90 and p1>=60:
            print('First Class')
            return 'First Class'
        elif p1 < 60 and p1>=50:
            print('Second Class')
            return 'Second Class'
        elif p1< 50 and p1>=40:
            print('Pass')
            return 'Pass'
        else:
            print('Fail')
            return 'Fail'

    
s1 = Student(1,'RR',[23,45,67,1])
#print(s1.calResult([23,45,67,1]))
s1.calGrade(s1.calResult([23,45,67,100]))
