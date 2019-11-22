import unittest
from social_network import SocialNet as SocialNet
from fastt import FASTT
from student import Student 
from task import Task 

class TestFastt(unittest.TestCase):

    def setUp(self):
        stu1 = Student(
            "richie", ["tennis", "hawks", "camping", "drama"], ["eli", "margot"], ["raleigh"], ["margot"], "eli")
        stu2 = Student(
            "margot", ["cigarettes", "lying", "camping"], ["richie", "raleigh", "eli"], ["dudley"], ["richie"], "richie")
        task1 = ("margot", ["drama", "lying", "cigarettes"])
        task2 = ("richie", ["camping", "drama", "tennis"])
        fst = FASTT([task1, task2], [stu1, stu2])
        print("okay")

    def test_test(self):
        print("okay")

if __name__ == '__main__':
    unittest.main()