#Handles Arith operations
import grin


class Add(grin.Token):
    """Handles the grin token ADD"""
    def __init__(self, token, vals):
        super().__init__(token)
        self.vals = vals

    def add_run(self) -> dict:
        """Adds the given values and variables together and updates the dictionary with the updated value"""
        if self.token[2].text in self.vals.keys():
            self.vals[self.token[1].text] += self.vals[self.token[2].value]
        elif self.token[1].text not in self.vals.keys():
            self.vals[self.token[1].text] = self.token[2].value + 0
        elif self.token[2].kind.category == grin.GrinTokenCategory.IDENTIFIER \
                and self.token[2].value not in self.vals.keys():
            self.vals[self.token[1].text] += 0
        elif self.token[1].text in self.vals.keys():
            self.vals[self.token[1].text] += self.token[2].value
        return self.vals


class Sub(grin.Token):
    """Handles the grin token SUB"""
    def __init__(self, token, vals):
        super().__init__(token)
        self.vals = vals

    def sub_run(self) -> dict:
        """Subtracts the given values and variables together and updates the dictionary with the updated value"""
        if self.token[2].value in self.vals.keys():
            self.vals[self.token[1].text] -= self.vals[self.token[2].value]
        elif self.token[1].text not in self.vals.keys():
            self.vals[self.token[1].text] = 0 - self.token[2].value
        elif self.token[2].kind.category == grin.GrinTokenCategory.IDENTIFIER \
                and self.token[2].value not in self.vals.keys():
            self.vals[self.token[1].text] -= 0
        elif self.token[1].text in self.vals.keys():
            self.vals[self.token[1].text] -= self.token[2].value
        return self.vals


class Mult(grin.Token):
    """Handles the grin token MULT"""
    def __init__(self, token, vals):
        super().__init__(token)
        self.vals = vals

    def mult_run(self) -> dict:
        """Multiplies the given values and variables together and updates the dictionary with the updated value"""
        if self.token[2].value in self.vals.keys():
            self.vals[self.token[1].text] *= self.vals[self.token[2].value]
        elif self.token[1].text not in self.vals.keys():
            self.vals[self.token[1].text] = self.token[2].value * 0
        elif self.token[2].kind.category == grin.GrinTokenCategory.IDENTIFIER \
                and self.token[2].value not in self.vals.keys():
            self.vals[self.token[1].text] *= 0
        elif self.token[1].text in self.vals.keys():
            self.vals[self.token[1].text] *= self.token[2].value
        return self.vals


class Div(grin.Token):
    """Handles the grin token DIV"""
    def __init__(self, token, vals):
        super().__init__(token)
        self.vals = vals

    def div_run(self) -> dict:
        """Divides the given values and variables together and updates the dictionary with the updated value"""
        if self.token[2].value in self.vals.keys():
            if type(self.vals[self.token[1].text]) is int and type(self.vals[self.token[2].value]) is int:
                self.vals[self.token[1].text] = int(self.vals[self.token[1].text] / self.vals[self.token[2].value])
            else:
                self.vals[self.token[1].text] /= self.vals[self.token[2].value]
        elif self.token[1].text not in self.vals.keys():
            self.vals[self.token[1].text] = 0 / self.token[2].value
        elif self.token[2].kind.category == grin.GrinTokenCategory.IDENTIFIER \
                and self.token[2].value not in self.vals.keys():
            self.vals[self.token[1].text] /= 0
        elif self.token[1].text in self.vals.keys():
            if type(self.vals[self.token[1].text]) is int and type(self.token[2].value) is int:
                self.vals[self.token[1].text] = int(self.vals[self.token[1].text] / self.token[2].value)
            else:
                self.vals[self.token[1].text] /= self.token[2].value
        return self.vals
