import copy
from collections import Counter
items = {
    'arrow': 12,
    'gold coin': 42,
    'rope': 1,
    'torch': 6,
    'dagger': 1
}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'gold coin', 'ruby', 'ruby', 'wand of vortex'] #<- Add itens Here!

def displayInventory(inventItems):
    copyInvent = copy.copy(inventItems)
    totalItems = 0
    print('Inventory: ')
    for k, v in copyInvent.items():
        print(str(v) + ' ' + k)
        totalItems += v
    print('Total number of items: ' + str(totalItems))


def addToInventory(invent, addItems):
    novosItems = []
    inventLoot = {}        
    for i in addItems:
        total = addItems.count(i)
        if i not in novosItems:
            novosItems.append(i)
            novosItems.append(total)
   
    itensTupla = tuple(novosItems)
     
    itensDic = dict(itensTupla[i: i + 2] for i in range(0, len(itensTupla), 2))
    inventLoot = itensDic
    #print(inventLoot) <- Testa a conversão     
    soma = Counter(invent) + Counter(inventLoot)
    return soma

items = addToInventory(items, dragonLoot)      
displayInventory(items)
