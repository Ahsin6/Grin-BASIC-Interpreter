import unittest
import grin
import unittest.mock


class test_in(unittest.TestCase):

    def test_Innum(self):
        val = {}
        val_2 = [{'A': 50}]
        lis = ['INNUM A']
        lis_2 = []
        for i in grin.parse(lis):
            with unittest.mock.patch('builtins.input', return_value="50"):
                lis_2.append(grin.Innum(i, val).innum_run())
        self.assertEqual(val_2, lis_2)

    def test_Innum_2(self):
        val = {}
        val_2 = [{'A': 50.5}]
        lis = ['INNUM A']
        lis_2 = []
        for i in grin.parse(lis):
            with unittest.mock.patch('builtins.input', return_value="50.5"):
                lis_2.append(grin.Innum(i, val).innum_run())
        self.assertEqual(val_2, lis_2)

    def test_Innum_3(self):
        val = {}
        lis = ['INNUM A']
        try:
            for i in grin.parse(lis):
                with unittest.mock.patch('builtins.input', return_value="ABC"):
                    grin.Innum(i, val).innum_run()
        except Exception as e:
            self.assertRaises(TypeError, e)

    def test_instr(self):
        val = {}
        val_2 = [{'A': "HELLO"}]
        lis = ['INSTR A']
        lis_2 = []
        for i in grin.parse(lis):
            with unittest.mock.patch('builtins.input', return_value="HELLO"):
                lis_2.append(grin.Instr(i, val).instr_run())
        self.assertEqual(val_2, lis_2)


if __name__ == '__main__':
    unittest.main()
