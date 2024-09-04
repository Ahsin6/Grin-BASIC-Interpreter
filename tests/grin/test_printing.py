import unittest
import contextlib
import io
import grin


class TestPrint(unittest.TestCase):

    def test_print_run(self):
        val = {"A": 0, "B": 8}
        lis = ['PRINT "H"', '.']
        output_str = 'H\nH\n'
        with contextlib.redirect_stdout(io.StringIO()) as output:
            for i in grin.parse(lis):
                grin.Print(i, val).print_run()
        self.assertEqual(output.getvalue(), output_str)

    def test_print_run_2(self):
        val = {"A": "H", "B": 8}
        lis = ['PRINT A', '.']
        output_str = 'H\nH\n'
        with contextlib.redirect_stdout(io.StringIO()) as output:
            for i in grin.parse(lis):
                grin.Print(i, val).print_run()
        self.assertEqual(output.getvalue(), output_str)

    def test_print_run_3(self):
        val = {"A": "H", "B": 8}
        lis = ['PRINT C', '.']
        output_str = '0\n0\n'
        with contextlib.redirect_stdout(io.StringIO()) as output:
            for i in grin.parse(lis):
                grin.Print(i, val).print_run()
        self.assertEqual(output.getvalue(), output_str)


if __name__ == '__main__':
    unittest.main()
