idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
}
# for key, value in idioms.items():
#     print(f"{key}: {' '.join(value)}")

my_family = {
    "sister": {
        "name": "Allison",
        "age": 31
    },
    "mother": {
        "name": "Darlene",
        "age": 67
    },
    "father": {
        "name": "Paul",
        "age": 64
    }
}

# {print(f'{value["name"]} is my {key} and is {value["age"]} years old')
#  for key, value in my_family.items()}


stockDict = {
    "GM": "General Motors",
    "CAT": "Caterpillar",
    "EK": "Eastman Kodak"
}

purchases = [
    ('GM', 100, '10-sep-2001', 48),
    ('CAT', 100, '1-apr-1999', 24),
    ('EK', 200, '1-jul-1998', 56),
    ('GM', 200, '1-jul-1998', 56)
]


def purchase_history():
    for each_tuple in purchases:
        price = each_tuple[1] * each_tuple[3]
        for key, value in stockDict.items():
            if each_tuple[0] is key:
                name = value
                print(f"I bought {name} stock for ${price}")


# purchase_history()

def purchas_history_2():
    new_dict = {}
    for each in purchases:
        if each[0] not in new_dict:
            new_dict[each[0]] = {}
    for key, value in new_dict.items():
        new_dict[key] = []
        for each in purchases:
            if each[0] is key:
                new_dict[key].append(each)
    for key, value in new_dict.items():
        if len(new_dict[key]) is 1:
            print(f"------ {new_dict[key][0][0]} ------")
            print(
                f"{new_dict[key][0][1]} shares at ${new_dict[key][0][3]} each on {new_dict[key][0][2]}")
            print("")
            print(
                f"Total value of stock in portfolio: ${new_dict[key][0][3] * new_dict[key][0][1]}")
            print("")
            print("")
        elif len(new_dict[key]) > 1:
            print(f"------ {new_dict[key][0][0]} ------")
            tuples_list = new_dict[key]
            total_list = []
            for each in tuples_list:
                print(f"{each[1]} shares at ${each[3]} on {each[2]}")
                total = each[1] * each[3]
                total_list.append(total)
            print("")
            print(f"Total value of stock portfolio: ${sum(total_list)}")
            print("")
            print("")
            
purchas_history_2()
