# The Next Protocol

def for_loop(iterable):
    iterator = iter(iterable)

    while True:    
        try: 
            item = next(iterator)
            yield item
        except StopIteration:
            break

iterable = [5,8,99,34,67]
result = for_loop(iterable)

for i in result:
    print(i)


# Output:
#5
#8
#99
#34
#67
