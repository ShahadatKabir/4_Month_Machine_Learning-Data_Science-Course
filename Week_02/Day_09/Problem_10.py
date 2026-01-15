# State Retention

def accumulator(numbers):
    count = 0
    total = 0
    while True:
        val = yield total
        total += val
        count += 1
        result = total / count
        #yield result
        print(f"Current average is: {result:.2f}")


numbers = [45,76,12,88,34,23,90]

gen = accumulator(numbers)
print(next(gen))  

for num in numbers:
    print(gen.send(num))

"""
# Output:
0
Current average is: 45.00
45
Current average is: 60.50
121
Current average is: 44.33
133
Current average is: 55.25
221
Current average is: 51.00
255
Current average is: 46.33
278
Current average is: 52.57
368
"""
