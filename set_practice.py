showroom = set()
showroom.add("corvette")
showroom.add("civic")
showroom.add("tahoe")
showroom.add("accord")
showroom.add("accord")
showroom.update(["silverado", "prius"])
showroom.discard("tahoe")
# print(showroom, len(showroom))

junkyard = set()
junkyard.add("sonata")
junkyard.add("bug")
junkyard.add("civic")
# print(junkyard)

# print(showroom.intersection(junkyard))

makes = (
    (1, "Toyota"), (2, "Nissan"),
    (3, "Ford"), (4, "Mini"),
    (5, "Honda"), (6, "Dodge"),
)

models = (
    (1, "Altima", 2), (2, "Thunderbird", 3),
    (3, "Dart", 6), (4, "Accord", 5),
    (5, "Prius", 1), (6, "Countryman", 4),
    (7, "Camry", 1), (8, "F150", 3),
    (9, "Civic", 5), (10, "Ram", 6),
    (11, "Cooper", 4), (12, "Pilot", 5),
    (13, "Xterra", 2), (14, "Sentra", 2),
    (15, "Charger", 6)
)

colors = (
    (1, "Black"), (2, "Charcoal"), (3, "Red"), (4, "Brick"),
    (5, "Blue"), (6, "Navy"), (7, "White"), (8, "Ivory")
)

available_car_colors = (
    (1, 1), (1, 2), (1, 7),
    (2, 1), (2, 3), (2, 7),
    (3, 2), (3, 3), (3, 7),
    (4, 3), (4, 5), (4, 8),
    (5, 2), (5, 4), (5, 8),
    (6, 2), (6, 6), (6, 7),
    (7, 1), (7, 3), (7, 7),
    (8, 1), (8, 5), (8, 8),
    (9, 1), (9, 6), (9, 7),
    (10, 2), (10, 5), (10, 7),
    (11, 3), (11, 6), (11, 8),
    (12, 1), (12, 4), (12, 7),
    (13, 2), (13, 6), (13, 8),
    (14, 2), (14, 5), (14, 8),
    (15, 1), (15, 4), (15, 7)
)

for make in makes:
    outer_dict = dict((b, a) for a, b in makes)
# print(outer_dict)
for key, value in outer_dict.items():
    model_list = []
    for model in models:
        if model[2] is outer_dict[key]:
            model_list.append(list(model))
    outer_dict[key] = model_list
    # print(model_list)
    inner_dict = {}
    for each_list in outer_dict[key]:
        each_list.remove(each_list[2])
        each_list.reverse()
        inner_dict[each_list[0]] = each_list[1]
    outer_dict[key] = inner_dict
    # print(inner_dict)
# print(outer_dict)
available_car_colors_list = []
for each in available_car_colors:
    two_numbers_list = list(each)
    available_car_colors_list.append(two_numbers_list)
# print(available_car_colors_list)
colors_list = []
for each in colors:
    color_number_list = list(each)
    colors_list.append(color_number_list)
# print(colors_list)
available_car_colors_list_mutated = []
for each_pair in available_car_colors_list:
    for each_color in colors_list:
        if each_pair[1] is each_color[0]:
            another_list = [each_pair[0], each_color[1]]
            available_car_colors_list_mutated.append(another_list)
# print(available_car_colors_list_mutated)
for key1, value1 in outer_dict.items():
    for key2, value2 in value1.items():
        final_list = []
        for each_list in available_car_colors_list_mutated:
            if each_list[0] is value2:
                final_list.append(each_list[1])
        value1[key2] = final_list
print(outer_dict)
