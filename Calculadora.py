def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2
        

def calculadora():
    print('\n{:=^40}'.format(' Caluladora '))
    print('{:-^40}'.format(' Opções disponiveis: '))
    print('1 - Soma  \t2 - Subtração \n3 - Multiplicação  4 - Divisão')
    
    op= int(input('\nO que deseja fazer: '))
    
    if op == 1:
        n1= int(input('\nDigite primeiro número: '))
        n2= int(input('Digite segundo número: '))
        
        somar= soma(n1, n2)
        
        print('\n%d + %d = %d' %(n1, n2, somar))
    elif op == 2:
        n1= int(input('\nDigite primeiro número: '))
        n2= int(input('Digite segundo número: '))
        
        subtracao = sub(n1, n2)
        
        print('\n%d - %d = %d' %(n1, n2, subtracao))
    elif op == 3:
        n1= int(input('\nDigite primeiro número: '))
        n2= int(input('Digite segundo número: '))
        
        multiplicacao = mult(n1, n2)
        
        print('\n%d * %d = %d' %(n1, n2, multiplicacao))
    elif op == 4:
        n1= int(input('\nDigite primeiro número: '))
        n2= int(input('Digite segundo número: '))
        
        divisao = div(n1, n2)
        
        print('\n%d / %d = %d' %(n1, n2, divisao))
    else:
        print('\tErro!')

calculadora()