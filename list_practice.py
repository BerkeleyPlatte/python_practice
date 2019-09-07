planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Neptune", "Pluto"])
planet_list.insert(1, "Venus")
planet_list.insert(2, "Varth")
rocky_planets = planet_list[0:4]
print(rocky_planets)
planet_list.remove("Pluto")

import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))
    
for num in range(0, 6):
    if num in my_randoms:
        print(f"my_randoms contains {num}")
    else: 
        print(f"my_randoms does not contain {num}")
        
spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
   ("HAL", "Jupiter"),
   ("Goofy", "Pluto")
] 

for each_planet in planet_list:
    for each_pair in spacecraft:
        if each_planet == each_pair[1]:
            print(f"{each_pair[0]} has vistited {each_planet}")
