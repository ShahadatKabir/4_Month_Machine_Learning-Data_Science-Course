# The Stacked Decorator

def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper


@bold
@italic
def format():
    return "Shahadat"
print(format())
