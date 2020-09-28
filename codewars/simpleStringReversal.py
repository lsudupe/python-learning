#solve("our code") = "edo cruo"
string = 'Alex mat tie'

def solve(word):
  replace_string = word.replace(' ', '$')
  replace_list = replace_string.split()
  spacePosition = []
  for i, elem in enumerate(replace_list):
    if '$' in elem:
      spacePosition.append(i)

  reverse = ''
  for char in range(len(word)-1, -1, -1):
    reverse += word[char] 

  return spacePosition

print(solve(string))
