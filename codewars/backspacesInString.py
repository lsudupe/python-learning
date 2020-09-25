s = 'ab#c###db'
def backspaces(s):
    for carac in s:
        if carac == '#':
            s.strip('#' - 1)
        s.strip('#')
    return s

print(backspaces(s))




