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


