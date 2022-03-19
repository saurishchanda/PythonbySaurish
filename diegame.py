import random

print("****Welcome to the game****")
dice=["1","2","3","4","5","6"]

print("Die 1 shows:")
roll1=random.choices(dice,weights=[1,1,1,1,1,45])
print(roll1)


print("Die 2 shows:")
roll2=random.choices(dice,weights=[45,1,1,1,1,1])
print(roll2)

print("Die 3 shows:")
roll3=random.choices(dice,weights=[45,1,1,1,1,1])
print(roll3)


