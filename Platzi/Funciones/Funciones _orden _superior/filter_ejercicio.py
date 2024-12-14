# Filter 
def fil():
    l=[1,2,3,4,5,6,7,8,9,10,11,12]
    a= list(filter(lambda x: x%2==0, l))
    print(f'La lista filtrada es: {a}')
    print('-'*50)
    b=tuple(filter(lambda x: x%2==0, l))
    print(f'La tupla filtrada es: {b}')



if __name__=='__main__':
    print('')
    fil()
    print('')