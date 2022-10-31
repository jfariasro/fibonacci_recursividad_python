def Fibonacci(numero):
    if(numero == 0 or numero == 1):
        return numero
    else:
        return Fibonacci(numero - 1) + Fibonacci(numero - 2)

for i in range(1, 10+1):
    print(Fibonacci(i))