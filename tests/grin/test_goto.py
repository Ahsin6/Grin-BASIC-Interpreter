import unittest
import grin


class Test_GoTo(unittest.TestCase):

    def test_goto(self):
        val = {}
        lis = ['GOTO 2', '.']
        p = 0
        expected_p = 1
        lis_2 = []
        labels = {}
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).goto_run_index())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_2(self):
        val = {"A": 5}
        lis = ['GOTO A', '.']
        p = 0
        expected_p = 4
        labels = {}
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).goto_run_index())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_3(self):
        val = {"A": 5}
        lis = ['GOTO 0', '.']
        p = 0
        lis_2 = []
        labels = {}
        try:
            for i in grin.parse(lis):
                lis_2.append(grin.Goto(i, val, p, labels).goto_run_index())
        except Exception as e:
            self.assertEqual("Cant jump to zero", str(e))

    def test_goto_4(self):
        val = {"A": 5}
        lis = ['GOTO B', '.']
        p = 0
        lis_2 = []
        labels = {}
        try:
            for i in grin.parse(lis):
                lis_2.append(grin.Goto(i, val, p, labels).goto_run_index())
        except Exception as e:
            self.assertEqual("Cant jump to zero", str(e))

    def test_goto_5(self):
        val = {"A": 0}
        lis = ['GOTO A', '.']
        p = 0
        lis_2 = []
        labels = {}
        try:
            for i in grin.parse(lis):
                lis_2.append(grin.Goto(i, val, p, labels).goto_run_index())
        except Exception as e:
            self.assertEqual("Cant jump to zero", str(e))

    def test_goto_cond(self):
        val = {}
        lis = ['GOTO 2 IF 2 < 3', '.']
        p = 0
        expected_p = 1
        lis_2 = []
        labels = {}
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_2(self):
        val = {"A": 5, "B": 10}
        lis = ['GOTO A IF B >= 10', '.']
        p = 0
        expected_p = 4
        lis_2 = []
        labels = {}
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_3(self):
        val = {"A": 0}
        lis = ['GOTO 10 IF B <= 0', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 9
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_4(self):
        val = {"A": 5}
        lis = ['GOTO B IF A <= 10', '.']
        p = 0
        lis_2 = []
        labels = {}
        try:
            for i in grin.parse(lis):
                lis_2.append(grin.Goto(i, val, p, labels).check_if())
        except Exception as e:
            self.assertEqual("Cant jump to zero", str(e))

    def test_goto_cond_5(self):
        val = {"A": 0}
        lis = ['GOTO A IF A <= 0', '.']
        p = 0
        lis_2 = []
        labels = {}
        try:
            for i in grin.parse(lis):
                lis_2.append(grin.Goto(i, val, p, labels).check_if())
        except Exception as e:
            self.assertEqual("Cant jump to zero", str(e))

    def test_goto_cond_6(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF B < 0', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_7(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF B < 6', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 9
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_8(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF B > 0', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 9
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_9(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF B > 6', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_10(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF B >= 6', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_11(self):
        val = {"A": 0, "B": 8}
        lis = ['GOTO 10 IF B <= 6', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_12(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF B = 5', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 9
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_13(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF B = 6', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_14(self):
        val = {"A": 0, "B": 7}
        lis = ['GOTO 10 IF B <> 5', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 9
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_15(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF B <> 5', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_16(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF 2 < 0', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_17(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF 5 < 6', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 9
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_18(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF 5 > 0', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 9
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_19(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF 5 > 6', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_20(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF 5 >= 6', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_21(self):
        val = {"A": 0, "B": 8}
        lis = ['GOTO 10 IF 8 <= 6', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_22(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF 5 = 5', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 9
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_23(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF 5 = 6', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_24(self):
        val = {"A": 0, "B": 7}
        lis = ['GOTO 10 IF 7 <> 5', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 9
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_25(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF 5 <> 5', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_26(self):
        val = {"A": 0, "B": 8}
        lis = ['GOTO 10 IF 5 <= 6', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 9
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_27(self):
        val = {"A": 0, "B": 8}
        lis = ['GOTO 10 IF 8 >= 6', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 9
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_28(self):
        val = {"A": 0, "B": 8}
        lis = ['GOTO "H"',  '.']
        p = 0
        lis_2 = []
        labels = {"H": 3}
        expected_p = 1
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).goto_run_index())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_29(self):
        val = {"A": 0, "B": 8}
        lis = ['GOTO "H"',  '.']
        p = 0
        lis_2 = []
        labels = {"H": 0}
        expected_p = -2
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).goto_run_index())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_30(self):
        val = {"A": 0, "B": 8}
        lis = ['GOTO "H"',  '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        try:
            for i in grin.parse(lis):
                lis_2.append(grin.Goto(i, val, p, labels).goto_run_index())
        except Exception as e:
            self.assertEqual("Label does not exist", str(e))

    def test_goto_cond_31(self):
        val = {"A": "H", "B": 8}
        lis = ['GOTO A', '.']
        p = 0
        lis_2 = []
        labels = {"H": 0}
        expected_p = -2
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).goto_run_index())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_32(self):
        val = {"A": "H", "B": 8}
        lis = ['GOTO A', '.']
        p = 0
        lis_2 = []
        labels = {"H": 3}
        expected_p = 1
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).goto_run_index())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_33(self):
        val = {"A": "H", "B": 8}
        lis = ['GOTO A', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        try:
            for i in grin.parse(lis):
                lis_2.append(grin.Goto(i, val, p, labels).goto_run_index())
        except Exception as e:
            self.assertEqual("Label does not exist", str(e))

    def test_goto_cond_34(self):
        val = {"A": 5, "B": 5}
        lis = ['GOTO 10 IF B = A', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 9
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_35(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF B = A', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_36(self):
        val = {"A": 0, "B": 7}
        lis = ['GOTO 10 IF B <> C', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 9
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_37(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF C <> A', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_38(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF 0 <> C', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

    def test_goto_cond_39(self):
        val = {"A": 0, "B": 5}
        lis = ['GOTO 10 IF 0 <> A', '.']
        p = 0
        lis_2 = []
        labels = {}
        expected_p = 0
        for i in grin.parse(lis):
            lis_2.append(grin.Goto(i, val, p, labels).check_if())
        self.assertEqual(expected_p, lis_2[0])

if __name__ == '__main__':
    unittest.main()