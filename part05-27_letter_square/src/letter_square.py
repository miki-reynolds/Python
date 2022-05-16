def square_letters(layers: int):
  letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  total = layers
  space = 0
  for i in reversed(range(1, layers)):

    cur_space = space
    nums = layers-1
    while(cur_space > 0):
      print(letters[nums],end='')
      cur_space-=1
      nums -= 1
    nums += 1
    
    for j in range(total*2-1):
      print(letters[i],end='')

    cur_space = space
    while(cur_space > 0):
      print(letters[nums],end='')
      cur_space-=1
      nums += 1
      
    total = total-1
    space += 1
    print()


  nums -= 1
  
  cur_space = space
  while(cur_space > 0):
    print(letters[nums],end='')
    cur_space-=1
    nums -= 1

  nums += 1
  
  print(letters[0],end='')

  cur_space = space
  while(cur_space > 0):
    print(letters[nums],end='')
    cur_space-=1
    nums += 1

  print()

  space -= 1
  total += 1
  
  for i in range(1, layers):
    cur_space = space
    nums = layers-1
    while(cur_space > 0):
      print(letters[nums],end='')
      cur_space-=1
      nums -= 1
    nums += 1
    
    for j in range(total*2-1):
      print(letters[i],end='')
      
    cur_space = space
    while(cur_space > 0):
      print(letters[nums],end='')
      cur_space-=1
      nums += 1
      
    total = total+1
    space -= 1
    print()

layers = 4
square_letters(layers)