#Handles GoTo operations
import grin

class Goto(grin.Token):
    """Handles the grin token GOTO"""
    def __init__(self, token, vals, p, labels):
        super().__init__(token)
        self.vals = vals
        self.p = p
        self.index = None
        self.labels = labels

    def goto_run_index(self) -> int:
        """Jumps the execution of the program to the index of the value given by returning the index value"""
        if self.token[1].value in self.vals.keys():
            if self.vals[self.token[1].value] == 0:
                raise RuntimeError("Cant jump to zero")
            elif type(self.vals[self.token[1].value]) is not int:
                if self.vals[self.token[1].value] in self.labels.keys():
                    if self.labels[self.vals[self.token[1].value]] > self.p:
                        self.p += (self.labels[self.vals[self.token[1].value]] - self.p - 1) - 1
                    else:
                        self.p -= self.p - self.labels[self.vals[self.token[1].value]] + 2
                else:
                    raise RuntimeError("Label does not exist")
            else:
                self.p += self.vals[self.token[1].value] - 1
        elif self.token[1].kind.category == grin.GrinTokenCategory.IDENTIFIER \
                and self.token[1].value not in self.vals.keys():
            raise RuntimeError("Cant jump to zero")
        elif self.token[1].kind.category == grin.GrinTokenCategory.LITERAL_VALUE and type(self.token[1].value) is not int:
            if self.token[1].value in self.labels.keys():
                if self.labels[self.token[1].value] > self.p:
                    self.p += (self.labels[self.token[1].value] - self.p - 1) - 1
                else:
                    self.p -= self.p - self.labels[self.token[1].value] + 2
            else:
                raise RuntimeError("Label does not exist")
        elif self.token[1].value == 0:
            raise RuntimeError("Cant jump to zero")
        else:
            self.p += self.token[1].value - 1
        return self.p

    def check_if(self) -> int:
        """Checks if the conditional is True"""
        if self.token[3].kind.category == grin.GrinTokenCategory.IDENTIFIER and self.token[5].kind.category == grin.GrinTokenCategory.IDENTIFIER:
            if self.token[3].text not in self.vals.keys():
                value_1 = 0
            else:
                value_1 = self.vals[self.token[3].text]
            if self.token[5].text not in self.vals.keys():
                value_2 = 0
            else:
                value_2 = self.vals[self.token[5].text]
        elif self.token[3].kind.category == grin.GrinTokenCategory.IDENTIFIER:
            if self.token[3].text not in self.vals.keys():
                value_1 = 0
                value_2 = self.token[5].value
            else:
                value_1 = self.vals[self.token[3].text]
                value_2 = self.token[5].value
        elif self.token[5].kind.category == grin.GrinTokenCategory.IDENTIFIER:
            if self.token[5].text not in self.vals.keys():
                value_1 = self.token[3].value
                value_2 = 0
            else:
                value_1 = self.vals[self.token[5].text]
                value_2 = self.token[3].value
        else:
            value_1 = self.token[3].value
            value_2 = self.token[5].value
        if self.token[4].kind == grin.GrinTokenKind.LESS_THAN:
            if value_1 < value_2:
                return self.goto_run_index()
            else:
                return self.p
        elif self.token[4].kind == grin.GrinTokenKind.GREATER_THAN:
            if value_1 > value_2:
                return self.goto_run_index()
            else:
                return self.p
        elif self.token[4].kind == grin.GrinTokenKind.GREATER_THAN_OR_EQUAL:
            if value_1 >= value_2:
                return self.goto_run_index()
            else:
                return self.p
        elif self.token[4].kind == grin.GrinTokenKind.LESS_THAN_OR_EQUAL:
            if value_1 <= value_2:
                return self.goto_run_index()
            else:
                return self.p
        elif self.token[4].kind == grin.GrinTokenKind.EQUAL:
            if value_1 == value_2:
                return self.goto_run_index()
            else:
                return self.p
        elif self.token[4].kind == grin.GrinTokenKind.NOT_EQUAL:
            if value_1 != value_2:
                return self.goto_run_index()
            else:
                return self.p
