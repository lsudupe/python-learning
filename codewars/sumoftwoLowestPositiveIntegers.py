'''Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
[10, 343445353, 3453445, 3453545353453] should return 3453455.'''
numbers = [10, 343445353, 3453445, 3453545353453]

'''def sum_two_smallest_numbers(numbers):
    lowOneNum = 100000000000000000000
    lowTwoNum = 100000000000000000000
    for num in numbers:
        if num < lowOneNum and num > 0 and num == float:
            lowOneNum = num
    for num in numbers:
        if num < lowTwoNum and num > 0 and num == float:
            lowTwoNum = num
    finalNum = lowOneNum + lowTwoNum
    return finalNum
print(sum_two_smallest_numbers(numbers))'''

lista = [4, 5, 3, 7]
def funcion(lista):
    sortList = sorted(lista)
    print(sortList[0] + sortList[1])

       
funcion(lista)
