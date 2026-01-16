# The Filter of filtering the non-zeros

numbers = [45,23,54,-10,19,-100]

non_zeros = list(filter(lambda x: x >= 0, numbers))

print(non_zeros)                # Output: [45, 23, 54, 19]
