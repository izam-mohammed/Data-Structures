def valid_parenthesis(s):
    stack = []
    brackets = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or stack.pop() != brackets[char]:
                return False
        else:
            return False
    return not stack


input_string = "([{}[]])"
print(valid_parenthesis(input_string))
