#solve("our code") = "edo cruo"
string = 'your code rocks'

def solve(word):
  #el primer paso de la función es darle la vuelta al string.Check
  reverse = ''
  reverse_nospace = []
  for char in range(len(word)-1, -1, -1):
    reverse += word[char] 
  for i in reverse:
    reverse_nospace.append(i)

  #el segundo paso buscar el index de los espacios, usare list comprehension [expression for item in list]
  char_list = []
  index = []
  for char in word:
    char_list.append(char)
  for idx, space in enumerate(char_list):
    if space == ' ':
      index.append(idx)
  #return index
  #el tercero, hacer que coincidan los espacios
  final_string = ''
  for position in index:
    reverse_nospace.insert(position, ' ')
  final_string = ''.join(reverse_nospace)

  return final_string
    
  
print(solve(string))

