def generating(howMany):
    fibonacci = []
    for n in range(0, howMany):
        if(n == 0 or n == 1):
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[n - 1] + fibonacci[n - 2])
    print(fibonacci)


while True:
    try:
        howMany = int(input("How many Fibonacci numbers do you want? "))
        break
    except ValueError:
        print("Your value must be integer or float type")

generating(howMany)
