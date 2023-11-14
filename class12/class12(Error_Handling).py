print("logic1")
print("logic2")

l1 : list[int] = [1,2,3]

try:
    print(5/2)# Error
    print(l1[0]) #NotError
    print(xyz) #Error 
except (ZeroDivisionError):
    print("Zero Division Error!")

except (IndexError):
    print("Index Error!")

except (NameError):
    print("Name Error!")

print("logic4")