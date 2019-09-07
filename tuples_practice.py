zoo = ("dog", "bear", "zebra")
# print(zoo.index("dog"))
(thing1, thing2, thing3) = zoo
# print(thing1)
newZoo = list(zoo)
newZoo.extend(["elephant", "mouse"])
final = tuple(newZoo)
# print(final)

appliances = ("oven", "fridge", "coffee maker", "rice cooker")
more_appliances = ("microwave", "stove")
final_appliances = appliances + more_appliances
print(final_appliances)