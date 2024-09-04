#Handles In operations
import grin


class Innum(grin.Token):
    """Handles the Grin token INNUM"""

    def __init__(self, token, vals):
        super().__init__(token)
        self.vals = vals
        self.num = None

    @staticmethod
    def _require_int_float(value, name):
        """Makes sure that input is of the right kind"""
        try:
            if "." in value:
                return float(value)
            else:
                return int(value)
        except:
            raise TypeError(f'{name} must be an integer or float, but was {type(value)}')

    def innum_run(self) -> dict:
        """Takes the input and stores it with the variable with the inputted value"""
        self.num = input("Enter a number: ")
        self.vals[self.token[1].text] = self._require_int_float(self.num, "Number")
        return self.vals


class Instr(grin.Token):
    """Handles the Grin token INSTR"""
    def __init__(self, token, vals):
        super().__init__(token)
        self.vals = vals
        self.str = None

    def instr_run(self) -> dict:
        """Takes the input and stores it with the variable with the inputted value"""
        self.str = input("Enter a string: ")
        self.vals[self.token[1].text] = self.str
        return self.vals
