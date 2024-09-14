def suma():
  global a
  global b 
  a=int(input('Ingrese el valor de a: '))
  b=int(input('Ingrese el valor de a: '))
  return a+b

def resta():
    return a-b

def multiplicacion():
    return a*b

def division():
    return a/b

c=suma()
print(f'La suma de {a,b} es: {c}')

d=resta()
print(f'La resta de {a,b} es: {d}')

e=multiplicacion()
print(f'La multiplicacion de {a,b} es: {e}')

f=division()
print(f'La division de {a,b} es: {f}')
