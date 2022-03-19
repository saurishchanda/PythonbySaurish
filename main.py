import random

print("****Welcome to the game****")
dice=["1","2","3","4","5","6"]

print("The die shows:")
roll=random.choices(dice,weights=[99,1,1,1,1,99])
print(roll)
