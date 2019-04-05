def braces(values):
    str_array = []
    close_brace = {']': '[', '}': '{', ')': '('}
    for value in values:
        brace_stack = []
        balanced = ""
        for brace in value:
            if brace in close_brace.keys():
                if len(brace_stack) == 0 or close_brace[brace] != brace_stack.pop():
                    balanced = "NO"
                    break
            if brace in close_brace.values():
                brace_stack.append(brace)
        if len(brace_stack) == 0 and balanced != "NO":
            balanced = "YES"
        str_array.append(balanced)
    return str_array

values = ["{}[]()","{[}]}"]
q1 = braces(values)
