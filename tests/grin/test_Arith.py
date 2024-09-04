import unittest
import grin


class Test_Arith(unittest.TestCase):

    def test_add_run(self):
        val = {"A": 10}
        val_2 = [{'A': 15}]
        lis = ['ADD A 5', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Add(i, val).add_run())
        self.assertEqual(val_2, lis_2)

    def test_add_run_2(self):
        val = {"A": 10}
        val_2 = [{'A': 10}]
        lis = ['ADD A B', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Add(i, val).add_run())
        self.assertEqual(val_2, lis_2)

    def test_add_run_3(self):
        val = {}
        val_2 = [{'A': 10}]
        lis = ['ADD A 10', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Add(i, val).add_run())
        self.assertEqual(val_2, lis_2)

    def test_add_run_4(self):
        val = {"A": 10, "B": 10}
        val_2 = [{'A': 20, 'B': 10}]
        lis = ['ADD A B', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Add(i, val).add_run())
        self.assertEqual(val_2, lis_2)

    def test_sub_run(self):
        val = {"A": 10}
        val_2 = [{'A': 5}]
        lis = ['SUB A 5', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Sub(i, val).sub_run())
        self.assertEqual(val_2, lis_2)

    def test_sub_run_2(self):
        val = {"A": 10}
        val_2 = [{'A': 10}]
        lis = ['SUB A B', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Sub(i, val).sub_run())
        self.assertEqual(val_2, lis_2)

    def test_sub_run_3(self):
        val = {}
        val_2 = [{'A': -10}]
        lis = ['SUB A 10', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Sub(i, val).sub_run())
        self.assertEqual(val_2, lis_2)

    def test_sub_run_4(self):
        val = {"A": 20, "B": 10}
        val_2 = [{'A': 10, 'B': 10}]
        lis = ['SUB A B', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Sub(i, val).sub_run())
        self.assertEqual(val_2, lis_2)

    def test_Mult_run(self):
        val = {"A": 10}
        val_2 = [{'A': 50}]
        lis = ['MULT A 5', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Mult(i, val).mult_run())
        self.assertEqual(val_2, lis_2)

    def test_mult_run_2(self):
        val = {"A": 10}
        val_2 = [{'A': 0}]
        lis = ['MULT A B', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Mult(i, val).mult_run())
        self.assertEqual(val_2, lis_2)

    def test_mult_run_3(self):
        val = {}
        val_2 = [{'A': 0}]
        lis = ['MULT A 10', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Mult(i, val).mult_run())
        self.assertEqual(val_2, lis_2)

    def test_mult_run_4(self):
        val = {"A": 20, "B": 10}
        val_2 = [{'A': 200, 'B': 10}]
        lis = ['MULT A B', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Mult(i, val).mult_run())
        self.assertEqual(val_2, lis_2)

    def test_div_run(self):
        val = {"A": 10}
        val_2 = [{'A': 2}]
        lis = ['DIV A 5', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Div(i, val).div_run())
        self.assertEqual(val_2, lis_2)

    def test_div_run_2(self):
        val = {"A": 10}
        lis = ['DIV A B', '.']
        lis_2 = []
        try:
            for i in grin.parse(lis):
                lis_2.append(grin.Div(i, val).div_run())
        except Exception as e:
            self.assertEqual("division by zero", str(e))

    def test_div_run_3(self):
        val = {}
        val_2 = [{'A': 0}]
        lis = ['DIV A 10', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Div(i, val).div_run())
        self.assertEqual(val_2, lis_2)

    def test_div_run_4(self):
        val = {"A": 20, "B": 10}
        val_2 = [{'A': 2, 'B': 10}]
        lis = ['DIV A B', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Div(i, val).div_run())
        self.assertEqual(val_2, lis_2)

    def test_div_run_5(self):
        val = {"A": 7, "B": 2}
        val_2 = [{'A': 3, 'B': 2}]
        lis = ['DIV A B', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Div(i, val).div_run())
        self.assertEqual(val_2, lis_2)

    def test_div_run_6(self):
        val = {"A": 7, "B": 2.0}
        val_2 = [{'A': 3.5, 'B': 2.0}]
        lis = ['DIV A B', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Div(i, val).div_run())
        self.assertEqual(val_2, lis_2)

    def test_div_run_7(self):
        val = {"A": 7}
        val_2 = [{'A': 3.5}]
        lis = ['DIV A 2.0', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.Div(i, val).div_run())
        self.assertEqual(val_2, lis_2)

if __name__ == '__main__':
    unittest.main()
