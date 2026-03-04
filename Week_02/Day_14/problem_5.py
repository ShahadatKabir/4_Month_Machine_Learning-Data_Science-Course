def fizzbuzz(number):
    for i in range(0, number):
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return str(number)
    

number = 100
for i in range(1, number):
    print(fizzbuzz(i))
