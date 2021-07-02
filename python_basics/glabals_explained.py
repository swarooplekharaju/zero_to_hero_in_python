import  config
print(config.a)
config.a = "hello"
print(config.a)
def main_function():
    x ="i will "
    def inner_function():
        global x
        x = "i will be ceo by 2030"
    print("x before calling inner function",x)
    inner_function()
    print("x after calling inner function", x)
main_function()
print(x)







