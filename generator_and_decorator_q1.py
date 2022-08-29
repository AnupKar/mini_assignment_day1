def decFunc(func1):
    def mainFunc(*args, **kwargs):
        func1(*args, **kwargs)
        func1(*args, **kwargs)
    return mainFunc

@decFunc

def multiply(num1, num2):
    print(num1 * num2)
multiply(2,3)

