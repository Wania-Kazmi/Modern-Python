# from typing import Tuple, Dict
# def abc(a : int, b : int ,*param1 : Tuple[str,...], **param2 : Dict[str , str]) -> None:
#     print(a,b,param1,param2)
     
# abc(1,2, "a","b", value = 100, value2 = 200)

# name22 : str = 4567890
# print(name22)

# from typing import Callable
# def simple_decorator(func : Callable[[int], None]) -> Callable[[int], None]:
#     def wrapper(num1 : int):
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening before the function is called.")
#     return wrapper

# @simple_decorator
# def say_hello(num1 : int):
#     print(num1)

# say_hello(22)

# name : str = 2323
# print(name)


from typing import Tuple, Dict

def myFunc(a : int, b : int, param1 : Tuple[str, ...], *param2 : Dict[str , str]) -> None:
    print(a,b,param1,param2)
     
myFunc(1,2, ("Zia", "Wania", "Osman"))

myFunc(1,2, ("Zia", "Wania", "Osman"), {"name": "Zeeshan"}, {"city": "karachi"})