def isValid(string):
    stack = []
    mapping = { ")": "(", "]": "[", "}": "{" }

    for ch in string:
        if ch in mapping:
            element = stack.pop() if stack else '#'
            if mapping[ch] != element:
                return
        else:
            stack.append(ch)
    return stack == []
