def spam():
    global eggs
    eggs = 'spam'   #Variável Global!

def bacon():
    eggs = 'bacon'  #Variável Local

def ham():
    print(eggs)     #Variável Global

eggs = 42           #Variável Global
spam()
print(eggs)