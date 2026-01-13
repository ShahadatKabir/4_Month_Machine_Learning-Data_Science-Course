# The Quadratic Nested Loop(O(N^2))
 
common_data = []

list_1 = [12,43,24,134,65]
list_2 = [33,12,56,77,23,86]

def duplicates(list_1, list_2):
    for value1 in list_1:
        for value2 in list_2:
            if value1 == value2:
                common_data.append(value1)

duplicates(list_1, list_2)
print(f"The common datas are: {common_data}")
