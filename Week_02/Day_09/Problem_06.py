# The Pipeline (Chaining)
def squares(lst):
    return [num * num for num in lst]

def filter(lst):
    return [num for num in lst if num % 2 == 0]

lst = []
num = int(input("Enter a number: "))
for i in range(num):
    while True:
        try:
            lst.append(int(input(f"Enter for {i}th index: ")))
            break
        except ValueError: 
            print("Not a number")




def gen1_squarer(numbers):
    # Step - 1: Squaring the numbers.
    for i in numbers:
        result = i*i
        print(f"The squarer of {i} is:")
        yield result

def gen2_filters(data):
    # Step-2: Filtering even and odd numbers.
    for i in data:
        if i % 2 == 0:
            yield i
            print(f"{i} -> even")
        else:
            print(f"The number {i} is: odd")


pipeline = gen2_filters(gen1_squarer(lst))


# The final result

for i in pipeline:
    print(i)
