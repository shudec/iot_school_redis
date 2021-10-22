from EcoleIotRedis import r
import unittest

class TestRedisExercices(unittest.TestCase):

    def test_ex0(self):
        self.assertEqual(r.get("ext:line:count"), "2224")

    def test_ex1(self):
        self.assertEqual(r.get("ext:temperature:1600032600"), "18.1")

    def test_ex2(self):
        self.assertEqual(r.llen("ext:timestamps"), 2224)
        self.assertEqual(r.llen("ext:temperatures"), 2224)
        self.assertEqual(len(r.smembers("ext:alldata")), 2224)

    def test_ex3(self):
        self.assertEqual(r.get("ext:temperature:max"), "37.1")
        self.assertEqual(r.get("ext:temperature:min"), "-1.2")

    def test_ex4(self):
        self.assertEqual(round(float(r.get("ext:temperatures:month:mean:1")),2), 6.39)

    def test_ex5(self):
        self.assertEqual(len(r.zrange("ext:days", 0, -1)), 280)

if __name__ == '__main__':
    unittest.main()