def flatten_lists(nested_lists):
    for item in nested_lists:
        if isinstance(item, list):
            yield from flatten_lists(item)
        else:
            yield item

data_list = [1, [2, [3, 4]]]
print(list(flatten_lists(data_list)))  
