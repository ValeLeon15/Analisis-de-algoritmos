from math import gcd

def problem_1(limite):
    suma=0

    for i in range (1,limite):
        if i%3==0 or i%5==0:
            suma=suma+i
    return suma

def problem_2(limite):
    suma = 0
    fibIn = 1
    fibActual = 2

    while fibActual <= limite:
        if fibActual % 2 == 0:
            suma += fibActual
        temp=fibIn
        fibIn = fibActual
        fibActual = temp + fibActual
    return suma

def problem_3(limite):
    primo = 2
    while (primo * primo) <= limite:
        while limite % primo == 0:
            limite =limite//primo #devuelve la division entera sin decimales
        primo += 1
    if limite > 1:
        return limite
    return primo
 
def palindromo(numero):
    return str(numero) == str(numero)[::-1]

def buscarPalindromoMasGrande():
    palindromoMasGrande = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            producto = i * j
            if palindromo(producto) and producto > palindromoMasGrande:
                palindromoMasGrande = producto
    return palindromoMasGrande

def problem_4():
    return buscarPalindromoMasGrande()

def problem_5(limite):
    mcm = 1
    for i in range(2, limite + 1):
        mcm = mcm * i // gcd(mcm, i) #con gcd sacamos el maximo comun divisor
    return mcm
    

print(problem_1(10))
print(problem_1(1000))
print(problem_2(10)) #no entiendo bien
print(problem_3(13195))
print(problem_3(600851475143))
print(problem_4())
print(problem_5(10))
print(problem_5(20))
