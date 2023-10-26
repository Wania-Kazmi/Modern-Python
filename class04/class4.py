from typing import Any


name: str = 333
# print(name)


names: list[Any] = ["Wania", "Kazmi", 22]
# print(names)

# class-5

# on tuple we can do everything like slicing, indexing and all but we cannot update it as it is immutable

# database: list[tuple[str, str]] = [
#     ("wania", "123"), ("qasim", "345"), ("roma", "678")]

# for row in database:
#     print(row)

# value = input("Enter value: ")
# print(f"{value} found")

database1: list[tuple[str, str]] = [
    ("wania", "123"), ("qasim", "345"), ("roma", "678")]

input_user : str = input("Enter username: ")
input_password : str = input("Enter your password: ")
    
# now we want to match both username and password to database variable 

for row in database1:
    user, password = row 
#     print(user,password)
    if input_user == user and input_password == password:
        print("Valid User")
        break
else:
    print("Invalid User or Not found")