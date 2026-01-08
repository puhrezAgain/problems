def validate_parens(cs: str):
    stack = []

    for c in cs:
        match c:
            case "{" | "[" | "(":
                stack.append(c)
            case "}":
                if not stack or stack[-1] != "{":
                    return False
                del stack[-1]
            case "]":
                if not stack or stack[-1] != "[":
                    return False
                del stack[-1]
                
            case ")":
                if not stack or stack[-1] != "(":
                    return False
                del stack[-1]
                
    return not stack

assert validate_parens("()[]{}")
assert not validate_parens("(]")
assert validate_parens("([{}])")
assert not validate_parens("]]][[[")
assert not validate_parens("[[]]]")
assert not validate_parens("{[}]")

