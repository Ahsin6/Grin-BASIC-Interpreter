#Handles Let operations
import grin


class Token:
    def __init__(self, token):
        self.token = token


class LET(Token):
    """Creates and stores variables with their values in a dictionary"""

    def __init__(self, token, vals):
        super().__init__(token)
        self.vals = vals

    def let_run(self) -> dict:
        """Checks the type of input and returns a new dictionary with a new variable"""
        if self.token[2].value in self.vals.keys():
            self.vals[self.token[1].text] = self.vals[self.token[2].value]
        elif self.token[2].kind.category == grin.GrinTokenCategory.IDENTIFIER \
                and self.token[1].text not in self.vals.keys():
            self.vals[self.token[1].text] = 0
        else:
            self.vals[self.token[1].text] = self.token[2].value
        return self.vals
