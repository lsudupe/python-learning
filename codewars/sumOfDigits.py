#Given n, take the sum of the digits of n. If that value has more than one digit, 
#continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
#  942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6

number = 942
def digital_root(n):
    num_list = [int(num) for num in str(n)]
    for number in range(len(num_list)):
        while len(num_list) > 1:
            sum(range(num_list[number]))
    return num_list

print(digital_root(number))


print('laura')