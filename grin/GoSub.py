#Handles GoSub operations
import grin


class GoSub(grin.Goto):
    """Handles the GoSub token"""
    def __init__(self, token, vals, p, labels):
        super().__init__(token, vals, p, labels)

    def gosub_run(self) -> int:
        """Calls on GOTO and returns the index"""
        if len(self.token) == 2:
            return self.goto_run_index()
        elif self.token[2].kind == grin.GrinTokenKind.IF:
            return self.check_if()


class Return_sub(grin.Goto):
    """Handles the Return Token"""
    def __init__(self, token, vals, p, labels, ret_lis):
        super().__init__(token, vals, p, labels)
        self.ret_lis = ret_lis

    def gosub_return(self) -> int:
        """Returns the index of the location for the last known GoSub"""
        if len(self.ret_lis) > 0:
            self.p = self.ret_lis[-1]
            self.ret_lis.pop(-1)
            return self.p
        else:
            raise RuntimeError("No GoSub encountered")
