

'''
def multiplicador(n):
    def multplica (x):
        return x * n
    return multplica

doblar = multiplicador(2)
triplicar = multiplicador(3)

print(f'La función doblar es: {doblar(7)}')
print(f'La función triplicar es: {triplicar(10)}')'''

# filter
uno=[0,7,88,1,6,4,8,99,5,149,230,13,963]
dos=list(filter(lambda x:x%2==0, uno))
print(dos)