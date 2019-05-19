import modules

n = input('Write fibonacci series up to: ')

myFibNo = modules.FibonacciNumbers(n)
result = myFibNo.calc()

print(result)
print("Finished")
