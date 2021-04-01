#Formar imagem com lista de caracteres X e Y
import copy
from textwrap import wrap
grid = [
    ['.','.','.','.','.','.'],
    ['.','0','0','.','.','.'],
    ['0','0','0','0','.','.'],
    ['0','0','0','0','0','.'],
    ['.','0','0','0','0','0'],
    ['0','0','0','0','0','.'],
    ['0','0','0','0','.','.'],
    ['.','0','0','.','.','.'],
    ['.','.','.','.','.','.']
    ]
newList = []
def imagem(lista):
    job = copy.copy(lista) 
    tamanho = len(job)
    new = []
    x = 0
    y = 0
    for i in range(6):             
       x += 1
       y += 1
       #print(i)
       for j in range(tamanho):
           #print(lista[i][j], end='')
           new.append(job[j][i])

    novoNew = ''.join(new)       
    for line in wrap(novoNew, width=9):
        print(line)       
    #print(novoNew)

imagem(grid)    