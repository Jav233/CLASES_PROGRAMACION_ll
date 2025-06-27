def fibonacci(n):
    if n <= 0:
        return 0
    
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = int(input("Ingrese el numero: "))
    if n < 0:
        print("Solo numeros positivos.")
    else:
        result = fibonacci(n)
        for i in range(n):
            print(f"Posición {i}: {fibonacci(i)}")
        print(f"El numero {n} en Fibonacci es: {result}")
        
if __name__ == "__main__":
    main()
    
def fibonacci_iterativo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

def main_iterativo():
    n = int(input("Ingrese el numero: "))
    if n < 0:
        print("Solo numeros positivos.")
    else:
        result = fibonacci_iterativo(n)
        for i in range(n):
            print(f"Posición {i}: {fibonacci_iterativo(i)}")
        print(f"El numero {n} en Fibonacci es: {result}")
        
if __name__ == "__main__":
    main_iterativo()  