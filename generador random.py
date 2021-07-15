from random import randint , uniform

x = 0
print("1 = Femenino , 2 = Masculino")

for x in range (1,10):
    edad = randint(18,75)
    sexo = randint(1,2)
    sueldo = uniform(200,1000) 
    x += 1
    print ("{0:10}   {1:3}   {2:3.10f}".format(edad,sexo,sueldo))
