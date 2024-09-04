import unittest
import grin


class Test_Go(unittest.TestCase):

    def test_gosub(self):
        val = {}
        lis = ['GOSUB 2', '.']
        p = 0
        expected_p = 1
        lis_2 = []
        labels = {}
        for i in grin.parse(lis):
            lis_2.append(grin.GoSub(i, val, p, labels).gosub_run())
        self.assertEqual(expected_p, lis_2[0])

    def test_gosub_cond(self):
        val = {"A": 0, "B": 5}
        lis = ['GOSUB 10 IF 5 = 6', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        for i in grin.parse(lis):
            lis_2.append(grin.GoSub(i, val, p, labels).gosub_run())
        self.assertEqual(expected_p, lis_2[0])

    def test_gosub_return(self):
        val = {"A": 0, "B": 5}
        lis = ['GOSUB 10 IF 5 = 6', '.']
        p = 0
        lis_2 = []
        labels = {}
        ret_lis = [2]
        expected_p = 2
        for i in grin.parse(lis):
            lis_2.append(grin.Return_sub(i, val, p, labels, ret_lis).gosub_return())
        self.assertEqual(expected_p, lis_2[0])

    def test_gosub_return_1(self):
        val = {"A": 0, "B": 5}
        lis = ['GOSUB 10 IF 5 = 6', '.']
        p = 0
        lis_2 = []
        labels = {}
        ret_lis = []
        expected_p = 2
        try:
            for i in grin.parse(lis):
                lis_2.append(grin.Return_sub(i, val, p, labels, ret_lis).gosub_return())
        except Exception as e:
            self.assertEqual("No GoSub encountered", str(e))

if __name__ == '__main__':
    unittest.main()