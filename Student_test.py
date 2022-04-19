import unittest
import pytest
from Student import Student

class Student_Test_case(unittest.TestCase):
  def test_student_test_1(self):
    s = Student(1,'RR',[34,56,78,39])
    result=s.calResult([34,56,78,39])
    #print(result)
    self.assertEqual(result,(207,51.75))

  def test_student_test_2(self):
    s = Student(1,'RR',[34,56,78,39])
    result=s.calGrade(s.calResult([34,56,78,39]))
    #print(result)
    self.assertEqual(result,'Second Class')
