import grin
from grin.let import Token


class Print(Token):
    """Class to handle the GRIN token PRINT"""
    def __init__(self, token, vals):
        super().__init__(token)
        self.vals = vals
        self.print_run()

    def print_run(self) -> None:
        """Checks if the printing object is a variable or literal value and print the object"""

        if self.token[1].kind.category == grin.GrinTokenCategory.LITERAL_VALUE:
            print(self.token[1].value)
        else:
            if self.token[1].text in self.vals.keys():
                print(self.vals[self.token[1].text])
            else:
                print(0)
