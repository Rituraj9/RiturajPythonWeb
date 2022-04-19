class Student:
    def __init__(self,sid,name,m) -> None:
        self.sid = sid
        self.name = name
        self.m = m
    def calResult(self,m):
        total = sum(m)
        percentage = total/4
        return total,percentage
    
s1 = Student(1,'RR',[23,45,67,1])
print(s1.calResult([23,45,67,1]))
