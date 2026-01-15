# Decorators with Arguments

def repeat(times):
    def deco(func):
        def wrap():
            for _ in range(times):
                func()
        return wrap
    return deco

@repeat(3)
def hello():
    print("Anika")

hello()
