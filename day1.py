def upper_dec(func ):
    def wrapper():
        result = func()
        return result.upper()
    return upper_dec

def test1():
    return "Hello World"

print(test1())