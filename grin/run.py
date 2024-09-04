import grin


def run():
    """Runs the GRIN interpreter in its entirety, Taking input statements and parsing through them and handling all
    the tokens """
    statements = None
    tokens = [] #All the tokens are stored in this list
    vals = {} #All the variables are stored in this list
    labels = {} #all the labels are stored in this list
    ret_lis = [] #Last known location of GoSub is stored in this list
    stop_statement = ["."]
    while statements not in stop_statement:
        statements = input()
        tokens.append(statements)
    parsed = grin.parse(tokens)
    parsed_list = []

    for line in parsed:
        if line[0].kind != grin.GrinTokenKind.END and line[0].kind != grin.GrinTokenKind.RETURN:
            if line[1].kind == grin.GrinTokenKind.COLON:
                labels[line[0].value] = line[0].location.line
                line = line[2:]
        parsed_list.append(line)
    p = 0
    while p < len(parsed_list):
        lines = parsed_list[p]

        if lines[0].kind == grin.GrinTokenKind.LET:
            let = grin.LET(lines, vals)
            vals = let.let_run()

        elif lines[0].kind == grin.GrinTokenKind.END:
            break

        elif lines[0].kind == grin.GrinTokenKind.PRINT:
            grin.Print(lines, vals)

        elif lines[0].kind == grin.GrinTokenKind.INNUM:
            try:
                innum = grin.Innum(lines, vals)
                vals = innum.innum_run()
            except TypeError as e:
                print(e)
                break

        elif lines[0].kind == grin.GrinTokenKind.INSTR:
            instr = grin.Instr(lines, vals)
            vals = instr.instr_run()

        elif lines[0].kind == grin.GrinTokenKind.ADD:
            try:
                add = grin.Add(lines, vals)
                vals = add.add_run()
            except:
                print("RuntimeError: Cant Add")
                break

        elif lines[0].kind == grin.GrinTokenKind.SUB:
            try:
                sub = grin.Sub(lines, vals)
                vals = sub.sub_run()
            except TypeError:
                print("RuntimeError: Cant subtract")
                break

        elif lines[0].kind == grin.GrinTokenKind.MULT:
            try:
                mult = grin.Mult(lines, vals)
                vals = mult.mult_run()
            except:
                print("RuntimeError: Cant Multiply")
                break

        elif lines[0].kind == grin.GrinTokenKind.DIV:
            try:
                div = grin.Div(lines, vals)
                vals = div.div_run()
            except ZeroDivisionError:
                print("RuntimeError: Cant divide by zero")
                break
            except:
                print("RuntimeError: Cant divide")
                break

        elif lines[0].kind == grin.GrinTokenKind.GOTO:
            goto = grin.Goto(lines, vals, p, labels)
            try:
                if len(lines) == 2:
                    p = goto.goto_run_index()
                elif lines[2].kind == grin.GrinTokenKind.IF:
                    p = goto.check_if()
                if p+1 >= len(parsed_list) or p+1 < 0:
                    print("RuntimeError: Cant jump to that location")
                    break
            except RuntimeError as e:
                print(e)
                break
        elif lines[0].kind == grin.GrinTokenKind.GOSUB:
            ret_lis.append(p)
            gosub = grin.GoSub(lines, vals, p, labels)
            try:
                p = gosub.gosub_run()
                if p+1 >= len(parsed_list) or p+1 < 0:
                    print("RuntimeError: Cant jump to that location")
                    break
            except RuntimeError as e:
                print(e)
                break
        elif lines[0].kind == grin.GrinTokenKind.RETURN:
            ret = grin.Return_sub(lines, vals, p, labels, ret_lis)
            try:
                p = ret.gosub_return()
                if p+1 >= len(parsed_list) or p+1 < 0:
                    print("RuntimeError: Cant jump to that location")
                    break
            except RuntimeError as e:
                print(e)
                break
        p += 1

