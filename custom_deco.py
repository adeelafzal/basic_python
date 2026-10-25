
# for passing multiple number of arguments 
# we can use *args andfor multiple number of keaywords **kwargs

def log_deco(func):
    def wrap(*args):
        print("Values", *args)
        result = func(*args)
        print("Result", result)
        return result
    return wrap

def greater_deco(func):
    def wrap(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return wrap

@log_deco
@greater_deco
def sub(a, b):
    return a - b

@log_deco
def sum(a, b, c):
    return a + b + c

print(sub(2, 4))
print(sum(4, 4, 2))