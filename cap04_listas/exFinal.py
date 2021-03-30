#Exercício final do capítulo 04

#Código para vírgulas:
import copy
spam = ['apples', 'bananas', 'tofu', 'cats', 'Arroz']

def processador(arquivoIn):
    arqRecebido = copy.copy(arquivoIn)
    frase = []
    num = len(arqRecebido)
    posicaoAnd = int(num -1)
    
    for itens in arqRecebido:    
      frase.append(itens)
      
            
    frase.insert(posicaoAnd, 'and')     
    fraseCast = ', '.join(frase)
    
    
    print(fraseCast)
    

processador(spam)