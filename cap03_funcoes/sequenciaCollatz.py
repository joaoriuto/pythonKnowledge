def collatz(number):  
    if (number % 2 == 0):
        print(number // 2)
        valor = number // 2
        return valor        
    else:
        print(3 * number + 1)
        valor = 3 * number +1
        return valor    
            
try:
    valor = int(input('Informe um número: '))
    while valor != 1:
        valor = collatz(int(valor))
except ValueError:
    print("Insira um número inteiro!")





    