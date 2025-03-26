def caching_fibonacci(): # створення функцій Ряд Фібоначчі
    cache = {}

    def fibonacci(n): # функція для обчислення 
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # формула
        return cache[n]
    
    return fibonacci

# отримуємо функцію fibonacci
fib = caching_fibonacci()

# використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610