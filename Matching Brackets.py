opening_brackets = ['(', '[', '{']
closing_brackets = [')', ']', '}']
bracket_matches = dict(zip(closing_brackets, opening_brackets))

def is_paired(input_string):
    stack = []
    for ch in input_string:
        if ch in opening_brackets:
            stack.append(ch)
        elif ch in closing_brackets:
            if not stack:
                return False
            if bracket_matches[ch] != stack.pop():
                return False
    return len(stack) == 0
