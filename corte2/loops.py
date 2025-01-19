for i in range(100, 301):
    if(i%12) != 0:
        continue
    print(i)

#factorial#
while True:
    value = int(input("Enter a positive integer value: "))
    print("value: ", value)
    a = isinstance(value,int)
    if a == True and value > 0:
        fact = 1
        for i in range (1,value+ 1):
            fact = fact*i
        print(f'The factorial of {value} is: ',fact)
    else:
        print("pleas, enter a positive integer number")

 #condiiconal#
a = input("Enter a number: ")
a = int(a)
b = input("Enter b number: ")
b = float(b)
c = a + b

if a == b:
    print("equal")
else:
    print("Different")

print("Type of a is: ", type(a))
print("Type of b is: ", type(b))
print("c = ", c)

if type(a) == type(b):
    print("a and b are of the same type")
else:
    print("a and b are of different type")

#impares/pares#
for i in range (1,21):
    residual = i%2
    if residual == 0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')

#times#
for i in range (1,21):
    residual = i%2
    if residual == 0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')

#busqueda#
import time
cadena = 'Python'

for letra in cadena:
    if letra == 't':
        continue
    print(letra)
    time.sleep(1)

#primos#
import time
inicio = time.time()

for i in range(0,31):
    conta = 0
    for n in range(1, i+1):
        residue = i%n
        if residue == 0:
            conta = conta + 1

        if conta == 2:
            print(f'{i} Es un primo')

fin = time.time()
print("t = ", (fin - inicio)*1000) 

#primos2#
a = 1
value = input('Ingrese un valor: ')
value = int(value)

while a == 1:
    for i in range(1, value + 1):
        conta = 0
        for n in range(1, i+1):
            if i % n == 0:
            #if residue == 0:
                conta += 1    
    if conta == 2:
        print(f'{i} Es un primo')
        print("\n")
    else:
        print(f'{i} No es un primo')
        print("\n")

        print('Do you want to continue?. Press 1 to do that')

    a = input()
    a = int(a)

    if a != 1:
        break

    value = input('Ingrese un valor: ')
    value = int(value)

#True or false#
my_cool_variable = 7 + 8 == 11
print(my_cool_variable)


