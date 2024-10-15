# programa que cuenta las vocales de una frase
a=input('Escriba una frase o palabra y contaré cuantas vocales hay: ')
print(f'La frase o palabra que usted escribio es: {a}')

lista=[]
vocales='aeiouAEIOU'

for i in a:
    if i in vocales:
        lista.append(i)
             
print(f'En la palabra escrita hay: {len(lista)} letras y las letras son: {lista}')
