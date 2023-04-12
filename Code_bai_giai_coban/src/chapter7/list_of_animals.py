# xử lý list
list_animal = ['ant', 'bear', 'cat', 'dog',
               'elephant', 'fish', 'goat', 'hippo']
print('List of animals:', list_animal)
print('Number of animals:', len(list_animal))
animal = input('I want to find: ').strip()
if animal.upper() in [x.upper() for x in list_animal]:
    print('There is', animal, 'in list of animals')
else:
    print('There is no', animal, 'in list of animals')
