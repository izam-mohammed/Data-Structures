def is_valid_parenthesis(s):
    stack = []
    parenthesis = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in parenthesis.values():
            stack.append(char)
        elif char in parenthesis.keys():
            if not stack or stack.pop() != parenthesis[char]:
                return False
        else:
            return False
    return len(stack) == 0


# tesitng

if __name__ == "__main__":
    s_true = "[()({})]"
    s_false = "[()({)}]"

    if is_valid_parenthesis(s_true):
        print(s_true, "is a valid parenthesis")
    else:
        print(s_true, "is not a valid parenthesis")
    if is_valid_parenthesis(s_false):
        print(s_false, "is a valid parenthesis")
    else:
        print(s_false, "is not a valid parenthesis")
