import unittest
import repo

class test_repo(unittest.TestCase):
    def setUp(self):
        self.a = 5
        self.b = 2
        self.ret = [7, 3, 10, 2.5, 1]
        self.cal = repo.Cal(self.a, self.b)

    def test_add(self):
        ret_add = repo.Cal(self.a, self.b).add()
        self.assertEqual(ret_add, self.ret[0])

    def test_all(self):
        ret_all = [self.cal.add(), self.cal.sub(), self.cal.mul(), self.cal.div(), self.cal.mod()]
        self.assertEqual(self.ret, ret_all)



if __name__=="__main__":
    print("Testing the validation of class cal in repo.py...")
    unittest.main()