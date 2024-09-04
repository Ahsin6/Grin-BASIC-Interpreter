import unittest
import grin



class test_let(unittest.TestCase):
    def test_token(self):
        expected =[grin.GrinToken(
                kind = grin.GrinTokenKind.LET, text = 'LET', value = 'LET',
                location = grin.GrinLocation(1, 10)),
            grin.GrinToken(
                kind = grin.GrinTokenKind.IDENTIFIER, text = 'NAME', value = 'NAME',
                location = grin.GrinLocation(1, 14)),
            grin.GrinToken(
                kind = grin.GrinTokenKind.LITERAL_STRING, text = '"Boo"', value = 'Boo',
                location = grin.GrinLocation(1, 19))]


        self.assertEqual(grin.let.Token(expected).token, expected)


    def test_let_run(self):
        val = {}
        val_2 = [{'A': 5, 'B': 5, 'C': 0}, {'A': 5, 'B': 5, 'C': 0}, {'A': 5, 'B': 5, 'C': 0}]
        lis = ['LET A 5', 'LET B A', 'LET C D', '.']
        lis_2 = []
        for i in grin.parse(lis):
            lis_2.append(grin.LET(i, val).let_run())
        self.assertEqual(val_2, lis_2)

if __name__ == '__main__':
    unittest.main()