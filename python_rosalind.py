#import this
#hipotenusa
'''a = 959 
b = 815
def hipotenusa(x, y):
    hipotenusa = (x**2) + (y**2)
    return hipotenusa
print(hipotenusa(a, b))'''
#strings and lists
'''string = 'fOy8LJ59lrOlGsIgQw9KgCPPhd2MylopharyngodonxsdqiYM8k1vSH5l3C9HLLrESMkizKcrocodilusa8X3sfUvXq0jhGURcitLxeUhkAFvzRE0lKUq5Ri1nqW6MSNWO9LhaaPgKZ8agGiyqVTHy7opNuiFK1c6ziDy458Ty17RL7BP.'
a = 27 
b = 41
c = 71
d = 80
def slice(string, a, b, c, d):
    a = string[a:b +1]
    b = string[c:d]
    return (str(a) + ' ' + str(b))
print(slice(string, a, b, c, d))
print(f'{string[a:b + 1]} {string[c:d + 1]}')'''
#Conditions and Loops
'''a = 4752 
b = 9123
def impares(a, b):
    sum = 0
    for i in range(a,b +1):
        if i % 2 != 0:
            sum += i
    return sum
print(impares(a,b))
o
result = sum([i for i in range(a,b +1) if x % 2 != 0])'''
#Working with Files

'''lineas_seleccionadas = []
with open('pruebas visual code/rosalind_prueba.txt', 'r') as f:
    lineas_seleccionadas = [line for pos, line in enumerate(f.readlines()) if pos % 2 != 0]
print(lineas_seleccionadas)
   
with open('pruebas visual code/rosalind_prueba_output.txt', 'w') as f:
    f.write(''.join([line for line in lineas_seleccionadas]))'''



    
    
