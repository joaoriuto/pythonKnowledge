catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +              '(Or enter nothing to Stop.): ')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] #Concatenação de lista

print('The cat names are: ')
for name in catNames:
    print(' ' + name)