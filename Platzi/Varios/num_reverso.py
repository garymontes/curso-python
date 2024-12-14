# programa que pide por teclado un número y lo invierte en su orden, de atras hacia adelante

def main():
    a=int(input('Ingrese el número que desea invertir: '))
    num_inv=0   
    
    while a>0:
        digito=a%10
        num_inv=num_inv*10+digito
        a=a//10
        
    print(f'El número invertido es: {num_inv} ')
    



if __name__=='__main__':
    print('')
    main()
    
    print('')