def yyd_decorator(func):
    def wrapTheFunction():
        print("[ Now calling: ", func.__name__)
 
        func()
 
        print("] Exit: ", func.__name__)
 
    return wrapTheFunction