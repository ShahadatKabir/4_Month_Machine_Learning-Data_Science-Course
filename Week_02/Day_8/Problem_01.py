# The Linear Scan (O(N))

def linear_scan(data, target):
    idx = 0
    while idx < len(data):  
        if data[idx] == target:
            return True
        idx += 1
    return False

print(linear_scan(list(range(1000000)), -5))
