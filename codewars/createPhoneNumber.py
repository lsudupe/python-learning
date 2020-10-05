#Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
#create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
'''def create_phone_number(n):
    parentheses1Index = [0]
    parentheses2Index = [4]
    spaceIndex = [5]
    guionIndex = [9]
    telefoneNumber = ''
    for i in parentheses1Index:
        n.insert(i,'(')
    for i2 in parentheses2Index:
        n.insert(i2, ')')
    for i3 in spaceIndex:
        n.insert(i3, ' ')
    for i4 in guionIndex:
        n.insert(i4, '-')

    
    telefoneNumber = ''.join(str(i) for i in n)
    return telefoneNumber'''



def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(create_phone_number(array))




